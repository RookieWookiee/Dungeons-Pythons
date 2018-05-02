from src.map import Map

import unittest
from unittest.mock import patch, Mock


class MapInitAndSpawnTests(unittest.TestCase):
    def setUp(self):
        class_dependencies = [
                'Hero', 'Treasure', 'Spawn', 'Gateway', 'Wall', 'Enemy', 'EmptyCell']
        symbols = ['H', 'T', 'S', 'G', '#', 'E', '.']
        patchers = [patch(f'src.map.{cls_name}') for cls_name in class_dependencies]

        for p, cls_name, sym in zip(patchers, class_dependencies, symbols):
            setattr(self, f'{cls_name}Mock', p.start())
            setattr(getattr(self, f'{cls_name}Mock'), 'sym', sym)

        self.addCleanup(patch.stopall)

    def test_init_cell_instance_correctess(self):
        # black magic
        input = ['S.#' ,'GET']

        expected = [
                [self.SpawnMock, self.EmptyCellMock, self.WallMock],
                [self.GatewayMock, self.EmptyCellMock, self.EmptyCellMock]]

        map = Map(input)
        actual = [[type(x) for x in row] for row in map.grid]

        for row, mocks in zip(range(2), expected):
            for col, ctor_mock in zip(range(3), mocks):
                all_kwargs = [kwargs for args, kwargs in ctor_mock.call_args_list]
                self.assertIn({'row': row, 'col': col}, all_kwargs)

    def test_init_enemy_is_instantiated(self):
        Map(['E'])
        enemy = self.EnemyMock.return_value
        self.EnemyMock.assert_called_once()
        self.EmptyCellMock.return_value.trigger_enter_event.assert_called_with(enemy)

    def test_init_treasure_is_instantiated(self):
        Map(['T'])
        treasure = self.TreasureMock.return_value
        self.EmptyCellMock.return_value.trigger_enter_event.assert_called_with(treasure)
        self.TreasureMock.assert_called_once()

    def test_init_raise_value_error_given_unknown_symbol(self):
        with self.assertRaises(ValueError):
            Map(['test'])

    @patch('src.map.next')
    def test_spawn_coords_of_hero_should_be_correct(self, next_mock):
        self.SpawnMock.return_value.row = 0
        self.SpawnMock.return_value.col = 0
        next_mock.return_value = self.SpawnMock.return_value

        test_map = Mock()
        test_map.grid = [[self.SpawnMock.return_value]]

        hero = self.HeroMock()

        Map.spawn(test_map, hero)
        self.assertEqual((hero.row, hero.col), (0, 0))

    @patch('src.map.next')
    def test_spawn_should_return_false_when_gen_is_exhausted(self, next_mock):
        hero = self.HeroMock()
        next_mock.side_effect = StopIteration

        test_map = Mock()

        self.assertFalse(Map.spawn(test_map, hero))

    @patch('src.map.next')
    def test_spawn_should_make_spawn_cell_empty_cell(self, next_mock):
        self.SpawnMock.return_value.row = 0
        self.SpawnMock.return_value.col = 0

        next_mock.return_value = self.SpawnMock.return_value

        test_map = Mock()
        test_map.grid = [[self.SpawnMock.return_value]]
        
        Map.spawn(test_map, self.HeroMock())

        self.EmptyCellMock.assert_called_with(row=0, col=0)

    @patch('src.map.next')
    def test_spawn_should_trigger_enter_event_on_empty_cell(self, next_mock):
        self.SpawnMock.return_value.row = 0
        self.SpawnMock.return_value.col = 0

        next_mock.return_value = self.SpawnMock.return_value

        test_map = Mock()
        test_map.grid = [[self.SpawnMock.return_value]]

        hero = self.HeroMock()
        Map.spawn(test_map, hero)

        self.EmptyCellMock.return_value.trigger_enter_event.assert_called_with(hero)

    def test_spawn_method_should_raise_type_error_if_arg_is_not_hero(self):
        hero = {'name': 'test', 'title': 'Less Mighty Tester'}

        with self.assertRaises(TypeError):
            Map.spawn(hero)

