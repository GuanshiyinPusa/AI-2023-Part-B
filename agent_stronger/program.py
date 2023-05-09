# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part B: Game Playing Agent

from referee.game import \
    PlayerColor, Action, SpawnAction, SpreadAction, HexPos, HexDir, \
    Board

import time
import math
from random import randint
import random


# This is the entry point for your game playing agent. Currently the agent
# simply spawns a token at the centre of the board if playing as RED, and
# spreads a token at the centre of the board if playing as BLUE. This is
# intended to serve as an example of how to use the referee API -- obviously
# this is not a valid strategy for actually playing the game!

class Agent:
    def __init__(self, color: PlayerColor, **referee: dict):
        """
        Initialise the agent.
        """
        self._color = color
        match color:
            case PlayerColor.RED:
                print("Testing: I am playing as red")
            case PlayerColor.BLUE:
                print("Testing: I am playing as blue")
                
        self.board = Board()
        self.N = 7
        print("referee: ", referee)
        
    
    # get all the possible actions of the board, for color player 
    def get_all_possible_actions(self, color):
        action_list = []
        for i in range(self.N):
            for j in range(self.N):
                action = SpawnAction(HexPos(i, j))
                cell = action.cell
                
                # spawn action
                if self.board._total_power < self.N*self.N:
                    if not self.board._cell_occupied(cell):
                        action_list.append(action)
                
                if self.board[cell].player != color:
                    continue
                
                # spread action    
                for dir in [HexDir.DownRight, HexDir.Down, HexDir.DownLeft, \
                    HexDir.UpLeft, HexDir.Up, HexDir.UpRight]:
                    
                    action = SpreadAction(HexPos(i, j), dir)
                    action_list.append(action)
        
        random.shuffle(action_list)
        n = len(action_list)
        action_list = action_list[:(n>>1)+1]
        
        return action_list
        
    
    # simulate the whole game, with Max Step
    def simulation(self, cur_color, MaxStep=10):
        step, winner = 0, None
        # simulate the game
        while not self.board.game_over and step<MaxStep:
            cur_color = cur_color.opponent
            action_list = self.get_all_possible_actions(cur_color)
            
            # randomly pick an action
            index = randint(0, len(action_list)-1)
            action = action_list[index]
            self.board.apply_action(action)
            step += 1
        
        # game over
        if self.board.game_over:
            winner = self.board.winner_color
        else:
            # choose the winner
            red = self.board._color_power(PlayerColor.RED)
            blue = self.board._color_power(PlayerColor.BLUE)
            if red >= blue+0:
                winner = PlayerColor.RED
            elif blue >= red+0:
                winner = PlayerColor.BLUE
            else:
                winner = None
        
        # recover the board
        for i in range(step):
            self.board.undo_action()
        
        return winner

    
    # calculate the UCB based on the formula
    # Wi is the total number of wins
    # Si is the total number of playouts
    # Sp is the parent node
    def get_UCB(self, Wi, Si, Sp, c=1.414):
        if Si==0:
            return 10000.0
        if Sp==0:
            return 1.0
        
        return 1.0*Wi/Si + c*math.sqrt(math.log(1.0*Sp)/Si)
    
    
    # selection for color
    def selection(self, color, tree_node, c=1.414, depth=0):
        # choose the one with max UCB
        max_UCB, target_action = 0.0, None
        action_list = self.get_all_possible_actions(color)
        for action in action_list:
            if str(action) in tree_node:
                (Wi, Si) = tree_node[str(action)]['info']
            else:
                Wi, Si = 0, 0
            Sp = tree_node['info'][1]
            UCB = self.get_UCB(Wi, Si, Sp, c)
            #if depth==0:
            #    print(color, action, Wi, Si, Sp, c, UCB)
            if max_UCB <= UCB:
                max_UCB, target_action = UCB, action
                
        
        # it's not a leaf node 
        if str(target_action) in tree_node:
            # make action along the path
            self.board.apply_action( target_action )
            # go down
            winner = self.selection(color.opponent, tree_node[str(target_action)], c, depth+1)
            self.board.undo_action()
        else:
            # new node
            tree_node[str(target_action)] = {'info': (0,0)}
            self.board.apply_action( target_action )
            # simulate the game
            winner = self.simulation( color )
            self.board.undo_action()
        
        # update the win and total number
        wt = tree_node[str(target_action)]['info']
        wt = (wt[0], wt[1]+1)
        if winner==color:
            wt = (wt[0]+1, wt[1])
        tree_node[str(target_action)]['info'] = wt
        
        return winner

    
    def action(self, **referee: dict) -> Action:
        """
        Return the next action to take.
        """
        start_time = time.time()
        
        # win number, total number
        root = {'info': (0,0) }
        # MCTS
        while True:
            # time out
            if time.time()-start_time>1.0:
                break
            
            winner = self.selection(self._color, root, 1.414)
            # update the win and total number
            if winner==self._color:
                root['info'] = (root['info'][0]+1, root['info'][1]+1)
            else:
                root['info'] = (root['info'][0], root['info'][1]+1)
        
        
        # choose the action with the max win_rate
        best_action, win_rate, wt = None, 0.0, None
        action_list = self.get_all_possible_actions(self._color)
        for action in action_list:
            if str(action) in root:
                (win, total) = root[str(action)]['info']
            else:
                win, total = 0, 1
            
            if win_rate <= 1.0*win/total:
                best_action, win_rate, wt = action, 1.0*win/total, (win,total)
        
        #print(best_action, win_rate, wt, root["info"])
        #return None
        return best_action


    def turn(self, color: PlayerColor, action: Action, **referee: dict):
        """
        Update the agent with the last player's action.
        """
        self.board.apply_action( action )
        