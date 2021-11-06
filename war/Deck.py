import Card


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    # Shuffles deck of cards
    def shuffle(self):
        return random.shuffle(self.all_cards)

    # Takes out card from top of deck
    def deal_one(self):
        return self.all_cards.pop()
