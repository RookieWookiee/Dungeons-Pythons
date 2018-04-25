from src.game_object import GameObject


class WarUnit(GameObject):
    def __init__(self, *, row, col, health, mana, damage=0):
        super().__init__(row, col)
        self.health = health
        self.mana = mana
        self._max_mana = self.mana
        self._min_mana = 0
        self._min_health = 1
        self._max_health = self.health
        self._weapon = None
        self._spell = None
        self.damage = damage

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
        assert damage_points > self._min_health - 1
        assert type(damage_points) is int or type(damage_points) is float

        if damage_points > self.health:
            self.health = self._min_health - 1
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        assert healing_points > 0
        assert type(healing_points) is int or type(healing_points) is float

        if self.health < self._min_health:
            return False
        elif healing_points + self.health > self._max_health:
            self.health = self._max_health
        else:
            self.health += healing_points
        return True

    def take_mana(self, mana_points):
        if self.mana + mana_points <= self._max_mana:
            self.mana += mana_points
        else:
            self.mana = self._max_mana
        return True

    def attack(self, by=None):
        # To be refactored
        if by == "weapon":
            if self._weapon:
                return self._weapon.damage
            else:
                return 0
        if by == "spell":
            if self._spell:
                if self.mana >= self._spell.mana_cost:
                    self.mana -= self._spell.mana_cost
                    return self._spell.damage
                else:
                    raise ValueError(
                        "Your mana is lower than the spell mana_cost.")
            else:
                return 0
        return self.damage
