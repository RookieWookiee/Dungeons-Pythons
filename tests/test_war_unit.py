import unittest
from src.war_unit import WarUnit


class TestWarUnit(unittest.TestCase):
    def setUp(self):
        self.hero = WarUnit(row=0, col=0, health=100, mana=20)

    def test_is_alive(self):
        with self.subTest("Test if hero is alive"):
            self.assertTrue(self.hero.is_alive())

        self.hero.health = 0

        with self.subTest("Test if hero is dead"):
            self.assertFalse(self.hero.is_alive())

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), 20)

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
            with self.assertRaises(AssertionError):
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
            self.assertTrue(self.hero.take_healing(200))

        with self.subTest("Is the hero's health is max possible health after the last healing - 200 points"):
            self.assertEqual(self.hero.health, self.hero.max_health)

    def tearDown(self):
        self.hero = WarUnit(row=0, col=0, health=100, mana=20)


if __name__ == "__main__":
    unittest.main()
