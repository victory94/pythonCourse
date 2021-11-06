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


# Player class
# Player starts out with a name and no cards on hand
class Player:
    def __init__(self, name):
        self.list_of_cards = []
        self.name = name

    # Add either list of cards or single card
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.list_of_cards.extend(new_cards)
        else:
            self.list_of_cards.append(new_cards)

    # Remove card from top of deck
    def remove_top_card(self):
        self.list_of_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.list_of_cards)} cards.'


if __name__ == '__main__':
    my_deck = Deck()
    print(my_deck.all_cards[0])
    my_deck.shuffle()
    print(len(my_deck.all_cards))
    print(my_deck.all_cards[0])

    player_1 = Player("Player 1")
    player_1.add_cards(my_deck.deal_one())
    print(player_1)
    print(len(my_deck.all_cards))
