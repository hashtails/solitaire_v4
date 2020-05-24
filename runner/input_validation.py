def validate_answer(player_input, valid_keys):
    if validate_int(player_input):
        player_input = int(player_input)
    if answer_inside_valid_keys(player_input, valid_keys):
        return player_input
    else:
        error_msg()


def validate_int(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False


def answer_inside_valid_keys(player_input, valid_keys: list):
    if player_input in valid_keys:
        return True
    else:
        return False


def error_msg():
    print('Invalid answer')
