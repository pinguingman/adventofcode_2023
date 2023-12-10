def main():
    sum = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line_sum = get_sum(line)
            sum += line_sum
            print(line_sum, line, sum)

    return sum


TEXT_TO_INT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

TEXT_TO_INT_REVERSED = {key[::-1]: value for key, value in TEXT_TO_INT.items()}


def get_sum(line: str) -> int:
    first = "0"
    last = "0"
    for symbol in line:
        if symbol.isnumeric():
            first = symbol
            break
    for symbol in reversed(line):
        if symbol.isnumeric():
            last = symbol
            break

    return int(first + last)


def second():
    sum = 0
    with open("input.txt") as f:
        for line in f.readlines():
            first = get_sum_with_text(line, TEXT_TO_INT)
            second = get_sum_with_text(line[::-1], TEXT_TO_INT_REVERSED)
            line_sum = int(first + second)
            sum += line_sum
            print(line_sum, line, sum)

    return sum


def get_sum_with_text(line: str, text_to_int: dict) -> str:
    for i, symbol in enumerate(line):
        if symbol.isnumeric():
            return symbol
        else:
            for text, digit in text_to_int.items():
                if not symbol == text[0]:
                    continue
                for j in range(1, len(text)):
                    try:
                        if line[i + j] == text[j]:
                            continue
                        else:
                            break
                    except IndexError:
                        break
                else:
                    return str(digit)

    return "0"


if __name__ == "__main__":
    print(main())
