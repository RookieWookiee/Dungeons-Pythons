from src.war_unit import WarUnit
from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.walkable import WalkableMixin as Walkable


class Enemy(WarUnit, Walkable, Printable):
    sym = 'E'

    def __init__(self, *, health, mana, damage, row=None, col=None):
        super().__init__(row, col, health, mana, damage)

    def _on_enter(self, obj):
        print('Fight!')
