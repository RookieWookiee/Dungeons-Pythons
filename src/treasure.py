from src.mixins.print_sym import PrintSymbolMixin as Printable
from src.mixins.walkable import WalkableMixin as Walkable
from src.mixins.consumable import ConsumableMixin as Consumable
from src.game_object import GameObject
from src.weapon import Weapon
from src.spell import Spell
from src.potion import (
    HealthPotion, ManaPotion,
    PotentHealthPotion, PotentManaPotion
)

import random


class Treasure(GameObject, Walkable, Printable):
    sym = 'T'
    items = [
        Weapon, Spell,
        HealthPotion, ManaPotion,
        PotentHealthPotion, PotentManaPotion
    ]

    def __init__(self, *, row, col):
        super().__init__(row, col)

    def _on_enter(self, obj):
        cls = random.choice(self.items)
        reward = cls.generate(obj)

        if isinstance(reward, Consumable):
            reward.consume(obj)
        else:
            reward.equip(obj)
        
        return True
