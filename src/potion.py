from src.mixins.consumable import ConsumableMixin as Consumable


class HealthPotion(Consumable):
    heal_percentage = 0.2

    def __init__(self, obj):
        self.heal_quantity = int(obj._max_health * self.heal_percentage)

    @classmethod
    def generate(cls, obj):
        return cls(obj)

    def consume(self, obj):
        obj.take_healing(self.heal_quantity)


class PotentHealthPotion(HealthPotion):
    heal_percentage = 0.5


class ManaPotion(Consumable):
    restore_percentage = 0.2

    def __init__(self, obj):
        self.mana_quantity = int(obj._max_mana * self.restore_percentage)

    @classmethod
    def generate(cls, obj):
        return cls(obj)

    def consume(self, obj):
        obj.take_mana(self.mana_quantity)


class PotentManaPotion(ManaPotion):
    restore_percentage = 0.5
