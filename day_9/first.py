def main():
    result = 0
    file = open("input.txt")
    for line in file.readlines():
        values = list(map(int, line.split()))
        result += get_next_value(values)
    return result


def get_next_value(values):
    differences = [values]
    while True:
        print(values)
        next_differences = []
        all_zeroes = True
        for i, value in enumerate(values):
            try:
                difference = values[i + 1] - value
            except IndexError:
                break
            if difference:
                all_zeroes = False
            next_differences.append(difference)
        differences.append(next_differences)
        values = next_differences
        if all_zeroes:
            differences[-1].append(0)
            break

    for i in range(len(differences) - 2, -1, -1):
        differences[i].append(differences[i + 1][-1] + differences[i][-1])

    return differences[0][-1]


if __name__ == "__main__":
    print(main())
