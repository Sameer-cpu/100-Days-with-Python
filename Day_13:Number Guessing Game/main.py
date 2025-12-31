print("welcome to Day 13")
from random import randint


#Function to check the user guess against the actual answer

#Chooose a random number between 1 to 100
print("Welcome to Number guessing game")
answer = randint(1,100)
print(answer)

#let the user guess the number
guess = int(input("guess a  number between 1 - 100"))


def check_answer(user_guess, rand_num):
    if user_guess > answer:
        print("too high")   
    elif user_guess < answer:
        print( "too low")
    else:
        print(f"you Got it, The actual answer was {rand_num}")


check_answer(guess,10)