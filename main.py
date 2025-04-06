from tic_tac_toe import TicTacToe
from argparse import ArgumentParser
import debug_simulations as sim

if __name__ == "__main__":
    game = TicTacToe()
    
    # Start CPU vs CPU game simulation
    game.cpu_vs_cpu_AI_simulation(print_moves=True, algorithm=game.MINIMAX, smart_level=game.LOW)
    
    # Print stats about played game
    game.print_insights()
    
    
