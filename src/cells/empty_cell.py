from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.occupiable import OccupiableMixin as Occupiable
from src.game_object import GameObject


class EmptyCell(GameObject, Occupiable, Printable):
    sym = '.'

    def __init__(self, *, row, col):
        self.row = row
        self.col = col
        self.occupant = None
