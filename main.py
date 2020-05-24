from match import Match
from runner.runner import Runner


#  - draw card etc


class Main:
    def __init__(self):
        self.runner = Runner()

    def run_game(self):
        self.runner.run()


if __name__ == '__main__':
    main_game = Main()
    main_game.run_game()

# for turns in range(100):
#     main_game.match.print_board()
#     action = input('(D)raw or (M)ove card: ').upper()  ###
#     if action == 'D':
#         main_game.match.stock.draw_card()
#
#     elif action == 'M':
#         action = input('From (W)aste, (T)ableaus or (F)oundations? ').upper()
#         if action == 'W':
#             if not match.waste.is_empty():
#                 action = input('To (T)ableaus or (F)oundations? ').upper()
#                 if action == 'T':
#                     answer = int(input('Wich one (1 - 7)? ')) - 1
#                     if match.tableaus[answer].check_acceptance(match.waste.top()):
#                         match.waste.move_single(match.tableaus[answer])
#                     else:
#                         input('This tableau can\'t accept this card. (press enter)')
#                 elif action == 'F':
#                     match.move_to_foundation(match(), match.waste)
#
#                 else:
#                     print('Answer not expected')
#             else:
#                 input('Wast pile is empty. (press enter)')
#         elif action == 'T':
#             origin = int(input('From wich one? (type number) '))
#             if match.tableaus[origin].is_empty():
#                 input('Tableau is empty.')
#             else:
#                 quantity = int(input('How many cards? '))
#                 if quantity > len(match.tableaus[origin].pool):
#                     input('There is not enough cards in the tableau.')
#                 else:
#                     target = int(input('To wich tableau? (type number) '))
#                     if match.tableaus[target].check_acceptance(match.tableaus[origin][-quantity]):  # !!!!!!
#                         hand = []
#                         for card in range(quantity):
#                             hand.append(match.tableaus[origin].pool.pop())
#                         for card in range(quantity):
#                             match.tableaus[target].pool.append(hand.pop())
#
#
#
#         elif action == 'F':
#             print('Moving from foundations not implemented yet')
#     else:
#         print('Unknown command.')
#
# # separa essa porra em fases.py
