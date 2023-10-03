class TicTacToe:
    def __init__(self) -> None:
        self.board = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
        self.player_input = None
        self.position = None

    def is_winner(self, winning_combination_arr):
        # below is recursion logic

        # if not winning_combination:
        #     return False

        # if (
        #     self.board[winning_combination[0][0][0]][winning_combination[0][0][1]]
        #     and self.board[winning_combination[0][1][0]][winning_combination[0][1][1]]
        #     and self.board[winning_combination[0][2][0]][winning_combination[0][2][1]]
        #     == user_input
        # ):
        #     print("condition met")
        #     return True

        # return self.is_winner(
        #     winning_combination[1:], winning_combination[:1], user_input
        # )

        for winning_combination in winning_combination_arr:
            if (
                self.board[winning_combination[0][0]][winning_combination[0][1]]
                == self.board[winning_combination[1][0]][winning_combination[1][1]]
                == self.board[winning_combination[2][0]][winning_combination[2][1]]
                == self.player_input
            ):
                return True
        return False

    def check_if_draw(self):
        pass
        #check if none of the array contain 1 then its draw
        check=any('1' in arr for arr in self.board)
        if not check:
            return True
        
    def validate_move(self):
        if (
            isinstance(self.position, tuple)
            and len(self.position) <= 2
            and isinstance(self.position[0], int)
            and isinstance(self.position[1], int)
            and self.position[0] <= 2
            and self.position[1] <= 2
        ):
            return True
        else:
            raise ValueError  # TODO change this

    # def validate_input(self): #TODO temporary commenting this, User input will be fixed automatically based on current player 1 or 2
    #     if self.player_input == "X":
    #         self.current_player = self.player_1

    #     elif self.player_input == "0":
    #         self.current_player = self.player_2
    #     else:
    #         raise ValueError  # TODO change this
    #     return True

    def winning_combinations(self):
        # check if same value is there in any of below

        winning_combination = [
            [(0, 0), (0, 1), (0, 2)],  # top row
            [(1, 0), (1, 1), (1, 2)],  # second row
            [(2, 0), (2, 1), (2, 2)],  # third row
            [(0, 0), (1, 0), (2, 0)],  # first column
            [(0, 1), (1, 1), (2, 1)],  # second column
            [(0, 2), (1, 2), (2, 2)],  # third column
            [(0, 0), (1, 1), (2, 2)],  # top left - bottom right diagonal
            [(0, 2), (1, 1), (2, 0)],  # top right -bottom left diagonal
        ]
        return self.is_winner(winning_combination)
        

        # TODO check for draw condition as well

    def print_board(self):
        for i in self.board:
            print("\t".join(map(str, i)))

    def accept_input(self, user_input, player_input):
        # input_valid = self.validate_input(position)
        # if input_valid:
        # check if move is valid

        self.position = user_input
        self.player_input = player_input

        move_valid = self.validate_move()

        if move_valid:
            row = self.position[0]
            column = self.position[1]
            # modify board with current player input
            if not self.board[row][column]=='1':
                return "Cannot write to exiting position"    
            self.board[row][column] = self.player_input
            
            print("--------------")

            self.print_board()
            if_winner = self.winning_combinations()
            if_draw = self.check_if_draw()
            if if_winner:
                print("inside if_winner")
                return True
            if if_draw:
                return "Match Draw"

        return False


try:
    n = 0
    obj = TicTacToe()
    while True:
        if n % 2 == 0:
            current_player = "Player_1"
            current_player_input = "X"
        else:
            current_player = "Player_2"
            current_player_input = "0"
        print(
            "-------------------------------------------------------------------------------"
        )
        print(f"--{current_player} ---Your Turn --")
        print(f"Your input is {current_player_input}")
        user_input = input("Enter your Position in 1,2 format : - ")
        print(
            "-------------------------------------------------------------------------------"
        )

        user_input = tuple(
            int(x) for x in user_input.split(",")
        )  # to convert user input 1,2 to tuple
        n += 1
        result = obj.accept_input(user_input, current_player_input)
        # obj.print_board()
        if result:
            print(result)
            print("You Win")
            break
            # TODO print which player has won

except KeyboardInterrupt:
    pass
