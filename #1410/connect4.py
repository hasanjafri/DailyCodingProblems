class Connect4:
    def __init__(self):
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1

    def print_grid(self):
        for row in self.grid:
            print(row)

    def drop_disc(self, column):
        if column < 0 or column > 6:
            raise ValueError("Column must be between 0 and 6.")
        for row in range(5, -1, -1):
            if self.grid[row][column] == 0:
                self.grid[row][column] = self.current_player
                return
        raise ValueError("This column is full")

    def switch_player(self):
        self.current_player = 1 if self.current_player == 2 else 2

    def check_win(self):
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if (
                    self.grid[row][col] == self.current_player
                    and self.grid[row][col + 1] == self.current_player
                    and self.grid[row][col + 2] == self.current_player
                    and self.grid[row][col + 3] == self.current_player
                ):
                    return True

        # Check vertical
        for row in range(3):
            for col in range(7):
                if (
                    self.grid[row][col] == self.current_player
                    and self.grid[row + 1][col] == self.current_player
                    and self.grid[row + 2][col] == self.current_player
                    and self.grid[row + 3][col] == self.current_player
                ):
                    return True

        # Check diagonal (top left to bottom right)
        for row in range(3):
            for col in range(4):
                if (
                    self.grid[row][col] == self.current_player
                    and self.grid[row + 1][col + 1] == self.current_player
                    and self.grid[row + 2][col + 2] == self.current_player
                    and self.grid[row + 3][col + 3] == self.current_player
                ):
                    return True

        # Check diagonal (bottom left to top right)
        for row in range(3, 6):
            for col in range(4):
                if (
                    self.grid[row][col] == self.current_player
                    and self.grid[row - 1][col + 1] == self.current_player
                    and self.grid[row - 2][col + 2] == self.current_player
                    and self.grid[row - 3][col + 3] == self.current_player
                ):
                    return True

        return False

    def play(self):
        while True:
            self.print_grid()
            print(f"Player {self.current_player}'s turn.")
            valid_input = False
            while not valid_input:
                try:
                    column = int(input("Enter column to drop the disc: "))
                    self.drop_disc(column)
                    valid_input = True
                except ValueError as e:
                    print(e)

            if self.check_win():
                self.print_grid()
                print(f"Player {self.current_player} wins!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = Connect4()
    game.play()
