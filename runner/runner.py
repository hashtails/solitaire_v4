from runner import action
from match import Match
from printer import print_board
from functions.general import draw_a_card, move_cards, empty, turn_top_cards_face_up
from functions.tableau import tableau_accepts_card
from functions.foundation import move_to_foundations


class Runner:
    def __init__(self):
        self.match = Match()
        for _ in range(100):
            self.run()

    def run(self):
        self.refresh_board()
        answer = action.draw_or_move()
        if answer == 'D':
            draw_a_card(self.match.stock, self.match.waste)
        elif answer == 'M':
            self.move_from()

    def move_from(self):
        answer = action.move_from()
        if answer == 'W' and not empty(self.match.waste):
            self.move_from_waste()
        elif answer == 'T':
            self.move_from_tableau()
        elif answer == 'F':
            print('f')
        else:
            print('can\'t')

    def move_from_waste(self):
        answer = action.move_to()
        if answer == 'T':
            self.move_to_tableau(self.match.waste)

        elif answer == 'F':
            move_to_foundations(self.match.waste, self.match.foundations)

    def move_from_foundation(self):
        index = action.which_foundation()
        self.move_to_tableau(self.match.foundations[index])

    def move_from_tableau(self):
        origin_index = action.which_tableau()
        if not empty(self.match.tableaus[origin_index]):
            destiny = action.move_to()
            if destiny == 'T':
                self.tableau_to_tableau(origin_index)
            if destiny == 'F':
                move_to_foundations(self.match.tableaus[origin_index], self.match.foundations)
        else:
            self.error_msg()

    def tableau_to_tableau(self, origin_index):
        destiny = action.which_tableau()
        quantity = action.how_many()
        valid_keys = action.set_range(1, 13)
        quantity = action.validate_answer(quantity, valid_keys)
        move_cards(self.match.tableaus[origin_index], self.match.tableaus[destiny], quantity)

    def move_to_tableau(self, origin, quantity=1):
        tableau = action.which_tableau()
        if tableau_accepts_card(origin[-1], self.match.tableaus[tableau]):
            move_cards(origin, self.match.tableaus[tableau], quantity)
        else:
            self.error_msg()

    def refresh_board(self):
        turn_top_cards_face_up(self.match.tableaus)
        print_board(self.match.stock, self.match.waste, self.match.foundations, self.match.tableaus)

    @staticmethod
    def error_msg():
        print('\n\nImpossibru')

