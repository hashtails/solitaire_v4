from cards.card import Card
from cards.foundation import Foundation
from functions.general import empty, following_number, move_cards, top_card
from enums import CardNumbers


def move_to_foundations(origin: list, foundations: dict):
    if foundation_accepts(origin, foundations):
        foundations[origin[-1].suit.value].append(origin.pop())
    else:
        print('Unable to move to foundations')


def foundation_accepts(origin: list, foundations: dict):
    card = top_card(origin)
    foundation = foundations[origin[-1].suit.value]
    if empty(foundation) and card.number.name == 'ACE':
        return True
    elif not empty(foundation) and card.number_index() == top_card(foundation).number_index() + 1:
        return True
    else:
        return False
