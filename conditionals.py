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