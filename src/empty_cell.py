from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.occupiable import OccupiableMixin as Occupiable
from src.game_object import GameObject


# TODO: override on_enter to replace the occupant
# if a hero takes a treasure for example
class EmptyCell(GameObject, Occupiable, Printable):
    sym = '.'

    def __init__(self, *, row, col):
        self.row = row
        self.col = col
        self.occupant = None

    def __str__(self):
        return str(self.occupant) if self.occupant is not None else self.sym