class MapMovementTests(unittest.TestCase):
    def setUp(self):
        class_dependencies = [
                'Hero', 'Treasure', 'Spawn', 'Gateway', 'Wall', 'Enemy', 'EmptyCell', ]
        symbols = ['H', 'T', 'S', 'G', '#', 'E', '.']
        patchers = [patch(f'src.map.{cls_name}') for cls_name in class_dependencies]

        for p, cls_name, sym in zip(patchers, class_dependencies, symbols):
            setattr(self, f'{cls_name}Mock', p.start())
            setattr(getattr(self, f'{cls_name}Mock'), 'sym', sym)

        self.map = Mock()
        self.hero = self.HeroMock()

        self.addCleanup(patch.stopall)

    def test_move_without_prior_spawn_should_raise_value_error(self):
        self.map.hero = None

        with self.assertRaises(ValueError):
            Map.move_hero(self.map, 'up')

    @patch('src.map.isinstance')
    def tests_move_on_walkable_objects_in_bounds_should_return_true(self, isinstance_mock):
        self.map.hero = self.hero
        isinstance_mock.return_value = True
        empty_cell = self.EmptyCellMock.return_value

        with self.subTest('move up'):
            self.map.grid = [[empty_cell], [empty_cell]]
            self.hero.row, self.hero.col = 1, 0

            self.assertTrue(Map.move_hero(self.map, 'up'))

        with self.subTest('move down'):
            self.map.grid = [[empty_cell], [empty_cell]]
            self.hero.row, self.hero.col = 0, 0

            self.assertTrue(Map.move_hero(self.map, 'down'))

        with self.subTest('move left'):
            self.map.grid = [[empty_cell, empty_cell]]
            self.hero.row, self.hero.col = 0, 1

            self.assertTrue(Map.move_hero(self.map, 'left'))

        with self.subTest('move right'):
            self.map.grid = [[empty_cell, empty_cell]]
            self.hero.row, self.hero.col = 0, 0

            self.assertTrue(Map.move_hero(self.map, 'right'))

    def test_move_row_out_of_bounds_should_return_false(self):
        self.map.grid = [[self.EmptyCellMock.return_value]]
        self.map.hero = self.hero
        self.hero.row, self.hero.col = 0, 0

        with self.subTest('move up'):
            self.assertFalse(Map.move_hero(self.map, 'up'))

        with self.subTest('move down'):
            self.assertFalse(Map.move_hero(self.map, 'down'))

    def test_move_col_out_of_bounds_should_return_false(self):
        self.hero.row, self.hero.col = 0, 0
        self.map.hero = self.hero
        self.map.grid = [[self.EmptyCellMock.return_value]]

        with self.subTest('move left'):
            self.assertFalse(Map.move_hero(self.map, 'left'))

        with self.subTest('move right'):
            self.assertFalse(Map.move_hero(self.map, 'right'))

    @patch('src.map.isinstance')
    def test_move_on_non_walkable_object_should_return_false(self, isinstance_mock):
        self.map.hero = self.hero
        empty_cell, wall_cell = self.EmptyCellMock.return_value, self.WallMock.return_value
        self.map.grid = [[wall_cell, wall_cell, wall_cell ], [wall_cell, empty_cell, wall_cell], [wall_cell, wall_cell, wall_cell ]]
        self.hero.row, self.hero.col = 1, 1

        isinstance_mock.return_value = False
        
        self.assertFalse(Map.move_hero(self.map, 'up'))
        self.assertFalse(Map.move_hero(self.map, 'down'))
        self.assertFalse(Map.move_hero(self.map, 'left'))
        self.assertFalse(Map.move_hero(self.map, 'right'))

    @patch('src.map.isinstance')
    def test_move_should_update_hero_coordinated(self, isinstance_mock):
        self.map.hero = self.hero
        empty_cell  = self.EmptyCellMock.return_value
        self.hero.row, self.hero.col = 0, 0

        self.map.grid = [[empty_cell, empty_cell]]
        Map.move_hero(self.map, 'right')
        self.assertEqual((self.hero.row, self.hero.col), (0, 1))

    @patch('src.map.isinstance')
    def test_move_should_trigger_leave_event(self, isinstance_mock):
        self.map.hero = self.hero
        self.hero.row, self.hero.col = 0, 0
        empty_cell = self.EmptyCellMock.return_value

        self.map.grid = [[empty_cell, empty_cell]]

        Map.move_hero(self.map, 'right')
        empty_cell.trigger_leave_event.assert_called_with()

    @patch('src.map.isinstance')
    def test_move_should_trigger_enter_event_on_targer_cell(self, isinstance_mock):
        self.map.hero = self.hero
        self.hero.row, self.hero.col = 0, 0
        empty_cell = self.EmptyCellMock.return_value

        self.map.grid = [[empty_cell, empty_cell]]

        Map.move_hero(self.map, 'right')
        empty_cell.trigger_enter_event.assert_called_with(self.hero)


if __name__ == '__main__':
    unittest.main()
