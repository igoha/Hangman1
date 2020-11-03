import random


random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
r_word = random.choice(word_list)  # random worl from word_list
g_word = r_word[0:3] + "-" * (len(r_word) - 3)  # generated word first 3 letter from r_wordl + "-"
word = input(f"Guess the word {g_word}: ")
if word == r_word:
    print("You survived!")
else:
    print("You lost!")
