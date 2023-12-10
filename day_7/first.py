from collections import Counter

STRENGTH = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    _power = None

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @property
    def power(self):
        if self._power is not None:
            return self._power

        card_to_count = Counter()
        for card in self.cards:
            card_to_count[STRENGTH[card]] += 1
        values = set(card_to_count.values())
        counts = list(card_to_count.values())

        # get card with given count

        if 5 in values:
            self._power = 7
        elif 4 in values:
            self._power = 6
        elif 3 in values and 2 in values:
            self._power = 5
        elif 3 in values:
            self._power = 4
        elif counts.count(2) == 2:
            self._power = 3
        elif 2 in values:
            self._power = 2
        else:
            self._power = 1
        return self._power

    def __lt__(self, other):
        if self.power == other.power:
            for i, card in enumerate(self.cards):
                if card == other.cards[i]:
                    continue
                else:
                    return STRENGTH[card] < STRENGTH[other.cards[i]]
        return self.power < other.power

    def __str__(self):
        return f"{self.cards} {self.power} {self.bid}"

    def __repr__(self):
        return self.__str__()


def main():
    hands = [
        Hand(x, int(y))
        for x, y in [
            line.split() for line in open("input.txt").read().split("\n")
        ]
    ]
    result = 0
    for i, hand in enumerate(sorted(hands)):
        result += (i + 1) * hand.bid
    return result


if __name__ == "__main__":
    main()
