class Card:
    cards: str
    bid: int

    def __init__(self, hand, bid):
        self.cards = hand
        self.bid = bid


def sort_hands(hands):
    for hand in hands:
        cards = list(hand.cards)
        for i in range(len(cards)):
            if cards[i] == "T":
                cards[i] = "10"
            if cards[i] == "J":
                cards[i] = "0"
            elif cards[i] == "Q":
                cards[i] = "12"
            elif cards[i] == "K":
                cards[i] = "13"
            elif cards[i] == "A":
                cards[i] = "14"
        hand.cards = cards

    hands = sorted(hands, key=lambda x : (-int(x.cards[0]), -int(x.cards[1]), -int(x.cards[2]), -int(x.cards[3]), -int(x.cards[4])))
    return hands


def main():
    hands = []
    with open("input7.txt") as f:
        line = f.readline()
        while line:
            line = line.split()
            hand = Card(line[0], line[1])
            hands.append(hand)
            line = f.readline()

    five_of_kind = []
    four_of_kind = []
    three_of_kind = []
    two_pair = []
    one_pair = []
    full_house = []
    highest_card = []
    for hand in hands:
        cards = list(hand.cards)
        counts = [0] * 14
        for card in cards:
            if card == "T":
                card = "10"
            if card == "J":
                card = "11"
            elif card == "Q":
                card = "12"
            elif card == "K":
                card = "13"
            elif card == "A":
                card = "14"
            counts[int(card)-1] += 1

        j_count = counts[10]
        counts[10] = 0
        counts = sorted(counts, reverse=True)
        counts[0] += j_count
        if counts[0] == 5:
            five_of_kind.append(hand)
        elif counts[0] == 4:
            four_of_kind.append(hand)
        elif counts[0] == 3 and counts[1] == 2:
            full_house.append(hand)
        elif counts[0] == 3:
            three_of_kind.append(hand)
        elif counts[0] == 2 and counts[1] == 2:
            two_pair.append(hand)
        elif counts[0] == 2:
            one_pair.append(hand)
        else:
            highest_card.append(hand)

    if len(five_of_kind) > 1:
        five_of_kind = sort_hands(five_of_kind)
    if len(four_of_kind) > 1:
        four_of_kind = sort_hands(four_of_kind)
    if len(full_house) > 1:
        full_house = sort_hands(full_house)
    if len(three_of_kind) > 1:
        three_of_kind = sort_hands(three_of_kind)
    if len(two_pair) > 1:
        two_pair = sort_hands(two_pair)
    if len(one_pair) > 1:
        one_pair = sort_hands(one_pair)
    if len(highest_card) > 1:
        highest_card = sort_hands(highest_card)

    final_rank = []
    final_rank.extend(five_of_kind)
    final_rank.extend(four_of_kind)
    final_rank.extend(full_house)
    final_rank.extend(three_of_kind)
    final_rank.extend(two_pair)
    final_rank.extend(one_pair)
    final_rank.extend(highest_card)

    final_rank.reverse()

    total = 0
    for i in range(len(final_rank)):
        hand = final_rank[i]
        total += int(hand.bid) * (i + 1)

    print(total)


main()