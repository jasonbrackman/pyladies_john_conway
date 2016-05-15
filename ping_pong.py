import game_of_life
import unittest
import random


class testCellFuture(unittest.TestCase):

    def mock_up_board(self):

        # for tests to be repeatable we need to stop a random distribution each time.
        random.seed(1234)
        game = game_of_life.Game(5, 6)
        return game

    def test__is_cell_neighbors_fewer_than_two(self, cellx=1, celly=1):
        """Any live cell with fewer than two live neighbours dies, as if caused by under-population"""

        game = self.mock_up_board()
        alive = game.how_many_neighbors_are_alive(cellx, celly)
        self.assertLess(alive, 2, "Your Alive neighbors is not less than two: {}".format(alive))

    def test__is_neighbors_two_or_three(self, cellx=3, celly=3):
        game = self.mock_up_board()
        alive = game.how_many_neighbors_are_alive(cellx, celly)
        self.assertTrue(alive == 2 or alive == 3)

    def test__is_cell_going_to_die(self, cellx=3, celly=4):
        game = self.mock_up_board()
        alive = game.how_many_neighbors_are_alive(cellx, celly)
        self.assertTrue(alive == 4)

if __name__ == "__main__":
    unittest.main()