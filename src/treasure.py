from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.walkable import WalkableMixin as Walkable
from src.game_object import GameObject


class Treasure(GameObject, Walkable, Printable):
    sym = 'T'

    def __init__(self, *, row, col):
        super().__init__(row, col)

    def _on_enter(self, obj):
        print('kompot')
