import unittest
from src.war_unit import WarUnit
from src.weapon import Weapon
from src.spell import Spell
from src.hero import Hero
from src.enemy import Enemy


class TestWarUnit(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(health=100, mana=50,
                         name="Yamamoto", title="Samurai", mana_regeneration_rate=2)
        self.enemy = Enemy(health=100, mana=100, damage=20)

    def test_is_alive(self):
        with self.subTest("Test if hero is alive"):
            self.assertTrue(self.hero.is_alive())

        self.hero.health = 0

        with self.subTest("Test if hero is dead"):
            self.assertFalse(self.hero.is_alive())

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), 50)

    def test_take_damage(self):
        with self.subTest("Test reduce the hero's health by damage"):
            self.hero.take_damage(10.5)
            # hero_healyh = self.hero.get_health()
            self.assertEqual(self.hero.get_health(), 89.5)

        with self.subTest("Test reduce the hero's health to negative value"):
            self.hero.take_damage(200)
            # hero_healyh = self.hero.get_health()
            self.assertEqual(self.hero.get_health(), 0)

        with self.subTest("Damage_points is positive"):
            with self.assertRaises(ValueError):
                self.hero.take_damage(-10)

        with self.subTest("Damage_points is int or float"):
            with self.assertRaises(TypeError):
                self.hero.take_damage("10.5")

    def test_take_healing(self):
        with self.subTest("healing_points is positive"):
            with self.assertRaises(AssertionError):
                self.hero.take_healing(-10)

        with self.subTest("Type of healing_points is int or float"):
            with self.assertRaises(TypeError):
                self.hero.take_healing("10")

        with self.subTest("Try to heal dead hero"):
            self.hero.health = 0
            self.assertFalse(self.hero.take_healing(10))
            # back the hero health

        self.hero.health = 50
        with self.subTest("Try to heal hero with more than the max possible healing_points"):
            self.hero.take_healing(200)
            self.assertEqual(self.hero.get_health(), self.hero._max_health)

        with self.subTest("Is the hero's health is max possible health after the last healing - 200 points"):
            self.assertEqual(self.hero.health, self.hero._max_health)

    def test_attack(self):
        weapon = Weapon(name="bow", damage=10)
        spell = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        gun = Weapon(name="gun", damage=40)
        ice = Spell(name="Ice", damage=50, mana_cost=50, cast_range=1)
        self.hero.equip(weapon)
        self.hero.learn(spell)

        with self.subTest("Hero attack with spell.damage > weapon.damage"):
            self.assertEqual(self.hero.attack(), spell.damage)

        with self.subTest("Hero attack with weapon if hero dont know spell"):
            self.hero.weapon = None
            self.assertEqual(self.hero.attack(), spell.damage)

        with self.subTest("Enemy attack with only damage"):
            self.assertEqual(self.enemy.attack(), self.enemy.damage)

        with self.subTest("Enemy attack with weapon"):
            self.enemy.equip(gun)
            self.assertEqual(self.enemy.attack(), gun.damage)

        with self.subTest("Attack method by weapon"):
            self.hero.equip(weapon)
            self.assertEqual(self.hero.attack(by="weapon"), 10)

        with self.subTest("Attack method by spell"):
            self.assertEqual(self.hero.attack(by="spell"), 30)

        with self.subTest("Try to attack with non-existent weapon"):
            self.hero.weapon = None
            self.assertEqual(self.hero.attack(by="weapon"), 0)

        with self.subTest("Try to attack with spell if hero's mana is lower than the Spell.mana_cost"):
            with self.assertRaises(ValueError):
                self.hero.attack(by="spell")

    def test_take_mana(self):
        self.hero.take_mana(100)
        self.assertEqual(self.hero.mana, 50)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Yamamoto the Samurai")

    def tearDown(self):
        self.hero = WarUnit(row=0, col=0, health=100, mana=50)


if __name__ == "__main__":
    unittest.main()
