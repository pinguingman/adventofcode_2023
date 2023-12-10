from math import ceil, floor, sqrt


def main():
    result = 1
    with open("input.txt") as f:
        times = f.readline()
        times = [t for t in times.split()[1:] if t]
        times = [int("".join(times))]

        distances = f.readline()
        distances = [d for d in distances.split()[1:] if d]
        distances = [int("".join(distances))]

    for time, distance in zip(times, distances):
        D = time**2 - 4 * distance
        x1 = (-time - sqrt(D)) / -2
        x2 = (-time + sqrt(D)) / -2

        ax = min(x1, x2)
        bx = max(x1, x2)

        if not bx % 1:
            bx -= 1
        bx = floor(bx)
        if not ax % 1:
            ax += 1
        ax = ceil(ax)

        result *= bx - ax + 1
        print(time, distance, ":", ax, bx, (bx - ax + 1))
    return result


if __name__ == "__main__":
    main()
