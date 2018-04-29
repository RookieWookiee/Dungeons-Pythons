from src.map import Map
from src.hero import Hero


def main():
    lvl = Map.load('./assets/maps/level1.txt')
    lvl.print_map()


if __name__ == '__main__':
    main()
    
lvl = Map.load('./assets/maps/level1.txt')
lvl.print_map()
h = Hero(name='foo', title='bar', health=100, mana=100, mana_regeneration_rate=2)
lvl.spawn(h)
