from src.map import Map


def main():
    lvl = Map.load('./assets/maps/level1.txt')
    lvl.print_map()


if __name__ == '__main__':
    main()
