from enum import Enum
from colorama import Fore, Style


class Suits(Enum):
    HEARTS = '♥'
    SPADES = '♠'
    CLUBS = '♣'
    DIAMONDS = '♦'


class CardNumbers(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'


def formatted_card(card):
    if card.suit == Suits.HEARTS or card.suit == Suits.DIAMONDS:
        return f'{card.number.value}{Fore.RED}{card.suit.value}{Style.RESET_ALL}'
    else:
        return f'{card.number.value}{Fore.BLACK}{card.suit.value}{Style.RESET_ALL}'


def formatted_blank(blank):
    return f'{Fore.BLACK}{blank}{Style.RESET_ALL}'
