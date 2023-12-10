def main():
    result = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line_sum = get_sum(line)
            result += line_sum
            print(line_sum, line, result)

    return result


def second():
    result = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line_sum = get_sum2(line)
            result += line_sum
            print(line_sum, line, result)

    return result


MAX_BALLS = {"red": 12, "green": 13, "blue": 14}


def get_sum(line: str):
    game_num, games = line.split(":")
    game_num = int(game_num.split(" ")[1])
    for game in games.split(";"):
        ball_result = {"red": 0, "green": 0, "blue": 0}
        for balls in game.split(","):
            balls = balls.strip()
            num, colour = balls.split(" ")
            num = int(num)
            ball_result[colour] += num

        for color, num in ball_result.items():
            if num > MAX_BALLS[color]:
                return 0

    return game_num


def get_sum2(line: str):
    games = line.split(":")[1]
    ball_result = {"red": 0, "green": 0, "blue": 0}
    for game in games.split(";"):
        for balls in game.split(","):
            balls = balls.strip()
            num, colour = balls.split(" ")
            num = int(num)
            ball_result[colour] = (
                ball_result[colour] if ball_result[colour] > num else num
            )

    result = 1
    for num in ball_result.values():
        result *= num

    return result


if __name__ == "__main__":
    print(main())
