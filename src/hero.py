from src.war_unit import WarUnit
from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.walkable import WalkableMixin as Walkable


class Hero(WarUnit, Walkable, Printable):
    sym = 'H'

    def __init__(self, *, row=None, col=None, health, mana, name, title=None, mana_regeneration_rate):
        super().__init__(row, col, health, mana)
        self.mana_regen = mana_regeneration_rate
        self.name = name
        self.title = title

    def equip(weapon):
        pass

    def learn(spell):
        pass
    
    def __on_enter(self, obj):
        print('Fight')

    _on_enter = __on_enter
