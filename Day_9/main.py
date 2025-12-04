# print("welcome to Day 9")

# student_data = {
#     "Harry": {
#         "scores": [88, 90, 92],
#         "details": {
#             "house": "Gryffindor",
#             "age": 15
#         }
#     },
#     "Hermione": {
#         "scores": [95, 98, 97],
#         "details": {
#             "house": "Gryffindor",
#             "age": 15
#         }
#     }
# }
#
# print(student_data["Harry"]["scores"][1])
# print(student_data["Harry"]["details"]["house"])

bidders = {}
should_continue = True


def add_bidders(name, amount):
    bidders[name] = amount  # store direct amount


def highest_bidder():
    max_name = ""
    max_amount = 0

    for name, amount in bidders.items():
        if amount > max_amount:
            max_amount = amount
            max_name = name

    return max_name, max_amount


while should_continue:
    name = input("What is your name?\n")
    amount = int(input("Your bidding amount:\n"))

    add_bidders(name, amount)

    ask_again = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if ask_again == "no":
        should_continue = False

winner_name, winner_amount = highest_bidder()

print(f"Highest Bidder: Name: {winner_name} | Bid Amount: ${winner_amount}")
