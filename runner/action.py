from runner.input_validation import validate_int, validate_answer


def draw_or_move():
    valid_keys = ['D', 'M']
    answer = input('(D)raw or (M)ove card: ').upper()
    return validate_answer(answer, valid_keys)


def move_from():
    valid_keys = ['W', 'T', 'F']
    answer = input('From (W)aste, (T)ableaus or (F)oundations? ').upper()
    return validate_answer(answer, valid_keys)


def move_to():
    valid_keys = ['T', 'F']
    answer = input('To (T)ableaus or (F)oundations? ').upper()
    return validate_answer(answer, valid_keys)


def which_tableau():
    valid_keys = set_range(1, 8)
    answer = input('Which one (1 - 7)? ')
    return validate_answer(answer, valid_keys)


def which_foundation():
    valid_keys = set_range(1, 4)
    answer = input('Which one (1 - 4)? ')
    return validate_answer(answer, valid_keys)


def how_many():
    valid_keys = set_range(1, 14)
    answer = input('How many cards? ')
    return validate_answer(answer, valid_keys)


def set_range(_from, _to):
    response = []
    for number in range(_from, _to):
        response.append(number)
    return response
