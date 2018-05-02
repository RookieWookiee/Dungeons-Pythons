import random


class Spell:
    presets = [
            {'name': '1', 'dmg': 0.5, 'mana_cost': 0.4, 'range': 2},
            {'name': '2', 'dmg': 0.3, 'mana_cost': 0.2, 'range': 1},
            {'name': '3', 'dmg': 0.1, 'mana_cost': 0.1, 'range': 1},
            {'name': '4', 'dmg': 0.2, 'mana_cost': 0.25, 'range': 3}
        ]

    def __init__(self, *, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    @classmethod
    def generate(cls, obj):
        selection = random.choice(cls.presets)

        name = selection['name']
        dmg = int(obj._max_health * selection['dmg'])
        mana_cost = int(obj._max_mana * selection['mana_cost'])
        cast_range = selection['range']

        return cls(name=name, damage=dmg, mana_cost=mana_cost, cast_range=cast_range)

    def equip(self, obj):
        obj.learn(spell=self)
