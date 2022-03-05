import random

names_string = input("Who attended?\n")
names = names_string.split(", ")
random_choice = random.randint(0, len(names) - 1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy the meal today!")
