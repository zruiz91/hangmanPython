#Step 1
import random


word_list = ["aardvark", "baboon", "camel"]

#TODo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")