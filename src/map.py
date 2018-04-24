from src.wall import Wall
from src.empty_cell import EmptyCell
from src.spawn import Spawn
from src.treasure import Treasure
from src.gateway import Gateway


class Map:
    #TODO: add enemy and hero
    __class_lookup = {
            '.': EmptyCell,
            '#': Wall,
            'S': Spawn,
            'T': Treasure,
            'G': Gateway
            }

    def __init__(self, lines):
        self.grid = []
        spawnpoints = []
        len_rows = len(lines)

        for row, line in zip(range(len_rows), lines):
            len_cols = len(lines[row])
            self.grid.append([])

            for col, sym in zip(range(len_cols), line):
                obj = self.__class_lookup[sym](row=row, col=col)
                self.grid[-1].append(obj)

                if isinstance(obj, Spawn):
                    spawnpoints.append(obj)

        self.spawnpoints = iter(spawnpoints)

    @classmethod
    def load(cls, fname):
        with open(fname) as f:
            return cls(f.readlines())

    def print_map(self):
        for row in self.grid:
            row_str = map(str, row)
            print("".join(row_str))

    #TODO: test it
    def spawn(self, hero):
        try:
            cell = next(self.spawnpoints)
            row, col = cell.row, cell.col
            cell = EmptyCell()  #This probably won't work
            cell.row, cell.col = row, col

            return True
        except StopIteration:
            return False

    def move_hero(self):
        pass
