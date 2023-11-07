# get user's name, capitalizing and removing whitespace if necessary
name = input("Enter Name: ").strip().title()

if name == "Bob":
    print("Hello, your name has bob in it")
else:
    print("Your name does not have bob in it")

match name:
    case "Bob":
        print("You have bob in your name")
    case _:
        print("Your name does not have bob in it")

print("Hello\n" * 3, end="")

# try-except allows non-number values to not break the code
while True:
    try:
        n = int(input("Enter A Number: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input, please try again")
        continue

# range gives an iterable the length of its input value
# _ designates we're not interested the inputs array's values, just using it as a reference value
for _ in range(n):
    print(f"This will repeat {n} number of times")