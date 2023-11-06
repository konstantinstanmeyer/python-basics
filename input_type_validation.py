# validation by checking value with if statement
def get_num_1():
    num = input("Enter a valid number: ")
    if num.isdigit():
        print("You have entered:", num)
    else:
        print("Invalid Number!")
        get_num_1()

# validation using try-exept block syntax
def get_num_2():
    try:
        num_input = input("Enter a valid number: ")
        num = int(num_input)
        print("You have entered:", num)
    except ValueError:
        print("Invalid Number!")
        get_num_2()

# *ARBITRARY: confirming input is string using type checking
def get_name():
    name = input("What is your name? ")
    if type(name) == str:
        print("Hello,", name)
    else:
        # else block can never be reached
        print("Invalid!")
        get_name()

get_num_1()
get_num_2()
get_name()