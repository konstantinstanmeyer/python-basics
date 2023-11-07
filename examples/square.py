# print a square in the terminal based on the input value
def square():
    num = int(input("Enter a number: "))

    # create rows + columns
    for _ in range(num):
         print_row(num)

# abstraction to give each funciton one responsibility
def print_row(len):
    print("#" * len)

square()