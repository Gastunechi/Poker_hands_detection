def findPokerHand(hand):
    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:  # loop to get rank and suit for each card
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]

        # We associate a value to A,K,Q,J rank in order to sort them for hands detection
        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11

        ranks.append(int(rank))
        suits.append(suit)

    sortedRanks = sorted(ranks)

    # Royal Flush, Straight Flush and Flush
    if suits.count(suits[0]) == 5:  # Check for Flush
        # Royal Flush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks:
            possibleRanks.append(10)
        # Straight Flush
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)
        # Flush
        else:
            possibleRanks.append(6)

    # Straight
    if all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(5)

    handsUniqueValue = list(set(sortedRanks))
    # Four of a kind and Full House
    # 3 3 3 3 5 -- set -- 3 5 -- unique values = 2 -- Four of a kind
    # 3 3 3 5 5 -- set -- 3 5 -- unique values = 2 -- Full House
    if len(handsUniqueValue) == 2:
        for val in handsUniqueValue:
            # Four of a kind
            if sortedRanks.count(val) == 4:
                possibleRanks.append(8)
            # Full House
            elif sortedRanks.count(val) == 3:
                possibleRanks.append(7)

    # Three of a Kind and Two Pairs
    # 7 7 7 6 5 -- set -- 7 6 5 -- unique values = 3 -- Three of a kind
    # 7 7 6 6 5 -- set -- 7 6 5 -- unique values = 3 -- Two pairs
    if len(handsUniqueValue) == 3:
        for val in handsUniqueValue:
            # Three of a kind
            if sortedRanks.count(val) == 3:
                possibleRanks.append(4)
            # Two pairs
            elif sortedRanks.count(val) == 2:
                possibleRanks.append(3)

    #  One Pair
    # 7 7 8 6 5 -- set -- 7 8 6 5 -- unique values = 4 -- One pair
    if len(handsUniqueValue) == 4:
        possibleRanks.append(2)




    if not possibleRanks:
        possibleRanks.append(1)

    pokerHandsRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a kind", 7: "Full House", 6: "Flush",
                       5: "Straight", 4: "Three of a kind", 3: "Two pair", 2: "One Pair", 1: "High Card"}

    output = pokerHandsRanks[max(possibleRanks)]
    print(hand, output)
    return output


if __name__ == "__main__":
    findPokerHand(["AH", "KH", "QH", "JH", "10H"])  # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # 4 of a kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card
