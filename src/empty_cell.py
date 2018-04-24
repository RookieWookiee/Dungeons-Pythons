from src.mixins.print_sym import PrintSymbolMixin
from src.game_object import GameObject


class EmptyCell(PrintSymbolMixin, GameObject):
    def __init__(self, *, row, col):
        self.row = row
        self.col = col
        self.sym = '.'
