
print("welcome to Day 7")
import random
import hangman_words

placeholder = ""
chances = 6 
game_over = False
unique_word = random.choice(hangman_words.random_things)
prev_char = []

for char in range(len(unique_word)):
    placeholder += "-"

print(placeholder)

while not game_over:
    guess_alphabet = input("guess an alphabet: ").lower()
    display = ""

    for letter in unique_word:
        if letter == guess_alphabet:
            display += letter
            prev_char.append(letter)
        elif letter in prev_char:
            display += letter
        else:
            display += "_"

    if guess_alphabet not in display:
        chances -= 1

    if "_" not in display:
        game_over = True
        print("you win!")
    elif chances == 0:
        game_over = True
        print(f"You Lose!\nthe correct work is: {unique_word}")

    print(display)
    print(f"Number Of Live Left: {chances}")


