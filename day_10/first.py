from collections import namedtuple
from math import ceil, floor

Point = namedtuple("Point", ["x", "y"], defaults=(None, None))

PIPES = {"|", "-", "L", "J", "7", "F", "S"}


def main():
    file = open("input.txt")
    maze = []
    previous_position = current_position = start_position = Point()
    for i, line in enumerate(file.read().split("\n")):
        maze.append(line)
        for j, value in enumerate(line):
            if value == "S":
                current_position = start_position = Point(j, i)

    counter = 0
    while True:
        next_position = get_next(maze, current_position, previous_position)
        print(next_position, maze[next_position.y][next_position.x])
        if next_position == start_position:
            break
        previous_position, current_position = current_position, next_position
        counter += 1
    print(ceil(counter / 2))


def get_next(maze, current_position: Point, previous_position: Point) -> Point:
    current_pipe = maze[current_position.y][current_position.x]
    if current_pipe == "|":
        next_positions = [
            Point(current_position.x, current_position.y - 1),
            Point(current_position.x, current_position.y + 1),
        ]
    elif current_pipe == "-":
        next_positions = [
            Point(current_position.x + 1, current_position.y),
            Point(current_position.x - 1, current_position.y),
        ]
    elif current_pipe == "L":
        next_positions = [
            Point(current_position.x + 1, current_position.y),
            Point(current_position.x, current_position.y - 1),
        ]
    elif current_pipe == "J":
        next_positions = [
            Point(current_position.x - 1, current_position.y),
            Point(current_position.x, current_position.y - 1),
        ]
    elif current_pipe == "7":
        next_positions = [
            Point(current_position.x - 1, current_position.y),
            Point(current_position.x, current_position.y + 1),
        ]
    elif current_pipe == "F":
        next_positions = [
            Point(current_position.x + 1, current_position.y),
            Point(current_position.x, current_position.y + 1),
        ]
    else:
        next_positions = [
            point
            for point in [
                Point(current_position.x + 1, current_position.y),
                Point(current_position.x, current_position.y + 1),
                Point(current_position.x - 1, current_position.y),
                Point(current_position.x, current_position.y - 1),
            ]
        ]

    for next_position in next_positions:
        try:
            next_pipe = maze[next_position.y][next_position.x]
        except IndexError:
            continue
        if next_pipe in PIPES and next_position != previous_position:
            return next_position


if __name__ == "__main__":
    print(main())
