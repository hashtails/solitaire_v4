from enums import Suits, CardNumbers, formatted_card, formatted_blank


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.face_up = True
        self.is_red = False
        if self.suit == Suits.HEARTS or self.suit == Suits.DIAMONDS:
            self.is_red = True

    def __str__(self):
        if not self.face_up:
            return formatted_blank('-')
        else:
            return formatted_card(self)

    def __repr__(self):
        return formatted_card(self)

    def number_index(self):
        return list(CardNumbers).index(self.number)






























