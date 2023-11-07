# From https://docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=None, flush=False)

from time import sleep

# removing new-line creation
print("Hello ", end="")
print("World")

# adding new-line creation within string
print("Line 1\nLine 2")

# flush parameter testing
# stackoverflow answer from Kurt Bourbaki, https://stackoverflow.com/a/74678272
for i in range(5):
    print(i, end=" ", flush=True)  # Print numbers as soon as they are generated
    # print(i, end=" ", flush=False)  # Print everything together at the end
    sleep(0.5)

print("end")

# printing with embedded quotations
print("Hello, \"bud\"")
print('Hello, "bud"')

# using format string
name = "Me"
print(f"Hello, {name}")

# empty line
print()