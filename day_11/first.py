from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Point:
    x: int = None
    y: int = None


def main():
    galaxies = []
    galaxies_by_x: dict[int, list[Point]] = defaultdict(list)
    y_add = 0

    line = ""
    for y, line in enumerate(open("input.txt").readlines()):
        empty_line = True
        for x, symbol in enumerate(line):
            if symbol == "#":
                galaxy = Point(x, y + y_add)
                galaxies.append(galaxy)
                galaxies_by_x[x].append(galaxy)
                empty_line = False
        if empty_line:
            y_add += 1

    x_add = 0
    for x in range(len(line)):
        if galaxies_by_x.get(x):
            for galaxy in galaxies_by_x[x]:
                galaxy.x += x_add
        else:
            x_add += 1

    lengths = 0
    for i, galaxy in enumerate(galaxies):
        for ii, other_galaxy in enumerate(galaxies[i + 1 :]):
            path = abs(galaxy.x - other_galaxy.x) + abs(
                galaxy.y - other_galaxy.y
            )
            lengths += path
            print(i + 1, galaxy, ii + i + 2, other_galaxy, path)
    return lengths


if __name__ == "__main__":
    print(main())
