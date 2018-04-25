from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.occupiable import OccupiableMixin as Walkable
from src.game_object import GameObject


class Gateway(GameObject, Walkable, Printable):
    sym = 'G'

    def __init__(self, *, row, col):
        super().__init__(row, col)

    def __on_enter(self, obj):
        print("You've reached the end of the level. Na ti kompot")

    _on_enter = __on_enter
