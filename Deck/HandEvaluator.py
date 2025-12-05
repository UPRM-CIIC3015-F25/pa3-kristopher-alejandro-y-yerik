from Cards.Card import Card, Rank , Suit

HAND_VALUES = {
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1,
    "": 0,
}
# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]) -> str:
    ranks = []
    suits = []
    for card in hand:
        ranks.append(card.rank.value)
        suits.append(card.suit)

    rank_counts: dict[int, int] = {}
    for r in ranks:
        rank_counts[r] = rank_counts.get(r, 0) + 1

    values = sorted(rank_counts.values(), reverse=True)

    has_four = False
    has_three = False
    pair_count = 0

    for c in values:
        if c == 4:
            has_four = True
        elif c == 3:
            has_three = True
        elif c == 2:
            pair_count += 1

    has_full_house = False
    if has_three:
        if pair_count >= 1:
            has_full_house = True
        else:

            if values.count(3) >= 2:
                has_full_house = True

    suit_counts: dict[Suit, int] = {}
    for s in suits:
        suit_counts[s] = suit_counts.get(s, 0) + 1

    is_flush = False
    flush_suit = None
    for s, count in suit_counts.items():
        if count >= 5:
            is_flush = True
            flush_suit = s
            break

    def has_straight_in_values(sorted_unique_vals: list[int]) -> bool:
        if len(sorted_unique_vals) < 5:
            return False
        run = 1
        for i in range(1, len(sorted_unique_vals)):
            if sorted_unique_vals[i] == sorted_unique_vals[i - 1]:
                continue
            if sorted_unique_vals[i] == sorted_unique_vals[i - 1] + 1:
                run += 1
                if run >= 5:
                    return True
            else:
                run = 1
        return False

    unique_ranks = sorted(set(ranks))
    is_straight = has_straight_in_values(unique_ranks)

    if not is_straight and 14 in unique_ranks:
        low_ace_ranks = [1 if v == 14 else v for v in unique_ranks]
        low_ace_ranks = sorted(set(low_ace_ranks))
        is_straight = has_straight_in_values(low_ace_ranks)

    is_straight_flush = False
    if is_flush and flush_suit is not None:
        flush_ranks = []
        for card in hand:
            if card.suit == flush_suit:
                flush_ranks.append(card.rank.value)

        flush_unique = sorted(set(flush_ranks))
        is_straight_flush = has_straight_in_values(flush_unique)

        if not is_straight_flush and 14 in flush_unique:
            low_ace_flush = [1 if v == 14 else v for v in flush_unique]
            low_ace_flush = sorted(set(low_ace_flush))
            is_straight_flush = has_straight_in_values(low_ace_flush)

    if is_straight_flush:
        return "Straight Flush"
    if has_four:
        return "Four of a Kind"
    if has_full_house:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if has_three:
        return "Three of a Kind"
    if pair_count >= 2:
        return "Two Pair"
    if pair_count == 1:
        return "One Pair"
    return "High Card"