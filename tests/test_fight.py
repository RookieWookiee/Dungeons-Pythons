from src.hero import Hero
from src.enemy import Enemy
from src.fight import Fight
from src.weapon import Weapon
from src.spell import Spell
import unittest


class TestFight(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(health=100, mana=50,
                         name="Yamamoto", title="Samurai", mana_regeneration_rate=2)
        self.enemy = Enemy(health=100, mana=100, damage=20)
        self.weapon = Weapon.generate(self.hero)
        self.spell = Spell(name="Fireball", damage=30,
                           mana_cost=50, cast_range=2)
        self.hero.learn(self.spell)
        self.hero.equip(self.weapon)

    def test_simple_fight_in_one_cell(self):
        fight = Fight(self.hero, self.enemy)
        self.assertIs(fight.start_fight(), self.hero)

    def test_sipmle_fight_starts_with_weapon(self):
        fight = Fight(self.hero, self.enemy, "spell")
        self.assertIs(fight.start_fight(), self.hero)
        print(self.hero.__dict__)


if __name__ == "__main__":
    unittest.main()
