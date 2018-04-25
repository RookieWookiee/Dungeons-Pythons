from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.game_object import GameObject


class Wall(GameObject, Printable):
    sym = '#'

    def __init__(self, *, row, col):
        super().__init__(row, col)
