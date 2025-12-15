import random

print("welcome to Day 11")

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Drew :)"
    elif c_score == 0:
        return "Lose, Opponent has BlackJack"
    elif u_score == 0:
        return "Win with a BlackJack"
    elif u_score >21:
        return "You went over, You lose"
    elif c_score > 21:
        return "Opponent went over, You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
is_game_end = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"User Cards: {user_cards}  User Score : {user_score}")
    print(f"Computer first Card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_end = True
    else:
        should_continue = input("type 'y' to get another card. type 'n' to pass")
        if should_continue == "y":
            user_cards.append(deal_card())
        else:
            is_game_end = True




while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"\n\n\n\n\nYour final hand: {user_cards}, Your total score: {user_score}")
print(f"Computer final hand: {computer_cards}, Computer total score: {computer_cards}")
print(compare(user_score,computer_score))