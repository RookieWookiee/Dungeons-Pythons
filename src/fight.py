from src.hero import Hero
from src.enemy import Enemy


class Fight:

    def __init__(self, hero, enemy, first_hit=None):
        self.hero = hero
        self.enemy = enemy
        self.turn = hero
        self.first_hit = first_hit

    def start_fight(self):
        while True:
            if self.first_hit:
                self.enemy.take_damage(self.hero.attack(self.first_hit))
                self.first_hit = None
            else:
                self.enemy.take_damage(self.hero.attack())
            if not self.enemy.is_alive():
                break
            self.hero.take_damage(self.enemy.attack())
            if not self.hero.is_alive():
                break

        return hero if self.hero.is_alive() else self.enemy


h = Hero(health=100, mana=50, name="Yamamoto",
         title="Samurai", mana_regeneration_rate=2)

e = Enemy(health=100, mana=100, damage=20)

f = Fight(h, e)
