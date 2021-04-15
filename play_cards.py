
from carddeck import CardDeck
from jokerdeck import JokerDeck

print(CardDeck)
d1 = CardDeck('Matilda')
print(type(d1))

# print(d1._dealer)  # DO NOT DO THIS

# print(d1.get_dealer())
#
# x = CardDeck.get_dealer(d1)
#
# d1.set_dealer("Ferdinand")

print(d1.dealer) # calls property method
d1.dealer = "Alice"

print(d1.dealer)

# INSTANCE.method(p1, p2, ...)
# becomes
# CLASS.method(INSTANCE, p1, p2...)
d2 = CardDeck('Ellen')
# print(d2.get_dealer())
print(d2.dealer)
d2.dealer = 'Lex Luthor'

try:
    d2.dealer = 12.2343
except TypeError as err:
    print(err)
else:
    print(d2)

try:
    d3 = CardDeck(8.9)
except TypeError as err:
    print(err)
else:
    print(d3)
    print(d3.dealer)

print(CardDeck.SUITS[0])
print(d1.SUITS[0])

d1.shuffle()
print(d1.cards, '\n')
d2.shuffle()

for i in range(5):
    card = d1.draw()
    print(card.rank, card.suit)
print()

suits = d1.get_suits()
print(suits)

print(CardDeck.get_suits())

CardDeck.bark()
d1.bark()

j1 = JokerDeck("Jerry")
print(j1)
j1.shuffle()
print(j1.cards)

print(CardDeck.mro())
print(JokerDeck.mro())

print(len(d1))
print(len(j1))
print(d1)
print(d2)
print(j1)
print(repr(j1))

j1.how_to_play()
print(JokerDeck.mro())

result = d1 + j1
print(result)



