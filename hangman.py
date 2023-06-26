#importing random and creating word list variable and a random chosen word variable
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Testing code
print(f'Pssst, the solution is {chosen_word}.')



#Creating blanks for display
display = []

for letter in chosen_word:
    display.append("_")


print(stages[lives])
print(f"{' '.join(display)}")

#While loop to keep the user guessing until completed
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # checks if the  user guessedright and switches the blank with the letter if it was correct
    i = 0
    for letter in chosen_word:
        if letter == guess:
            display[i] = guess

        i += 1

    #Checks if guess was wrong and detreacts from their life score if so.
    if guess not in chosen_word:
        lives -= 1
        # Checks if user still has life if not game over
        if lives == 0:
            end_of_game = True
            print("You lose, loser.")



    # prints the display list variable as a string
    print(f"{' '.join(display)}")


    # checks if user has guessed all the blanks and if so wins
    if "_" not in display:
        end_of_game = True
        print("You've won.")

    print(stages[lives])