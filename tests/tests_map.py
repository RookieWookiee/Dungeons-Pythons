# TODO: Delete Hero once implemented
from src.map import Map
from src.empty_cell import EmptyCell
from src.gateway import Gateway
from src.spawn import Spawn
from src.treasure import Treasure
from src.wall import Wall
from src.hero import Hero


import unittest


class MapTests(unittest.TestCase):
    def setUp(self):
        self.input = ['S.##',
                      '#T##',
                      '#..G']
        self.test_map = Map(self.input)
        self.num_rows = len(self.input)
        self.num_cols = len(self.input[0])

    def test_init(self):
        test_map = self.test_map
        num_rows, num_cols = self.num_rows, self.num_cols
        test_spawns = list(test_map.spawnpoints)

        with self.subTest('types of the cells should be correct'):
            expected = [[Spawn, EmptyCell, Wall, Wall],
                        [Wall, EmptyCell, Wall, Wall],
                        [Wall, EmptyCell, EmptyCell, Gateway]]

            actual = [[type(x) for x in row] for row in test_map.grid]

            for row, exp_row, act_row in zip(range(num_rows), expected, actual):
                for col, exp_col, act_col in zip(range(num_cols), exp_row, act_row):
                    self.assertEqual(act_col, exp_col,
                                     msg=f'At position (row: {row}, col: {col})')

        with self.subTest('Treasure should be at (1, 1)'):
            self.assertIsInstance(test_map.grid[1][1].occupant, Treasure)

        with self.subTest('coordinates of cells should be correct'):
            for row, line in zip(range(num_rows), test_map.grid):
                for col, cell in zip(range(num_cols), line):
                    self.assertEqual((row, col), (cell.row, cell.col))

        with self.subTest('len(spawnpoints) should be 1'):
            self.assertEqual(len(test_spawns), 1)

        with self.subTest('coordinates of spawn should be (0, 0)'):
            spawn = test_spawns[0]
            self.assertEqual((spawn.row, spawn.col), (0, 0))

    def test_spawn_coords_of_hero_should_be_correct(self):
        hero = Hero(name='test',
                 title='Mighty Tester',
                 health=100,
                 mana=100,
                 mana_regeneration_rate=2)
        test_map = self.test_map

        with self.subTest('hero coordinates should be (0, 0)'):
            self.assertEqual((hero.row, hero.col), (None, None))
            test_map.spawn(hero)
            self.assertEqual((hero.row, hero.col), (0, 0))

    def test_spawn_cell_should_become_empty_cell_after_spawn(self):
        hero = Hero(name='test',
                 title='Mighty Tester',
                 health=100,
                 mana=100,
                 mana_regeneration_rate=2)
        
        self.assertIsInstance(self.test_map.grid[0][0], Spawn)
        self.test_map.spawn(hero)
        self.assertIsInstance(self.test_map.grid[0][0], EmptyCell)

    def test_spawn_method_should_return_false_at_second_spawn(self):
        hero = Hero(name='test',
                 title='Mighty Tester',
                 health=100,
                 mana=100,
                 mana_regeneration_rate=2)
        
        self.assertTrue(self.test_map.spawn(hero))
        self.assertFalse(self.test_map.spawn(hero))

    def test_spawn_method_should_not_change_hero_coords_at_second_spawn(self):
        hero = Hero(name='test',
                 title='Mighty Tester',
                 health=100,
                 mana=100,
                 mana_regeneration_rate=2)

        self.test_map.spawn(hero)
        self.assertEqual((hero.row, hero.col), (0, 0))
        self.test_map.spawn(hero)
        self.assertEqual((hero.row, hero.col), (0, 0))

    def test_spawn_method_should_raise_type_error_if_arg_is_not_hero(self):
        hero = {'name': 'test', 'title': 'Less Mighty Tester'}

        with self.assertRaises(TypeError):
            self.test_map(hero)
