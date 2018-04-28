from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.occupiable import OccupiableMixin as Occupiable
from src.game_object import GameObject


class Spawn(GameObject, Occupiable, Printable):
    sym = 'S'

    def __init__(self, *, row, col):
        super().__init__(row, col)
        self.occupant = None
