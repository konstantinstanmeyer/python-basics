# else block always runs if except block does not
try:
    x = int(input("Enter a valid number: "))
except ValueError:
    print("invalid input")
else:
    print(f"x is {x}")

# code that re-runs after every incorrect input

while True:
    try:
        x = int(input("Enter a valid number: "))

        # will not hit break if ValueError is returned
        break
    except ValueError:
        print("invalid input")

# the break condition being met hands back the values within the try block back to a greater scope
print(f"x is {x}")

# shorter syntax abstracting to function

def main():
    y = get_int()
    print(f"y is {y}")

# rerun after every failed attempt
def get_int():
    while True:
        try:
            return int(input("Enter a valid number: "))
        except ValueError:
            # can also send a print statement
            pass

main()