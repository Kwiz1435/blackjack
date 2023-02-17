import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self, hidden=False):
        card = self.cards.pop()
        if hidden:
            print("Dealer's hidden card")
        else:
            print(card)
        return card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        has_ace = False
        for card in self.cards:
            if card.value == 1:
                has_ace = True
            value += min(card.value, 10)
        if has_ace and value + 10 <= 21:
            value += 10
        return value

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def play(self):
        print("Welcome to Blackjack!\n")
        self.deck.shuffle()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card(hidden=True))

        print(f"Player's hand: {self.player_hand}")
        print(f"Dealer's hand: {self.dealer_hand}\n")

        if self.player_hand.get_value() == 21:
            print("Blackjack! Player wins!")
            return

        while True:
            choice = input("Would you like to hit or stand? ")
            if choice.lower() == "hit":
                self.player_hand.add_card(self.deck.deal_card())
                print(f"Player's hand: {self.player_hand}")
                if self.player_hand.get_value() > 21:
                    print("Bust! Dealer wins!")
                    return
            elif choice.lower() == "stand":
                print(f"Dealer's hand: {self.dealer_hand}")
                while self.dealer_hand.get_value() < 17:
                    self.dealer_hand.add_card(self.deck.deal_card())
                    print(f"Dealer's hand: {self.dealer_hand}")
                if self.dealer_hand.get_value() > 21:
                    print("Dealer busts! Player wins!")
                elif self.player_hand.get_value() > self.dealer_hand.get_value():
                    print("Player wins!")
                elif self.player_hand.get_value() < self.dealer_hand.get_value():
                    print("Dealer wins!")
                else:
                    print("Push! It's a tie!")
                return

game = Game()
game.play()
