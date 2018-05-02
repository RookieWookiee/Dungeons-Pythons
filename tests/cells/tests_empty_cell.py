import unittest
from src.cells.empty_cell import EmptyCell
from unittest.mock import Mock


class OccupiableEmptyCellTests(unittest.TestCase):
    def test_str_on_empty_cell_returns_symbol(self):
        self.assertEqual(str(EmptyCell(row=0, col=0)), EmptyCell.sym)

    def test_cell_with_occupant_should_trigger_occupant_event(self):
        cell = EmptyCell(row=0, col=0)
        cell.occupant = Mock()
        cell.trigger_enter_event(Mock())

        cell.occupant.trigger_enter_event.assert_called

    def test_occupant_trigger_return_true_replace_occupant_with_new_obj(self):
        cell = EmptyCell(row=0, col=0)

        occupant = Mock()
        occupant._on_enter.return_value = True

        cell.occupant = occupant

        new_occupant = Mock()
        new_occupant.sym = 't'
        cell.trigger_enter_event(new_occupant)

        self.assertEqual(cell.sym, 't')

    def test_occupant_trigger_return_false_do_not_replace_occupant(self):
        cell = EmptyCell(row=0, col=0)

        occupant = Mock()
        occupant._on_enter.return_value = False
        cell.occupant = occupant

        new_occupant = Mock()
        new_occupant.sym = 't'
        cell.trigger_enter_event(new_occupant)

        self.assertEqual(cell.sym, EmptyCell.sym)
