from typing import Optional


def main():
    result = 0
    with open("input.txt") as f:
        lines = [line for line in f.readlines()]
        for i, line in enumerate(lines):
            for j, symbol in enumerate(line):
                if symbol == "*":
                    ratio = get_ratio(i, j, lines)
                    result += ratio

    return result


def get_ratio(i, j, lines):
    result = 0
    numbers = []
    for x in range(i - 1, i + 2):
        skip_y_until: Optional[int] = None
        for y in range(j - 1, j + 2):
            if skip_y_until is not None:
                if y == skip_y_until:
                    skip_y_until = None
                    continue
                elif y < skip_y_until:
                    continue
                else:
                    skip_y_until = None
            try:
                symbol = lines[x][y]
            except IndexError:
                continue
            if symbol.isnumeric():
                number, skip_y_until = get_number_and_end(x, y, lines)
                numbers.append(number)
            else:
                continue
    if len(numbers) == 2:
        result += numbers[0] * numbers[1]
    return result


def get_number_and_end(i, j, lines) -> tuple[int, int]:
    # find first number char
    initial_j = j
    number = lines[i][j]
    j -= 1
    while True:
        try:
            symbol = lines[i][j]
        except IndexError:
            break
        else:
            if symbol.isnumeric():
                number = symbol + number
                j -= 1
            else:
                break

    j = initial_j + 1
    while True:
        try:
            symbol = lines[i][j]
        except IndexError:
            break
        else:
            if symbol.isnumeric():
                number += symbol
                j += 1
            else:
                break

    return int(number), j


if __name__ == "__main__":
    main()
