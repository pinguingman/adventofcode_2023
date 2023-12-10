def main():
    with open("input.txt") as f:
        result = get_sum(f)

    print(result)


def get_sum(file):
    points = 0
    for line in file:
        line = line[:-1].split(":")[1]
        wins, yours = line.split("|")
        wins = set(x for x in wins.split(" ") if x != "")
        yours = set(x for x in yours.split(" ") if x != "")
        your_wins_count = len(yours.intersection(wins))
        if your_wins_count:
            line_points = 1
            for _ in range(1, your_wins_count):
                line_points *= 2

            points += line_points
            print(f"{line} {your_wins_count} {line_points}")
    return points


if __name__ == "__main__":
    main()
