# hangman game
import random


def foo_print_word(g_word):
    print("\n" + g_word)
    return

letters = set()
random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)  # random word from word_list
# g_word = r_word[0:3] + "-" * (len(r_word) - 3)  # generated word first 3 letter from r_word + "-"
guess_word = (len(random_word) * "-")
print("H A N G M A N")
for _ in range(8):
    foo_print_word(guess_word)
    letter = input("Input a letter: ")
