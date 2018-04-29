from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.occupiable import OccupiableMixin as Occupiable
from src.game_object import GameObject


class Gateway(GameObject, Occupiable, Printable):
    sym = 'G'

    def __init__(self, *, row, col):
        super().__init__(row, col)
        self.occupant = None

    def _on_enter(self, obj):
        super()._on_enter(obj)
        print("You've reached the end of the level. Na ti kompot")
