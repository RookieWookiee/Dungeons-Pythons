class Weapon:
    def __init__(self, *, name, damage):
        self.name = name
        self.damage = damage

    @classmethod
    def generate(cls, obj):
        damage = int(obj._max_health * 0.3)
        return cls(name='Heartsbane', damage=damage)

    def equip(self, obj):
        obj.equip(weapon=self)
