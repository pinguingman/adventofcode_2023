seed_to_result = {}


def main():
    mapping = {}
    with open("input.txt") as f:
        seeds = [int(s) for s in f.readline().split(":")[1].strip().split()]
        name = None
        while 1:
            line = f.readline().strip().split()
            if not line:
                break
            print("line", line)
            if len(line) == 2:
                name = line[0]
                mapping[name] = []
                continue

            mapping[name].append([int(x) for x in line])

    while seeds:
        threads = []
        seed_start = seeds.pop(0)
        seed_range = seeds.pop(0)
        ranges = [seed_start, seed_range + seed_start]
        print("seed ranges", ranges)
        for range_start, range_end in ranges:
            for name, name_mapping in mapping.items():
                for maps in name_mapping:
                    ranges = process_seed_range(range_start, range_end, maps)

    return min(seed_to_result.values())


def process_seed_range(start, end, mapping):
    # print("processing seed:", seed)
    value = seed
    for name, name_mapping in mapping.items():
        for end, start, length in name_mapping:
            if value >= start and value < start + length:
                value = end + (value - start)
                # print("mapped:", (name, (end, start, length) ), "new value:", value)
                break
        else:
            pass
            # print("unmapped:", seed, "value:", value)
    # print("finish seed:", seed, value)


def process_seed(seed, mapping):
    # print("processing seed:", seed)
    value = seed
    for name, name_mapping in mapping.items():
        for end, start, length in name_mapping:
            if value >= start and value < start + length:
                value = end + (value - start)
                # print("mapped:", (name, (end, start, length) ), "new value:", value)
                break
        else:
            pass
            # print("unmapped:", seed, "value:", value)
    # print("finish seed:", seed, value)

    seed_to_result[seed] = value


if __name__ == "__main__":
    main()
