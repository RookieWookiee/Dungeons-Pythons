from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.occupiable import OccupiableMixin as Occupiable
from src.game_object import GameObject


class Gateway(GameObject, Occupiable, Printable):
    sym = 'G'

    def __init__(self, *, row, col):
        super().__init__(row, col)
        self.occupant = None

    def __on_enter(self, obj):
        self.occupant = obj
        print("You've reached the end of the level. Na ti kompot")

    _on_enter = __on_enter
