from src.mixins.print_sym import PrintSymbolMixin
from src.game_object import GameObject


class Gateway(PrintSymbolMixin, GameObject):
    def __init__(self, *, row, col):
        super().__init__(row, col)
        self.sym = 'G'
