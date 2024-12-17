# BMI Calculator
# user_name = input("Enter your name: ")
# name_length = len(user_name)

# print("Number of letters in your name: " + str(name_length))

# Tip Calculator
print("Welcome to the Tip Calculator.!")
total_amount = input("What was the total bill: \n$")
tip = input("How much tip would you like to give 0 - 99: \n")
bil_split = input("How many people to split the bill: \n")

get_total_tip = round((int(tip) / 100) * int(total_amount))

calculate_total_price = int(total_amount) + get_total_tip

split_bill = round(calculate_total_price / int(bil_split))

print(f"\ntotal bill with {tip}% tip : ${calculate_total_price}\nSplit in {bil_split}\nSplit Amount: ${split_bill}")