"""Functions of Game Hangman"""
import os


def cls():
    """Clears the console"""

    os.system('cls' if os.name == 'nt' else 'clear')


def save_word(word):
    """Saves a word to the history"""

    with open('word_history.txt', 'a') as the_file:
        the_file.write(word + '\n')


def make_guess(guess, word, guess_word):
    """Check if guessing letter is in word
    if yes - find all coincidences and replace '_' with the letters

    if not - add guessing letter to misses and reduce the lives

    returns True/False guessing letter in the word
    """

    if guess in word:
        coincidence = [i for i, letter in enumerate(word) if letter == guess]
        for index in coincidence:
            guess_word[index] = word[index]
        return True
    return False


def check_guess(guess, guess_word, misses):
    """Returns if guess letter has already been entered"""

    return guess in guess_word or guess in misses


def check_victory(guess_word):
    """Returns if there's more '_' in guessing word"""
    return '_' in guess_word


def print_status(guess_word, lives, misses):
    """Prints current state of game: guessed word, amount of lives, missed letters"""

    print(f'\nWord: {" ".join(guess_word)}')
    print(f'Lives: {lives}')
    print(f'Misses: {" ".join(misses)}\n')


def new_game():
    """Defines the process of new game
    1. Saves the word to file
    2. Defines: the number of lives, guess word with '_', list of missed letters
    3. Loop until you have lives
        3.1 print status
        3.2 enter guess letter
        3.3 check letter
        3.4 edit guessed word
        3.5 check victory
    """

    word = input('Set the word first: ')
    save_word(word)
    cls()
    guess_word = ['_'] * len(word)
    lives = 7
    misses = []
    while lives:
        print_status(guess_word, lives, misses)
        guess = str(input('Enter the letter: '))
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess, guess_word, misses):
                print('Letter has already been entered')
                continue
            if not make_guess(guess, word, guess_word):
                misses += guess
                lives -= 1
            if not check_victory(guess_word):
                print('\nYou WON!!!')
                break
        else:
            print('Wrong value. Try again')
    if lives == 0:
        print('\nYou LOST :(')


def word_history():
    """Print words history"""

    with open('word_history.txt', 'r') as the_file:
        print(''.join(the_file.readlines()))


def main_menu():
    """Prints main menu with choices"""

    while True:
        print('\n-------------------')
        print('1 - New Game')
        print('2 - Words History')
        print('3 - Exit')
        print('-------------------\n')

        choice = int(input('Enter the number: '))

        if choice == 1:
            new_game()
        elif choice == 2:
            word_history()
        elif choice == 3:
            break
        else:
            print('Wrong value. Try again')


if __name__ == '__main__':
    cls()
    print('Welcome to Hangman!')
    main_menu()
    print('Bye! Thanks for playing')
