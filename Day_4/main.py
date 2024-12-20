import random

# random_number = random.randint(0,3)

# if(random_number % 2 == 0):
#     print("Heads")
# else:
#     print("Tails")

# friends = ["person1", "person2", "person3","person4"]
#
# print(random.choice(friends))

select_rps_human = int(input("What do you chose? Type 1 for \"Rock\", 2 for \"Paper\", and 3 for \"Scissors\": "))
select_rsa_computer = random.randint(1, 3)

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

print(f"computer select {select_rsa_computer}")
if (((select_rps_human == 1) and (select_rsa_computer == 3)) or
    ((select_rps_human == 2) and (select_rsa_computer == 1)) or
    ((select_rps_human == 3) and (select_rsa_computer == 2))):
    if select_rps_human == 1:
        print(rock)
    elif select_rps_human == 2:
        print(paper)
    else:
        print(scissors)

    if select_rsa_computer == 1:
        print(rock)
    elif select_rsa_computer == 2:
        print(paper)
    else:
        print(scissors)

    print("\nyou Win.!\nComputer Lose.!")
elif(((select_rps_human == 3) and (select_rsa_computer == 1)) or
   (( select_rps_human == 1) and (select_rsa_computer == 2)) or
    ((select_rps_human == 2) and (select_rsa_computer == 3))):
    if select_rps_human == 1:
        print(rock)
    elif select_rps_human == 2:
        print(paper)
    else:
        print(scissors)

    if select_rsa_computer == 1:
        print(rock)
    elif select_rsa_computer == 2:
        print(paper)
    else:
        print(scissors)

    print("\nyou Lose.!\nComputer Win.!")
elif select_rps_human == select_rsa_computer:
    print("Match Draw.!")
else:
    print("try again and select 1 to 3,\n1 for \"Rock\",\n2 for \"Paper\",\n3 for \"Scissors\"")
