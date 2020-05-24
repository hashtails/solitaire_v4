from functions.general import draw_a_card
from functions.preparing import create_foundations, create_deck, create_tableaus, populate_tableaus


class Match:
    def __init__(self):
        self.stock = create_deck()
        self.foundations = create_foundations()
        self.tableaus = create_tableaus()
        self.waste = []
        self.score = 0
        populate_tableaus(self.stock, self.tableaus)
        draw_a_card(self.stock, self.waste)





