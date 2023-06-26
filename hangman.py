#importing random and creating word list variable and a random chosen word variable
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')



#Creating blanks for display
display = []

for letter in chosen_word:
    display.append("_")


print(display)

#While loop to keep the user guessing until completed
while "_" in display:
    guess = input("Guess a letter: ").lower()


    i = 0
    for letter in chosen_word:
        if letter == guess:
            display[i] = guess

        i += 1


    print(display)