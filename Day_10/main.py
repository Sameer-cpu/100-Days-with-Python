# print("welcome to Day 10")

# year = int(input("please ender the year to check its leap or not: "))
#
# def is_leap_year(leap_year):
#     reminder = leap_year % 4 == 0
#     print(leap_year % 4)
#     if reminder:
#         return True
#     else:
#         return False
#
# print(f"the {year} is leap: {is_leap_year(year)}")

# Calculator project:

should_continue = True
total = 0
previous = None

def _add(n1, n2):
    return n1 + n2

def _subtract(n1, n2):
    return n1 - n2

def _multiply(n1, n2):
    return n1 * n2

def _divide(n1, n2):
    return n1 / n2

def calculating(n1,n2,_operator):
    if _operator == "+":
        return _add(n1,n2)
    elif _operator == "-":
        return _subtract(n1,n2)
    elif _operator == "*":
        return _multiply(n1,n2)
    elif _operator == "/":
        return _divide(n1,n2)
    else:
        return "Invalid operator"


while should_continue:
    if previous is None:
        value1 = int(input("value one: "))
    else:
        value1 = int(previous)
    operator = input("for add use \'+\' operator\nfor subtract use \'-\' operator\nfor multiple use \'*\' operator\nfor divide use \'/\' operator\n\nplease select an operator: ")
    value2 = int(input("value two: "))
    total = calculating(n1 = value1, _operator=operator, n2= value2)
    _continue = input("would you like to continue? \'YES\' or \'NO\'").strip().lower()
    print(f"{value1} {operator} {value2} = {total}")
    if _continue == "no":
        should_continue = False
    elif _continue == "yes":
        previous = total
    else:
        print("Invalid choice, stopping...")
        should_continue = False