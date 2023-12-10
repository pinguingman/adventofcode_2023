from collections import defaultdict


def main():
    with open("input.txt") as f:
        result = get_sum(f)

    print(result)


def get_sum(file):
    points = 0
    cards_to_count = defaultdict(lambda: 1)

    for line in file:
        card_num, line = line[:-1].split(":")
        card_num = int(card_num.split(" ")[-1])

        wins, yours = line.split("|")
        wins = set(x for x in wins.split(" ") if x != "")
        yours = set(x for x in yours.split(" ") if x != "")
        your_wins_count = len(yours.intersection(wins))
        if your_wins_count:
            print(f"process {card_num}")
            for i in range(1, your_wins_count + 1):
                cards_to_count[i + card_num] += cards_to_count[card_num]
                print(f"adding {cards_to_count[card_num]} to {i + card_num}")
        points += cards_to_count[card_num]
    return points


if __name__ == "__main__":
    main()
