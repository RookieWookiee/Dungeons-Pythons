from src.game_object import GameObject


class WarUnit(GameObject):
    def __init__(self, *, row, col, health, mana):
        super().__init__(row, col)
        self.health = health
        self.mana = mana
        self.min_health = 1
        self.max_health = self.health

    def is_alive(self):
        if self.health < 1:
            return False
        return True

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        pass

    def take_damage(self, damage_points):
        assert damage_points > self.min_health - 1
        assert type(damage_points) is int or type(damage_points) is float

        if damage_points > self.health:
            self.health = self.min_health - 1
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        assert healing_points > 0
        assert type(healing_points) is int or type(healing_points) is float

        if self.health < self.min_health:
            return False
        elif healing_points + self.health > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points
        return True

    def take_mana(mana_points):
        pass
