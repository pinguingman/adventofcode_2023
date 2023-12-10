def main():
    file = open("input.txt")
    directions = file.readline().strip()
    mapping = {}
    for line in file.readlines():
        try:
            key, values = line.split("=")
        except:
            continue
        key = key.strip()
        left, right = values.strip(" ()\n").split(", ")
        mapping[key] = {"L": left, "R": right}
    i = 0
    steps = 0
    position = "AAA"
    end_key = "ZZZ"

    while True:
        try:
            direction = directions[i]
        except Exception as e:
            print(f"new lap {e}")
            i = 0
            direction = directions[i]

        print(
            f"{position} {list(mapping[position].values())} {direction} -> ",
            end="",
        )

        position = mapping[position][direction]
        print(position)
        if position == end_key:
            print(steps + 1)
            return

        steps += 1
        i += 1


if __name__ == "__main__":
    main()
