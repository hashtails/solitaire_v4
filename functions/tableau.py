from cards.card import Card
from enums import CardNumbers
from functions.general import empty, oposite_color


def tableau_accepts_card(card: Card, tableau: list):
    if card.number == CardNumbers.KING and empty(tableau):
        return True
    elif oposite_color(card, tableau[-1]) and card.number_index() < tableau[-1].number_index():
        return True


def enough_cards_face_up(tableau: list, number: int):
    max_number = 0
    for card in tableau:
        if card.face_up:
            max_number += 1
    if max_number <= number:
        return True
