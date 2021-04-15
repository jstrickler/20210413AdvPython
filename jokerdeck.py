from carddeck import CardDeck, Card

class Game:
    def how_to_play(self):
        print("How to play...")

class JokerDeck(Game, CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call in CardDeck
        for joker_num in "1", "2":
            card = Card(joker_num, 'Joker')
            self._cards.append(card)

