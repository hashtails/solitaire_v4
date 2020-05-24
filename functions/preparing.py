from enums import Suits, CardNumbers
from cards.card import Card
from random import shuffle
from functions.general import move_cards, turn_top_cards_face_up


def create_cards(suit):
    suit_sequence = []
    for card_number in CardNumbers:
        this_card = Card(card_number, suit)
        suit_sequence.append(this_card)
    return suit_sequence


def create_deck():
    deck = []
    for suit in Suits:
        suit_sequence = create_cards(suit)
        deck.extend(suit_sequence)
    shuffle(deck)
    return deck


def create_foundations():
    foundations = {}
    for suit in Suits:
        foundations[suit.value] = []
    return foundations


def create_tableaus():
    tableaus = []
    for tableau in range(7):
        tableaus.append([])
    return tableaus


def populate_tableaus(stock, tableaus):
    amount_of_cards = 1
    for tableau in tableaus:
        move_cards(stock, tableau, amount_of_cards)
        amount_of_cards += 1
    turn_cards_face_down(tableaus)
    turn_top_cards_face_up(tableaus)


def turn_cards_face_down(tableaus):
    for tableau in tableaus:
        for card in tableau:
            card.face_up = False











