import time
import random


class Game:

    def __init__(self, row, col):
        self.rows = row
        self.cols = col
        self.cells = self.init_board()

    def init_board(self, start_alive=0.2):

        cells = list()
        for row in range(self.rows):
            cells.append([])
            for col in range(self.cols):
                possibility_of_alive = random.random()
                alive = possibility_of_alive <= start_alive
                cells[row].append(alive)

        return cells

    def update_board(self):
        new_board = list()

        for row in range(self.rows):
            new_board.append([])
            for col in range(self.cols):
                is_alive = self.cells[row][col]
                number_of_neighbors = self.how_many_neighbors_are_alive(row, col)

                if is_alive:
                    if 2 > number_of_neighbors or number_of_neighbors > 3:
                        is_alive = False
                else:
                    if number_of_neighbors == 3:
                        is_alive = True

                new_board[row].append(is_alive)

        self.cells = new_board

    def how_many_neighbors_are_alive(self, cellx, celly):
        alive_count = 0

        for row in range(cellx - 1, cellx + 2):
            if 0 < row < self.rows:
                for col in range(celly - 1, celly + 2):
                    if 0 < col < self.cols:
                        alive_count += self.cells[row][col]

        # removing the center cell
        alive_count -= self.cells[cellx][celly]

        return alive_count

    def print_board(self):
        print('    ' * len(self.cells[0]) + " ")
        for row in self.cells:
            repr = ["  {} ".format('o' if col is True else ' ') for col in row]
            repr.append(" ")
            print(''.join(repr))
            print('    '*len(row) + " ")


if __name__ == "__main__":
    game = Game(10, 25)
    for tick in range(150):
        game.update_board()
        time.sleep(0.1)
        print("\n"*25)
        game.print_board()
