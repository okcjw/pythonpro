class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """A hand of playing cards."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """A deck of playing cards."""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")

class Player(Hand):
    """A player for a game."""

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
    
# Define a Blackjack card class that inherits from the Card class in the cards module
class Positionalble_Card(Card):
    ACE_VALUE = 1

    # Define a property to get the value of the card
    @property
    def value(self):
        if self.is_face_up:
            v = Positionalble_Card.RANKS.index(self.rank) + 2
            if v > 10:
                v = 10
        else:
            v = None
        return v

# Define a Blackjack deck class that inherits from the Deck class in the cards module
class BJDeck(Deck):
    # Populate the deck with Blackjack cards
    def populate(self):
        for suit in Positionalble_Card.SUITS:
            for rank in Positionalble_Card.RANKS:
                self.cards.append(Positionalble_Card(rank, suit))

# Define a Blackjack hand class that inherits from the Hand class in the cards module
class BJHand(Hand):
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    # Override the __str__ method to provide a string representation of the hand
    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    # Define a property to get the total value of the hand
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == Positionalble_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10

        return t

    # Check if the hand is busted (total value exceeding 21)
    def is_busted(self):
        return self.total > 21

# Define a Blackjack player class that inherits from the Blackjack hand class
class BJPlayer(BJHand):
    # Ask the player if they want to hit (receive another card)
    def is_hitting(self):
        response = ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    # Display a message when the player busts
    def bust(self):
        print(self.name, "busts.")
        self.lose()

    # Display a message when the player loses
    def lose(self):
        print(self.name, "loses.")

    # Display a message when the player wins
    def win(self):
        print(self.name, "wins.")

    # Display a message when the player pushes (ties with the dealer)
    def push(self):
        print(self.name, "pushes.")

# Define a Blackjack dealer class that inherits from the Blackjack hand class
class BJDealer(BJHand):
    # Determine if the dealer should hit (receive another card)
    def is_hitting(self):
        return self.total < 17

    # Display a message when the dealer busts
    def bust(self):
        print(self.name, "busts.")

    # Flip the first card of the dealer (reveal the face-down card)
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

# Define the main Blackjack game class
class BJGame(object):
    def __init__(self, names):
        # Initialize the list of players, create player objects, and initialize the dealer
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)

        self.dealer = BJDealer("Dealer")

        # Create a deck and populate it with Blackjack cards
        self.deck = BJDeck()
        self.deck.populate()

    # Property to get a list of players still playing (not busted)
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    # Deal additional cards to a player until they bust or decide to stop hitting
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    # Create a new deck, shuffle it, and deal initial cards to players and dealer
    def new_deck(self):
        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()

    # Play a round of the Blackjack game
    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # Clear the hands of players and dealer for the next round
        for player in self.players:
            player.clear()
        self.dealer.clear()

class Chip:
    type='dollar'
    amount=1

# Define the main function to start the Blackjack game
def main():
    print("\t\tWelcome to Blackjack!\n")

    # Get the number of players and their names
    names = []
    number = ask_number("How many players? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter the player name: ")
        names.append(name)

    print()

    print(names[0],end="")
    first=input(", How much will you bat($)? : ")
    
    print(names[1],end="")
    second=input(", How much will you bat($)? : ")

    # Create a Blackjack game object with the specified player names
    game = BJGame(names)

    # Play the game until the player decides to exit
    again = None
    while again != "n":
        game.play()
        game.new_deck()
        again = ask_yes_no("\nDo you want to play again?: ")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()

# Wait for user input before exiting the script
input("\n\nPress the enter key to exit.")
 
