from cards.card import Card
from enums import CardNumbers
from cards.foundation import Foundation


def empty(pile_of_cards: list):
    if len(pile_of_cards) < 1:
        return True
    else:
        return False


def top_card(pile_of_cards: list):
    if len(pile_of_cards) > 0:
        return pile_of_cards[-1]
    else:
        return ' '


def oposite_color(card_1: Card, card_2: Card):
    if card_1.is_red != card_2.is_red:
        return True


def turn_top_cards_face_up(tableaus: list):
    for tableau in tableaus:
        tableau[-1].face_up = True


def draw_a_card(stock, waste):
    if not empty(stock):
        this_card = stock.pop()
        waste.append(this_card)
    else:
        reset_stock(stock, waste)


def reset_stock(stock, waste):
    cards_in_waste = len(waste)
    for _ in range(cards_in_waste):
        this_card = waste.pop()
        stock.append(this_card)


def move_cards(origin: list, destiny: list, quantity: int):
    cards = []
    for card in range(quantity):
        cards.append(origin.pop())
    destiny.extend(reversed(cards))


def following_number(higher_card: Card, lower_card: Card):
    if higher_card.number_index() == lower_card.number_index() - 1:
        return True


