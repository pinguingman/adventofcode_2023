from math import lcm


def main():
    file = open("input.txt")
    directions = file.readline().strip()
    mapping = {}
    positions = []
    for line in file.readlines():
        try:
            key, values = line.split("=")
        except:
            continue
        key = key.strip()
        if key[2] == "A":
            positions.append(key)
        left, right = values.strip(" ()\n").split(", ")
        mapping[key] = {"L": left, "R": right}
    i = 0
    steps = 0
    results = []
    while True:
        try:
            direction = directions[i]
        except Exception as e:
            print(f"new lap {e}")
            i = 0
            direction = directions[i]

        print(steps, direction, positions)
        to_remove = []
        if not positions:
            print(lcm(*results))
            return
        for j, position in enumerate(positions):
            positions[j] = mapping[position][direction]
            if positions[j][2] == "Z":
                to_remove.append(positions[j])
                results.append(steps + 1)

        for key in to_remove:
            positions.remove(key)

        steps += 1
        i += 1


if __name__ == "__main__":
    main()
