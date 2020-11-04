# hangman game
import random

letters = set()
random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)  # random word from word_list
# g_word = r_word[0:3] + "-" * (len(r_word) - 3)  # generated word first 3 letter from r_word + "-"
print("H A N G M A N")
