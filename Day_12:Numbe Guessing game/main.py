print("welcome to Day 12")

guess_number = int(input("Enter a number: "))

def is_prime():
    if guess_number <= 1:
        return False
    for i in range(2, guess_number):
        if guess_number % i == 0:
            return False
    return True


print(is_prime())