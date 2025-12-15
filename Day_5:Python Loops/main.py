import random
# print("welcome to Day 5")
#
# fruits = ["Apple", "Banana", "Orange"]
#
# for item in fruits:
#     print(item)

# student_score = [10,20,30,100,500,300,120,400]
#
# print(max(student_score))
#
# highest_score = 0
#
# for score in student_score:
#     if(score > highest_score):
#         highest_score = score
#
# print(f"highest number is {highest_score}")

# sum = 0
#
# for num in range(1, 101):
#     sum += num
#
# print(sum)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?", "|"]

print("Welcome to the pyPassword Generator ")
number_of_alphabets = int(input("How many letter's would you like in your password?: "))
number_of_numbers = int(input("How many numbers would you like in your password?: "))
number_of_symbols = int(input("How many symbols would you like in your password?: "))

#Easy Way.

password_list = []
total_password =number_of_alphabets + number_of_numbers + number_of_symbols + 1


for number in range(1, total_password):
    if len(password_list) < number_of_alphabets:
        password_list.append(random.choice(alphabets))
    elif (len(password_list) >= number_of_alphabets) and (len(password_list) < (number_of_alphabets + number_of_numbers)):
        password_list.append(random.choice(numbers))
    elif len(password_list) >= (number_of_alphabets + number_of_numbers):
        password_list.append(random.choice(symbols))


random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"your random password is: {password}")



