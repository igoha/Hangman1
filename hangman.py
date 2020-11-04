# hangman game
import random


def foo_print_word(g_word):
    print("\n" + "".join(g_word))
    return


def foo_test_word(letter):
    if random_word.count(letter) == 0:
        print("That letter doesn't appear in the word")
        return
    foo_add_letter(letter)
    return


def foo_add_letter(letter):
    for pos, let in enumerate(random_word):
        if let == letter:
            guess_word[pos] = let
    return


random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)  # random word from word_list
guess_word = list((len(random_word) * "-"))
print("H A N G M A N")
for _ in range(8):
    foo_print_word(guess_word)
    letter = input("Input a letter: ")
    foo_test_word(letter)
print('''
Thanks for playing!
We'll see how well you did in the next stage''')
