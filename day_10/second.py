from collections import namedtuple

Point = namedtuple("Point", ["x", "y"], defaults=(None, None))

PIPES = {"|", "-", "L", "J", "7", "F", "S"}


def main():
    maze = []
    previous_position = current_position = start_position = Point()

    file = open("input.txt")
    for y, line in enumerate(file.read().split("\n")):
        maze.append(line)
        for x, value in enumerate(line):
            if value == "S":
                current_position = start_position = Point(x, y)

    line_to_pipes = [[] for _ in range(len(maze))]

    counter = 0
    while True:
        next_position = get_next(maze, current_position, previous_position)

        line_to_pipes[next_position.y].append(next_position.x)

        print(next_position, maze[next_position.y][next_position.x])
        if next_position == start_position:
            break
        previous_position, current_position = current_position, next_position

    print("Count pipes")
    for y, pipes in enumerate(line_to_pipes):
        if not pipes:
            continue
        pipes.sort()
        first_pipe, last_pipe = pipes[0], pipes[-1]
        for x in range(first_pipe + 1, last_pipe):
            if x not in pipes:
                intersections = 0
                for xx in range(x, last_pipe + 1):
                    pipe = maze[y][xx]
                    if xx in pipes and pipe in {
                        "|",
                        "F",
                        "7",
                    }:
                        intersections += 1
                if intersections % 2:
                    counter += 1
                    print(Point(x, y))

    return counter


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
        # Start case
        # up
        next_positions = []
        try:
            pipe = maze[current_position.y - 1][current_position.x]
        except IndexError:
            pass
        else:
            if pipe in {"|", "7", "F"}:
                Point(current_position.x, current_position.y - 1)

        # down
        try:
            pipe = maze[current_position.y + 1][current_position.x]
        except IndexError:
            pass
        else:
            if pipe in {"|", "L", "J"}:
                return Point(current_position.x, current_position.y + 1)
        # left
        try:
            pipe = maze[current_position.y][current_position.x - 1]
        except IndexError:
            pass
        else:
            if pipe in {"-", "L", "F"}:
                return Point(current_position.x - 1, current_position.y)

        # right
        try:
            pipe = maze[current_position.y][current_position.x + 1]
        except IndexError:
            pass
        else:
            if pipe in {"-", "J", "7"}:
                return Point(current_position.x + 1, current_position.y)

    for next_position in next_positions:
        try:
            next_pipe = maze[next_position.y][next_position.x]
        except IndexError:
            continue
        if next_pipe in PIPES and next_position != previous_position:
            return next_position


if __name__ == "__main__":
    print(main())
