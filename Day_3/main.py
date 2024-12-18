# num = int(input("add a number: \n"))
#
# if(num % 2 == 0):
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")
#from random import choice

# weight = 85
# height = 1.85
#
# bmi = round(weight / (height ** 2))
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi >= round(18.5) & bmi < 25.1:
#     print("normal weight")
# else:
#     print("overweight")

# print("Welcome to the rollercoaster!")
# user_height = int(input("What is your height in cm? "))
# bill = 0
# if user_height >= 120 :
#     print("You can ride the rollercoaster")
#     age = int(input("What is your Age: "))
#     if age <= 12 :
#         bill = 5
#         print(f"Child tickets are ${bill}.")
#     elif age <= 18:
#         bill = 7
#         print(F"Youth tickets are ${bill}.")
#     else:
#         bill = 12
#         print(f"Adult tickets are ${bill}.")
#
#
#     want_photo = input("Dou you want to have a photo? Type \"y/Y\" for \"Yes\" and \"n/N\" for \"No\": ")
#     if want_photo == "y" or want_photo == "Y":
#         bill += 3
#         print(f"Your total bill is ${bill}")
#
# else:
#     print("Sorry you have to grow taller before riding the rollercoaster.")

# print("Welcome to Python Pizza Deliveries.!")
# size = input("What size of Pizza do you want? S, M or L: ")
# pepperoni = input("Do you want \"Pepperoni\" on your Pizza? Y or N: ")
# extra_cheese = input("Do you want \"Extra Cheese\" on your Pizza? Y or N: ")
#
# price = 0
#
# if size == "s" or size == "S":
#     price += 15
# elif size == "m" or size == "M":
#     price += 20
# else:
#     price += 25
#
# if pepperoni == "y" or pepperoni == "Y":
#     if size == "s" or size == "S":
#         price += 2
#     else:
#         price += 3
#
# if extra_cheese == "y" or extra_cheese == "Y":
#     price += 1
#
# print(f"your total bill is ${price}")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island.!")
print("your mission is to find treasure")
choice_one = input('you\'re at the crossroad, where you do you go? type "left" or "right" ').lower()

if choice_one == "left":
    choice_two = input("You're come to the lake, "
                       "there is an island in the middle of the lake. "
                       "Type \"wait\" for wait for a boat. Type \"swim\" to swim across ").lower()
    if choice_two == "wait":
        choice_three = input("You arrived aat the island unharmed. "
                             "there is a house with three doors. "
                             "One is red, one yellow, and one blue. "
                             "Which door do you choose? ").lower()
        if choice_three == "yellow":
            print("\nYou found the treasure. You Win.!")
        elif choice_three == "red":
            print("\nit's a room full of fire. Game Over.")
        elif choice_three == "red":
            print("\nyou enter a room oof beast. Game Over.")
        else:
            print("\nYou choose a door that doesn't exist. Game Over")
    else:
        print("\nAttacked by trout. Game Over.")
else:
    print("\nYou fell into a hole! Game Over")