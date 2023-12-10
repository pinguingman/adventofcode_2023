def main():
    with open("input.txt") as f:
        result = get_sum(f)

    print(result)


def get_sum(file):
    result = 0
    lines = [file.readline()[:-1]]
    i = -1
    have_more_lines = True
    while have_more_lines:
        try:
            line = file.readline()[:-1]
            if not line:
                have_more_lines = False
            i += 1
            lines.append(line)
        except StopIteration:
            have_more_lines = False

        current_num = ""
        need_to_add = False
        for j, symbol in enumerate(lines[i]):
            if symbol.isnumeric():
                current_num += symbol
                if not need_to_add:
                    need_to_add = have_adjusting_symbols(lines, i, j)
            else:
                if need_to_add:
                    print("add num", current_num)
                    result += int(current_num)
                current_num = ""
                need_to_add = False
        else:
            if need_to_add:
                print("add num at end", current_num)
                result += int(current_num)
    return result


def have_adjusting_symbols(lines: list[list[str]], x: int, y: int):
    for i in range(x - 1, x + 2):
        if i < 0:
            continue
        for j in range(y - 1, y + 2):
            if j < 0:
                continue
            try:
                if not lines[i][j].isnumeric() and lines[i][j] != ".":
                    return True
            except IndexError:
                pass

    return False


if __name__ == "__main__":
    main()
