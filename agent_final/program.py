# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part B: Game Playing Agent
import sys
 
# setting path
sys.path.append('../project b')
from referee.game import PlayerColor, Action, SpawnAction, SpreadAction, HexPos, HexDir, Board

import time
import math
from random import randint


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
        
    
    def get_all_possible_actions(self, color):
        action_list = []
        for i in range(self.N):
            for j in range(self.N):
                action = SpawnAction(HexPos(i, j))
                cell = action.cell
                
                if self.board._total_power < self.N*self.N:
                    if not self.board._cell_occupied(cell):
                        action_list.append(action)
                
                if self.board[cell].player != color:
                    continue
                    
                for dir in [HexDir.DownRight, HexDir.Down, HexDir.DownLeft, \
                    HexDir.UpLeft, HexDir.Up, HexDir.UpRight]:
                    
                    action = SpreadAction(HexPos(i, j), dir)
                    action_list.append(action)
        
        return action_list
        
    
    def simulation(self, cur_color, MaxStep=10):
        step, winner = 0, None
        while not self.board.game_over and step<MaxStep:
            cur_color = cur_color.opponent
            action_list = self.get_all_possible_actions(cur_color)
            
            index = randint(0, len(action_list)-1)
            action = action_list[index]
            self.board.apply_action(action)
            step += 1
        
        if self.board.game_over:
            winner = self.board.winner_color
        else:
            red = self.board._color_power(PlayerColor.RED)
            blue = self.board._color_power(PlayerColor.BLUE)
            if red >= blue+2:
                winner = PlayerColor.RED
            elif blue >= red+2:
                winner = PlayerColor.BLUE
            else:
                winner = None

        for i in range(step):
            self.board.undo_action()
        
        return winner

    
    def get_UCB(self, Wi, Si, Sp, c=1.414):
        if Si==0:
            return 10000.0
        if Sp==0:
            return 1.0
        
        return 1.0*Wi/Si + c*math.sqrt(math.log(1.0*Sp)/Si)
    
    
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
            if max_UCB <= UCB:
                max_UCB, target_action = UCB, action
                
        
        # it's not a leaf node 
        if str(target_action) in tree_node:
            # make along the path
            self.board.apply_action( target_action )
            winner = self.selection(color.opponent, tree_node[str(target_action)], c, depth+1)
            self.board.undo_action()
        else:
            tree_node[str(target_action)] = {'info': (0,0)}
            self.board.apply_action( target_action )
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
        while True:
            # time out
            if time.time()-start_time>1.0:
                break
            
            winner = self.selection(self._color, root, 1.414)
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
            
        """
        match self._color:
            case PlayerColor.RED:
                return SpawnAction(HexPos(3, 3))
            case PlayerColor.BLUE:
                # This is going to be invalid... BLUE never spawned!
                return SpreadAction(HexPos(3, 3), HexDir.Up)
        """

    def turn(self, color: PlayerColor, action: Action, **referee: dict):
        """
        Update the agent with the last player's action.
        """
        self.board.apply_action( action )
        
        """
        match action:
            case SpawnAction(cell):
                print(f"Testing: {color} SPAWN at {cell}")
                pass
            case SpreadAction(cell, direction):
                print(f"Testing: {color} SPREAD from {cell}, {direction}")
                pass
        """
