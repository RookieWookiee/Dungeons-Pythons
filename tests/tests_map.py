from src.map import Map
from src.empty_cell import EmptyCell
from src.gateway import Gateway
from src.spawn import Spawn
from src.treasure import Treasure
from src.wall import Wall

import unittest


# TODO:
# add test for whether or not the spawn cell is changed
# to empty cell after invoking spawn()
class MapTests(unittest.TestCase):
    def test_init_no_enemies(self):
        input = ['S.##',
                 '#T##',
                 '#..G']
        test_map = Map(input)
        num_rows, num_cols = len(input), len(input[0])  # 3, 4
        test_spawns = list(test_map.spawnpoints)

        with self.subTest('types of the cells should be correct'):
            expected = [[Spawn, EmptyCell, Wall, Wall],
                        [Wall, Treasure, Wall, Wall],
                        [Wall, EmptyCell, EmptyCell, Gateway]]

            actual = [[type(x) for x in row] for row in test_map.grid]

            for row, exp_row, act_row in zip(range(num_rows), expected, actual):
                for col, exp_col, act_col in zip(range(num_cols), exp_row, act_row):
                    self.assertEqual(act_col, exp_col,
                            msg=f'At position (row: {row}, col: {col})')

        with self.subTest('coordinates of cells should be correct'):
            for row, line in zip(range(num_rows), test_map.grid):
                for col, cell in zip(range(num_cols), line):
                    self.assertEqual((row, col), (cell.row, cell.col))

        with self.subTest('len(spawnpoints) should be 1'):
            self.assertEqual(len(test_spawns), 1)

        with self.subTest('coordinates of spawn should be (0, 0)'):
            spawn = test_spawns[0]
            self.assertEqual((spawn.row, spawn.col), (0, 0))
