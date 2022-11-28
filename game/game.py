# --- MAIN CLASS ---
class GameClass:
    def __init__(self) -> None:
        self.cli_class = None
        self.user_input = -1
        self.current_player = 1
        self.is_game_running = True
        self.marked_columns = 0
        self.wins = [0, 0]
        self.information_code = 0
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    
    # -- PUBLIC METHODS --
    def get_input_send_request(self) -> bool:
        """ Getting input and verifying it. If it's an valid input, then mark a column on the board.

        When called, and the game is currently running. Then get an input from user by calling **CliClass.get_input()**
        And if it's an valid input, it's going to format the input so that it's compatible to an 2 dimension list.
        It passes the formatted input to **GameClass.verify_mark_columns()** arguments.

        :return: Is the input from the user valid
        """

        if self.is_game_running:
            self.cli_class.get_input()
            if self.verify_input():
                row, column = self.format_input()
                self.verify_mark_columns(row, column, self.current_player)
                return True
            return False
    
    def set_cli_class(self, cliclass_) -> None: 
        self.cli_class = cliclass_
    
    def set_game_state(self) -> None:
        state = self.get_board_state()
        self.information_code = state
        if state != 0:
            self.is_game_running = False
            self.cli_class.display_cli()
            if state == 1:
                self.wins[0] += 1
            elif state == 2:
                self.wins[1] += 1

    def reset(self) -> None:
        self.user_input = -1
        self.current_player = 1
        self.is_game_running = True
        self.information_code = 0
        self.marked_columns = 0
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    
    # -- PRIVATE METHODS --
    def verify_mark_columns(self, row, column, player_code) -> None:
        if self.board[row][column] == 0 and player_code != 0:
            self.mark_column(row, column, player_code)
            self.next_turn()
    
    def get_board_state(self) -> int:
        # Horizontal
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                return self.board[row][1]
        
        # Vertical
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != 0:
                return self.board[1][column]
        
        # Diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[1][1]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[1][1]
        
        # Draw
        if self.is_board_full():
            return 3
        
        # Playing
        return 0
    
    def next_turn(self) -> None:
        self.current_player = self.current_player % 2 + 1
        self.information_code = 0
    
    def is_board_full(self) -> bool:
        return self.marked_columns >= 9

    def format_input(self):
        input_ = self.user_input
        
        if input_ == 1:
            return 0, 0
        if input_ == 2:
            return 0, 1
        if input_ == 3:
            return 0, 2
        if input_ == 4:
            return 1, 0
        if input_ == 5:
            return 1, 1
        if input_ == 6:
            return 1, 2
        if input_ == 7:
            return 2, 0
        if input_ == 8:
            return 2, 1
        if input_ == 9:
            return 2, 2
        return -1, -1
        
    def verify_input(self) -> bool:
        if self.user_input < 1 or self.user_input > 9:
            return False
        return True
    
    def mark_column(self, row, column, player_code) -> None:
        self.board[row][column] = player_code
        self.marked_columns += 1
