from tic_tac_toe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()
    
    # Start CPU vs CPU game simulation
    game.cpu_vs_cpu_AI_simulation(print_moves=True, algorithm=game.MINIMAX, smart_level=game.MEDIUM)

    # Print mapping of the board
    game.print_mapping()

    # Start Player vs CPU game
    #game.player_vs_cpu(smart_level=game.MEDIUM, player1=True)

    # Player vs Player game
    """
    game.set_player_symbol(1,"E")
    game.set_player_symbol(2,"B")
    game.player_vs_player()
    """

    # Print stats about played game
    game.print_insights()
    
    
