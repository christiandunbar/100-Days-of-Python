import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# 1st
eazyPassword = ""

for char in range(0, nr_letters + 1):
    eazyPassword += letters[random.randint(0, len(letters) - 1)]

for char in range(0, nr_symbols + 1):
    eazyPassword += symbols[random.randint(0, len(symbols) - 1)]

for char in range(0, nr_numbers + 1):
    eazyPassword += numbers[random.randint(0, len(numbers) - 1)]

print(f"Your eazy password is (1st): {eazyPassword}")

# 2nd
eazyPassword = ""

for char in range(0, nr_letters + 1):
    eazyPassword += random.choice(letters)

for char in range(0, nr_symbols + 1):
    eazyPassword += random.choice(symbols)

for char in range(0, nr_numbers + 1):
    eazyPassword += random.choice(numbers)

print(f"Your eazy password is (2nd): {eazyPassword}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# 1st

hardPassword = "".join(random.sample(eazyPassword, len(eazyPassword)))
print(f"Your hard password is (1st): {hardPassword}")

# 2nd
password_list = []

for char in range(0, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
hardPassword = "".join(password_list)

print(f"Your hard password is (2nd): {hardPassword}")


