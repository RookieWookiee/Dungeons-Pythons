from src.war_unit import WarUnit
from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.walkable import WalkableMixin as Walkable


class Hero(WarUnit, Walkable, Printable):
    sym = 'H'

    def __init__(self, *, health, mana, name, mana_regeneration_rate, title, row=None, col=None,):
        super().__init__(row, col, health, mana)
        self.mana_regen = mana_regeneration_rate
        self.name = name
        self.title = title

    def __str__(self):
        return self.name

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def _on_enter(self, obj):
        print('Fight')
