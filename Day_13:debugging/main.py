print("welcome to Day 13: Debugging")

# def my_function():
#     for i in range(1,20):
#         print(f"{i}")
#         if i == 20:
#             print("got it.")
#
# my_function()

# from random import randint
#
# dice_image = ["d1","d2","d3","d4","d5","d6"]
# dice_number = randint(0, len(dice_image)-1)
# print(dice_number)
# print(f"{dice_image[dice_number]}")

# year = int(input("What's you year of birth? "))
#
# if 1980 < year < 1994:
#     print("You are a millennial...")
# elif year >= 1994:
#     print("you are a gen z.")

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap(2000))