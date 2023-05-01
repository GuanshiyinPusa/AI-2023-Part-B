# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part B: Game Playing Agent

from referee.game import \
    PlayerColor, Action, SpawnAction, SpreadAction, HexPos, HexDir, \
    Board

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
        
    
    def get_all_possible_actions(self, color):
        action_list = []
        for i in range(self.N):
            for j in range(self.N):
                if self.board._total_power < self.N*self.N:
                    action = SpawnAction(HexPos(i, j))
                    cell = action.cell
                    if not self.board._cell_occupied(cell):
                        action_list.append(action)
                
                for dir in [HexDir.DownRight, HexDir.Down, HexDir.DownLeft, \
                    HexDir.UpLeft, HexDir.Up, HexDir.UpRight]:
                    
                    action = SpreadAction(HexPos(i, j), dir)
                    cell = action.cell
                    if self.board[cell].player == color:
                        action_list.append(action)
        
        return action_list

    
    def action(self, **referee: dict) -> Action:
        """
        Return the next action to take.
        """
        action_list = self.get_all_possible_actions(self._color)

        return action_list[randint(0, len(action_list)-1)]

            
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
