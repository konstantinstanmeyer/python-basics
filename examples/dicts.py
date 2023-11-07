import random

people = {
    "Rob": random.randint(20, 80),
    "Bob": random.randint(20, 80),
    "Tod": random.randint(20, 80),
    "Pat": random.randint(20, 80),
    "Max": random.randint(20, 80),
}

# print the name and age of each person on their own line
for p in people:
    print(p, people[p], sep=": ")

people_2 = [
    {
        "name": "Rob",
        "age": random.randint(20, 80),
        "weight": random.randint(120, 300)
    },
    {
        "name": "Bob",
        "age": random.randint(20, 80),
        "weight": random.randint(120, 300)
    },
    {
        "name": "Tod",
        "age": random.randint(20, 80),
        "weight": random.randint(120, 300)
    },
]

for p in people_2:
    print(p["name"], p["age"], str(p["weight"]) + "lbs", sep=", ")