from src.war_unit import WarUnit
from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.walkable import WalkableMixin as Walkable


class Enemy(WarUnit, Walkable, Printable):
    sym = 'E'

    def __init__(self, *, row=None, col=None, health, mana, damage):
        super().__init__(row, col, health, mana)
        self.damage = damage

    def __on_enter(self, obj):
        print('Fight!')

    _on_enter = __on_enter
