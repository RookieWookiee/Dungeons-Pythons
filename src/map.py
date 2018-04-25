from src.wall import Wall
from src.empty_cell import EmptyCell
from src.spawn import Spawn
from src.treasure import Treasure
from src.gateway import Gateway
from src.hero import Hero
from src.enemy import Enemy

from os import linesep


class Map:
    __class_lookup = {
            '.': EmptyCell,
            'T': EmptyCell,
            'E': EmptyCell,
            '#': Wall,
            'S': Spawn,
            'G': Gateway,
            }

    def __init__(self, lines):
        self.grid = []
        spawnpoints = []
        self.hero = None
        self.treasures = set()
        self.enemies = set()

        len_rows = len(lines)

        for row, line in zip(range(len_rows), lines):
            len_cols = len(lines[row])
            self.grid.append([])

            for col, sym in zip(range(len_cols), line):
                obj = self.__class_lookup[sym](row=row, col=col)

                if sym == Treasure.sym:
                    treasure = Treasure(row=row, col=col)
                    obj.occupant = treasure
                    self.treasures.add(treasure)
                elif sym == Enemy.sym:
                    enemy = Enemy(row=row, col=col, health=None, mana=None, damage=None)
                    obj.occupant = enemy
                    self.enemies.add(enemy)

                self.grid[-1].append(obj)

                if isinstance(obj, Spawn):
                    spawnpoints.append(obj)

        self.spawnpoints = iter(spawnpoints)

    @classmethod
    def load(cls, fname):
        with open(fname) as f:
            return cls([x.strip() for x in f])

    def __str__(self):
        res = []
        rows = len(self.grid)

        for row in self.grid:
            str_row = map(str, row)
            res.append(''.join(str_row))

        return linesep.join(res)

    def print_map(self):
        print(self)

    def spawn(self, hero):
        self.hero = hero

        if not isinstance(hero, Hero):
            expected, actual = Hero.__name__, hero.__class__.__name__
            raise TypeError(
                    f'Invalid hero: expected {expected}, got {actual}')

        try:
            spawn = next(self.spawnpoints)
            self.grid[spawn.row][spawn.col] = new_cell = EmptyCell(row=spawn.row, col=spawn.col)
            new_cell.occupant = hero
            self.hero.row, self.hero.col = spawn.row, spawn.col

            return True
        except StopIteration:
            return False

    def move_hero(self):
        pass
