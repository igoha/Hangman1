# hangman game
import random


counter = 8
letter_set = set()


def foo_print_word(g_word):
    print("\n" + "".join(g_word))
    return


def foo_test_word(leter):
    global counter
    if len(leter) != 1:
        print("You should input a single letter")
        return
    if leter.islower() is not True:
        print("Please enter a lowercase English letter")
        return
    if leter in letter_set:
        print("You've already guessed this letter")
        return
    if random_word.count(leter) == 0:
        print("That letter doesn't appear in the word")
        letter_set.add(leter)
        counter -= 1
        return
    else:
        foo_add_letter(leter)
    return


def foo_add_letter(leter):
    for pos, let in enumerate(random_word):
        if let == leter:
            guess_word[pos] = let
            letter_set.add(leter)
    return


def foo_menu():
    user_choise = input('Type "play" to play the game, "exit" to quit: ')
    return user_choise


print("H A N G M A N")
while True:
    user_choise = foo_menu()
    if user_choise == "exit":
        break
    elif user_choise == "play":
        random.seed()
        word_list = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(word_list)  # random word from word_list
        guess_word = list((len(random_word) * "-"))
        while counter > 0:
            foo_print_word(guess_word)
            letter = input("Input a letter: ")
            foo_test_word(letter)
            test_word = "".join(guess_word)
            if test_word == random_word:
                print('''You guessed the word!
You survived!
''')
                break
        if test_word != random_word:
            print("You lost!\n")
