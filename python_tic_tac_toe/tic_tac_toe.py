"""Module for game Tic-tac-toe"""
import random
import logging


logging.basicConfig(
    level=logging.INFO,
    filename='win.log',
    format='%(asctime)s - %(message)s',
)


class Board:
    """Class representing a board of the game"""

    __win_coord = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    def __init__(self):
        """Constructor"""
        self.board = [*range(1, 10)]
        print(self.board)

    def _print_board(self):
        """Printing the board of game"""
        print('-------------')
        for i in range(3):
            print("|", self.board[0 + i * 3],
                  "|", self.board[1 + i * 3],
                  "|", self.board[2 + i * 3],
                  "|")
            print("-------------")

    def __check_cell(self, number):
        """Returns if the cell is empty"""
        return number in self.board

    def _make_move(self, number, character):
        """Function for making move in game"""
        while not self.__check_cell(number):
            print('Sorry, the cell is occupied.')
            number = int(input('Try again -> '))
        self.board[number - 1] = character
        self._print_board()

    def _check_victory(self):
        """Returns if board is in winning state"""
        for each in self.__win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def _reset_board(self):
        """Clears the board"""
        self.board = [*range(1, 10)]


class Player:
    """Class representing a player of game"""

    def __init__(self, character, name):
        """Constructor"""
        self.name = name
        self.character = character


class PlayProcess(Board):
    """Class representing the process of the game"""

    def __init__(self):
        Board.__init__(self)
        self.score = [0, 0]
        self.pl1 = None
        self.pl2 = None

    def __create_players(self):
        """Creates players"""
        pl1_name = input('Enter the X-player name -> ')
        pl2_name = input('Enter the O-player name -> ')
        self.pl1 = Player('X', pl1_name)
        self.pl2 = Player('O', pl2_name)

    def __move_process(self, player):
        """Takes the players move and calls the board make_move function"""
        print(f'{player.name}, to put your {player.character}?')
        move = int(input('Enter the number of cell -> '))
        self._make_move(move, player.character)

    def play(self):
        """Calls the creation of players and prints the board"""
        self.__create_players()
        logging.info('=====%s vs %s=====', self.pl1.name, self.pl2.name)
        self._print_board()
        self.__play_process()

    def __play_again(self):
        """Clears the board and prints it"""
        self._reset_board()
        self._print_board()
        self.__play_process()

    def __log_score(self, current_pl):
        """Writes the log info about the score"""
        if current_pl is self.pl1:
            self.score[0] += 1
            logging.info('Score: %s:%s.', self.score[0], self.score[1])
        else:
            self.score[1] += 1
            logging.info('Score: %s:%s.', self.score[0], self.score[1])

    def __play_process(self):
        """Defines the process of a game"""
        if random.randint(1, 2) == 1:
            print(f'{self.pl1.name} starts')
            current_pl = self.pl2
        else:
            print(f'{self.pl2.name} starts')
            current_pl = self.pl1

        while not self._check_victory():
            if not [i for i in self.board if isinstance(i, int)]:
                print('Draw!')
                logging.info('Draw')
                logging.info('Score: %s:%s.', self.score[0], self.score[1])
                break
            if current_pl == self.pl1:
                current_pl = self.pl2
            else:
                current_pl = self.pl1
            self.__move_process(current_pl)
        else:
            print(f'{current_pl.name} WON with {current_pl.character}!')
            logging.info('%s wins.', current_pl.name)
            self.__log_score(current_pl)

        choice = input('Play again? Y/N -> ')
        if choice in ('Y', 'y'):
            self.__play_again()


class Menu:
    """Class representing main aspects of the game tic-tac-toe"""

    def main_menu(self):
        """Prints main menu"""
        print('------------------------',
              '1 - Play',
              '2 - Victory logs',
              '3 - Clear victory logs',
              '4 - Exit',
              '------------------------\n', sep='\n')
        choice = input('Enter the number -> ')
        self.__define_choices(choice)

    @staticmethod
    def print_log():
        """Prints file with log victories"""
        print('Log:')
        with open('win.log') as file:
            for line in file:
                print(line.strip())

    @staticmethod
    def clear_log():
        """Clears file with log victories"""
        with open('win.log', 'w'):
            pass

    def __define_choices(self, choice):
        """Calls the chosen functions"""
        if choice == '1':
            new_game = PlayProcess()
            new_game.play()
        elif choice == '2':
            self.print_log()
            self.main_menu()
        elif choice == '3':
            self.clear_log()
            self.main_menu()
        elif choice == '4':
            print('Goodbye!')


if __name__ == '__main__':
    print('Welcome to Tic-Tac-Toe!\n')
    test = Menu()
    test.main_menu()
