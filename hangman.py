import random


random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
word = input("Guess the word: ")
r_word = random.choice(word_list)
if word == r_word:
    print("You survived!")
else:
    print("You lost!")
