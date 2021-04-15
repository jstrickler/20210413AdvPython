import random



class Card:
    def __init__(self, rank, suit):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    # how to create the object in code
    def __repr__(self):
        return f'Card("{self.rank}","{self.suit}")'

class CardDeck:  # inherit from 'object'
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer # call setter prop
        self._color = 'blue'
        self._animal = None
        self._make_deck()
        # C++/Java/C#
        # this.dealer = dealer

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


    # # getter (AKA accessor)
    # def get_dealer(self):
    #     return self._dealer
    #
    # # setter (AKA mutator)
    # def set_dealer(self, dealer):
    #     self._dealer = dealer

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")
        self._code = 'abc'

    @property
    def beast(self):
        return

    @beast.setter
    def beast(self, value):
        pass

    @property
    def real_name(self):
        return self._real_name

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def bark():
        print("Woof!")

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}('{self.dealer}')"

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer} {len(self)})"

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp
