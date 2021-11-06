import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# Class which creates a Card object with suit and rank
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# Deck class, creates and shuffles deck
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


if __name__ == '__main__':
    my_deck = Deck()
    print(my_deck.all_cards[0])
    my_deck.shuffle()
    print(len(my_deck.all_cards))
    print(my_deck.all_cards[0])
