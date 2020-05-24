from enums import Suits, formatted_blank


def print_board(stock: list, waste: list, foundations: dict, tableaus: list):
    stock = str(len(stock))
    waste = top_card(waste)
    hearts_f = top_card(foundations[Suits.HEARTS.value])
    spades_f = top_card(foundations[Suits.SPADES.value])
    clubs_f = top_card(foundations[Suits.CLUBS.value])
    diamonds_f = top_card(foundations[Suits.DIAMONDS.value])
    board_size = longest_tableau(tableaus)

    print_break_line()
    print_top_row(stock, waste, hearts_f, spades_f, clubs_f, diamonds_f)
    print_tableaus(tableaus, board_size)
    fill_spaces(board_size, 10)


def print_break_line():
    print('\n\n**********************************************')


def fill_spaces(board_size, desirable_size: int):
    for used_spaces in range(desirable_size - board_size):
        print('\n')


def print_top_row(stock, waste, hearts_f, spades_f, clubs_f, diamonds_f):
    print('{0:5s}{1:20s}{2:10s}{3:10s}{4:10s}{5:s}\n'.format(('(' + stock + ')'), waste,
                                                             hearts_f, spades_f, clubs_f, diamonds_f))


def print_tableaus(tableaus, board_size):
    for row in range(board_size):
        this_row = []
        make_row(tableaus, row, this_row)
        print_tableaus_row(this_row)


def append_card_or_blank(tableaus, column, row, this_row):
    try:
        this_row.append(str(tableaus[column][row]))
    except IndexError:
        this_row.append(formatted_blank(' '))


def make_row(tableaus, row, this_row):
    for column in (range(7)):
        append_card_or_blank(tableaus, column, row, this_row)


def print_tableaus_row(this_row):
    print('{0:15s}{1:15s}{2:15s}{3:15s}{4:15s}{5:15s}{6:s}'.format(this_row[0], this_row[1], this_row[2], this_row[3],
                                                                   this_row[4], this_row[5], this_row[6], ))


def top_card(pile_of_cards: list):
    if len(pile_of_cards) > 0:
        return str(pile_of_cards[-1])
    else:
        return ' '


def longest_tableau(tableaus: list):
    size = 0
    for tableau in tableaus:
        if len(tableau) > size:
            size += len(tableau)
    return size


def get_foundation(foundations: list, suit: Suits):
    return next((foundation for foundation in foundations if foundation.suit == suit))
