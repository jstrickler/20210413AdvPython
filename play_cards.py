"""
Play a game of cards.

Uses the CardDeck and JokerDeck classes.

No strategy implemented (yet).
"""
from carddeck import CardDeck
from jokerdeck import JokerDeck

def main():
    """
    Program entry point

    :return: None
    """
    print(CardDeck)
    card_deck_1 = CardDeck('Matilda')
    print(type(card_deck_1))

    # print(card_deck_1._dealer)  # DO NOT DO THIS

    # print(card_deck_1.get_dealer())
    #
    # x = CardDeck.get_dealer(card_deck_1)
    #
    # card_deck_1.set_dealer("Ferdinand")

    print(card_deck_1.dealer) # calls property method
    card_deck_1.dealer = "Alice"

    print(card_deck_1.dealer)

    # INSTANCE.method(p1, p2, ...)
    # becomes
    # CLASS.method(INSTANCE, p1, p2...)
    card_deck_2 = CardDeck('Ellen')
    # print(card_deck_2.get_dealer())
    print(card_deck_2.dealer)
    card_deck_2.dealer = 'Lex Luthor'

    try:
        card_deck_2.dealer = 12.2343
    except TypeError as err:
        print(err)
    else:
        print(card_deck_2)

    try:
        card_deck_3 = CardDeck(8.9)
    except TypeError as err:
        print(err)
    else:
        print(card_deck_3)
        print(card_deck_3.dealer)

    print(CardDeck.SUITS[0])
    print(card_deck_1.SUITS[0])

    card_deck_1.shuffle()
    print(card_deck_1.cards, '\n')
    card_deck_2.shuffle()

    for _ in range(5):
        card = card_deck_1.draw()
        print(card.rank, card.suit)
    print()

    suits = card_deck_1.get_suits()
    print(suits)

    print(CardDeck.get_suits())

    CardDeck.bark()
    card_deck_1.bark()

    joker_deck_1 = JokerDeck("Jerry")
    print(joker_deck_1)
    joker_deck_1.shuffle()
    print(joker_deck_1.cards)

    print(CardDeck.mro())
    print(JokerDeck.mro())

    print(len(card_deck_1))
    print(len(joker_deck_1))
    print(card_deck_1)
    print(card_deck_2)
    print(joker_deck_1)
    print(repr(joker_deck_1))

    joker_deck_1.how_to_play()
    print(JokerDeck.mro())

    result = card_deck_1 + joker_deck_1
    print(result)

if __name__ == '__main__':
    main()

