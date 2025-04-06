"""
Tic-Tac-Toe: using Minimax algorithm

@brief AI educational project
@author Emilio Garzia, 2025
"""

import copy
import random

class TicTacToe:
    def __init__(self):
        self.player1_symbol = "X"
        self.player2_symbol = "O"
        self.field_state = [
                [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL],
                [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL],
                [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL]]
        self.moves = 0
        self.elapsed_time = None
        
    """
    Determines who is next player
    """
    def player(self):
        current_player = None
        if(self.moves%2==0):
            current_player = self.PLAYER1
        else:
            current_player = self.PLAYER2
        return current_player

    """
    Check all possible legal move   
    Field's mapping
        0,0|0,1|0,2
        1,0|1,1|1,2
        2,0|2,1|2,2
    """
    def actions(self):
        i=j=0
        available_actions = []
        for cells in self.field_state:
            j=0
            for cell in cells:
                if(cell == self.EMPTY_CELL):
                    available_actions.append([i,j])
                j+=1
            i += 1
        return available_actions

    """
    Check the state of the game after a move
    """
    def result(self, action):
        if(action in self.actions()):
            self.field_state[action[0]][action[1]] = self.player()
            self.moves += 1
        else:
            print("The choosed move is illegal, or you tries to fill a non empty cell!")

    """
    Version of result() method which not change the state of the field,
    but just simulate a taken action
    """
    def result_simulated(self, action):
        new_game = copy.deepcopy(self)
        if action in new_game.actions():
            new_game.field_state[action[0]][action[1]] = new_game.player()
            new_game.moves += 1
            return new_game
        else:
            return None

    """
    Mimimax algorithm
    """
    def minimax(self, smart_level=302):
        if self.terminal()[0]:
            return None  # trivial case

        def max_value(state):
            if state.terminal()[0]:
                return state.utility(), None
            action_scores = []
            for action in state.actions():
                new_state = state.result_simulated(action)
                score, _ = min_value(new_state)
                action_scores.append((score, action))
            action_scores.sort(reverse=True)
            return action_scores[0][0], self.__top_n_actions__(action_scores, smart_level)

        def min_value(state):
            if state.terminal()[0]:
                return state.utility(), None #trivial case
            action_scores = []
            for action in state.actions():
                new_state = state.result_simulated(action)
                score, _ = max_value(new_state)
                action_scores.append((score, action))
            action_scores.sort()
            return action_scores[0][0], self.__top_n_actions__(action_scores, smart_level)

        current_player = self.player()
        if current_player == self.PLAYER1:
            _, action = max_value(self)
        else:
            _, action = min_value(self)
        return action

    def __top_n_actions__(self, actions, smart_level):
        if smart_level == self.HIGH:
            top_n = 1  # optimal choice
        elif smart_level == self.MEDIUM:
            top_n = 10
        elif smart_level == self.LOW:
            top_n = 30
        else:
            top_n = 1
        
        top_n_actions = actions[:top_n]
        return random.choice(top_n_actions)[1]
        

    """
    Check if the game has ended after a move
    """
    def terminal(self):
        tmp = []
        stop_coordinates = []
        tmp_stop_coords = []

        main_diag = []
        sec_diag = []

        # Check diagonals
        for i in range(3):
            main_diag.append(self.field_state[i][i])
            stop_coordinates.append([i,i])
            sec_diag.append(self.field_state[i][2 - i])
            tmp_stop_coords.append([i,2-i])

        # Check main diagonal
        if main_diag[0] != self.EMPTY_CELL and self.__checkMonovaluesArray__(main_diag):
            return True, self.MAIN_DIAG_WIN, stop_coordinates

        # Check second diagonal
        if sec_diag[0] != self.EMPTY_CELL and self.__checkMonovaluesArray__(sec_diag):
            return True, self.SECOND_DIAG_WIN, tmp_stop_coords
        
        # erase all support data structures for diag
        del tmp_stop_coords, main_diag, sec_diag

        # Check vertical win
        for col in range(3):
            tmp = []
            stop_coordinates = []
            for row in range(3):
                tmp.append(self.field_state[row][col])
                stop_coordinates.append([row, col])
            if tmp[0] != self.EMPTY_CELL and self.__checkMonovaluesArray__(tmp):
                return True, self.VERTICAL_WIN, stop_coordinates

                
        # Check horizontal win
        for row in range(3):
            tmp = []
            stop_coordinates = []
            for col in range(3):
                tmp.append(self.field_state[row][col])
                stop_coordinates.append([row, col])
            if tmp[0] != self.EMPTY_CELL and self.__checkMonovaluesArray__(tmp):
                return True, self.HORIZONTAL_WIN, stop_coordinates

        # Check draw
        if(self.moves == 9): return True, self.DRAW, None

        return False, None, None

    """
    Determines the result of the game (-1|0|1)
    """
    def utility(self):
        result, win_kind, winner_coords = self.terminal()
        
        if(not result): return False

        if(win_kind == self.DRAW):
            return self.DRAW
        else:
            if(self.field_state[winner_coords[0][0]][winner_coords[0][1]] == self.PLAYER1):
                return self.PLAYER1
            elif(self.field_state[winner_coords[0][0]][winner_coords[0][1]] == self.PLAYER2):
                return self.PLAYER2

    """
    Print game's field
    """
    def print_field(self):
        i = 0
        for cells in self.field_state:
            for cell in cells:
                if(cell == self.EMPTY_CELL): 
                    print("-", end=" ")
                elif(cell == self.PLAYER1):
                    print(self.player1_symbol, end=" ")
                elif(cell == self.PLAYER2):
                    print(self.player2_symbol, end=" ")
                i += 1
                if(i%3==0): print()

    """
    Restart the game
    """
    def restart(self):
        self.field_state = [
                [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL],
                [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL],
                [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL]]
        self.moves = 0
        self.elapsed_time = None

    """
    Set symbol for a specific player
    """ 
    def set_player_symbol(self, player_number:int, symbol:str):
        if not isinstance(player_number, int):
            raise TypeError("player_number attribute must be an integer equal to 1 or 2")
        if not isinstance(symbol, str):
            raise TypeError("symbol attribute must be a string with lenght equal to 1")
        
        if(len(symbol)==1):
            if(player_number == 1):
                self.player1_symbol = symbol
            elif(player_number == 2):
                self.player2_symbol = symbol
        else:
            print("The lenght of the symbol must be 1")

    """
    Simulation of a match where the opponents are CPUs
    """
    def cpu_vs_cpu_AI_simulation(self, smart_level=302, print_moves=False, algorithm=200):
        if algorithm == self.MINIMAX:
            while not self.terminal()[0]:
                action = self.minimax(smart_level=smart_level)
                self.result(action=action)
                if print_moves:
                    print(f"----- Move: #{self.moves} -----")
                    self.print_field()
        if algorithm == self.ALPHA_BETA_PRUNING:
            pass
                
    """
    Print stats about played game, 
    """
    def print_insights(self, stop_term=True, winner_coords=True, elapsed_time=True):
        end_state, end_term, coords = self.terminal()
        if end_state:
            if stop_term:
                if end_term == self.DRAW:
                    print("Match result: DRAW")
                elif end_term == self.HORIZONTAL_WIN:
                    print("Math result: HORIZONTAL WIN")
                elif end_term == self.VERTICAL_WIN:
                    print("Math result: VERTICAL WIN")
                elif end_term == self.MAIN_DIAG_WIN:
                    print("Math result: MAIN DIAGONAL WIN")
                elif end_term == self.SECOND_DIAG_WIN:
                    print("Math result: SECOND DIAGONAL WIN")
                print(f"Done moves: {self.moves}")

            if winner_coords:
                if end_term != self.DRAW:
                    if self.field_state[coords[0][0]][coords[0][1]] == self.PLAYER1:
                        print(f"The winner is: {self.PLAYER1}")
                    else:
                        print(f"The winner is: {self.PLAYER2}")
                    print(f'Winner coordinates: {coords}')
            
            if elapsed_time and self.elapsed_time is not None:
                print(f"Game duration: {self.elapsed_time}ms")
        else:
            print("Tha game hasn't ended, invoke this method when the game has ended!")


    """
    @Support method
    Check if the elements of a vector are all equals, 
        and if the lenght is equal to 3
    """
    @staticmethod
    def __checkMonovaluesArray__(vector, verbose=False):
        if len(vector) != 3:
            if verbose:
                print("__checkMonovaluesArray__() error: lunghezza non valida!")
            return False
        first_value = vector[0]
        for element in vector:
            if element != first_value:
                return False
        return True

    # Eenumerators for players
    @property 
    def PLAYER1(self): return 1
    @property 
    def PLAYER2(self): return -1
    @property
    def EMPTY_CELL(self): return 100
    # Enumerators for game results
    @property
    def DRAW(self): return 0
    @property
    def VERTICAL_WIN(self): return 101
    @property
    def HORIZONTAL_WIN(self): return 102
    @property
    def MAIN_DIAG_WIN(self): return 103
    @property
    def SECOND_DIAG_WIN(self): return 104
    # Enumarators for AI Algorithm
    @property
    def MINIMAX(self): return 200
    @property
    def ALPHA_BETA_PRUNING(self): return 201
    # Enumerators for AI uncertainty
    @property
    def LOW(self): return 300
    @property
    def MEDIUM(self): return 301
    @property
    def HIGH(self): return 302
