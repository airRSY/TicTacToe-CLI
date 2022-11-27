# --- MODULES ---
from copy import deepcopy

# --- MAIN CLASS ---
class CliClass():
    def __init__(self, gameclass_) -> None:
        self.game_class = gameclass_
        
        self.display_cli()
    
    # -- PUBLIC METHODS --
    def display_cli(self) -> None:
        self.separate_from_old_board()
        
        self.create_lines()
        self.display_upper_tab()
        self.create_lines()
        
        self.display_board()
        
        self.create_lines()
        self.display_bottom_tab()
        self.create_lines()
    
    def get_input(self) -> None:
        current_player = self.game_class.current_player
        
        print("[Pemain ", end="")
        if (current_player == 1):
            print("X", end="")
        else:
            print("O", end="")
        print("] ", end="")
        
        self.game_class.user_input = int(input(">> "))
    
    # -- PRIVATE METHODS --
    def separate_from_old_board(self) -> None:
        print("\n" * 40)
    
    def create_lines(self) -> None:
        # print("=-=-" * 20 + "=")
        print("=-=-"*10 + "|" + "-=-="*10)
    
    def new_line(self) -> None:
        print()
    
    def display_upper_tab(self) -> None:
        game_class = self.game_class
        wins = game_class.wins
        is_game_running = game_class.is_game_running
        current_player = game_class.current_player
        
        print("\t       Pemain X: {} Kemenangan   |   Pemain O: {} Kemenangan".format(wins[0], wins[1]))
        self.new_line()
        
        if (is_game_running):
            print(" "*36 + "Giliran ", end="")
            if (current_player == 1):
                print("X")
            else:
                print("O")
        else:
            print(" "*31 + "Permainan Berakhir")
    
    def display_bottom_tab(self) -> None:
        print("[KONSOL] >> ", end="")
        self.print_information()
    
    def format_board(self) -> list:
        board = deepcopy(self.game_class.board)
        
        for rowIdx, rowVal in enumerate(board):
            for columnIdx, columnVal in enumerate(rowVal):
                if (columnVal == 0):
                    board[rowIdx][columnIdx] = "_"
                if (columnVal == 1):
                    board[rowIdx][columnIdx] = "X"
                if (columnVal == 2):
                    board[rowIdx][columnIdx] = "O"
        
        return board
    
    def display_board(self) -> None:
        board = self.format_board()
        
        self.new_line()
        print(" "*12 + "     |     |     ", end="")
        print(" "*23 + "     |     |     ")
        
        print(" "*12 + "  {}  |  {}  |  {}  ".format(board[0][0], board[0][1], board[0][2]), end="")
        print(" "*23 + "  1  |  2  |  3  ")
        
        print(" "*12 + "_____|_____|_____", end="")
        print(" "*23 + "_____|_____|_____")
        
        print(" "*12 + "     |     |     ", end="")
        print(" "*23 + "     |     |     ")
        
        print(" "*12 + "  {}  |  {}  |  {}  ".format(board[1][0], board[1][1], board[1][2]), end="")
        print(" "*23 + "  4  |  5  |  6  ")
        
        print(" "*12 + "_____|_____|_____", end="")
        print(" "*23 + "_____|_____|_____")
        
        print(" "*12 + "     |     |     ", end="")
        print(" "*23 + "     |     |     ")
        
        print(" "*12 + "  {}  |  {}  |  {}  ".format(board[2][0], board[2][1], board[2][2]), end="")
        print(" "*23 + "  7  |  8  |  9  ")
        
        print(" "*12 + "     |     |     ", end="")
        print(" "*23 + "     |     |     ")
        self.new_line()
    
    def print_information(self) -> None:
        information_code = self.game_class.information_code
        
        if (information_code == 0):
            print("Permainan sedang berlangsung!")
        elif (information_code == 1):
            print("Pemain X telah memenangkan permainan!")
        elif (information_code == 2):
            print("Pemain O telah memenangkan permainan!")
        elif (information_code == 3):
            print("Permainan berakhir dengan seri!")