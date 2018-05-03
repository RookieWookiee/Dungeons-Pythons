from src.game_object import GameObject
from src.weapon import Weapon
from src.spell import Spell


class WarUnit(GameObject):

    def __init__(self, row, col, health, mana, damage=0):
        super().__init__(row, col)
        self.health = health
        self.mana = mana
        self._max_mana = self.mana
        self._min_mana = 0
        self._min_health = 1
        self._max_health = self.health
        self.weapon = None
        self.spell = None
        self.damage = damage

    def is_alive(self):
        if self.health < 1:
            return False
        return True

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
        else:
            raise(ValueError("The hero can be equipped only with Weapon!"))

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.spell = spell
        else:
            raise (ValueError("The hero can learn onli Spell"))

    def can_cast(self):
        if self.spell and self.mana >= self.spell.mana_cost:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points < 0:
            raise ValueError
        elif type(damage_points) is int or type(damage_points) is float:
            if damage_points > self.health:
                self.health = self._min_health - 1
            else:
                self.health -= damage_points
        else:
            raise TypeError

    def take_healing(self, healing_points):
        assert healing_points > 0
        assert type(healing_points) is int or type(healing_points) is float

        if not self.is_alive():
            return False
        elif healing_points + self.health > self._max_health:
            self.health = self._max_health
        else:
            self.health += healing_points

    def take_mana(self, mana_points):
        if self.mana + mana_points <= self._max_mana:
            self.mana += mana_points
        else:
            self.mana = self._max_mana

    def attack(self, by=None):
        # To be refactored
        # Wrong method !!!
        # Logic for first_hit and etc ...
        if by == "weapon":
            if self.weapon:
                return self.weapon.damage
            else:
                return 0
        if by == "spell":
            if self.spell:
                if self.mana >= self.spell.mana_cost:
                    self.mana -= self.spell.mana_cost
                    return self.spell.damage
                else:
                    raise ValueError(
                        "Your mana is lower than the spell mana_cost.")
            else:
                return 0
        return self.damage
