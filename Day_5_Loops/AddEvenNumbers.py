# 1st
total = 0

for x in range(1, 101):
    if (x / 2).is_integer():
        total += x

print(f"Total is: {total}")

# 2nd
total = 0

for x in range(1, 101):
    if x % 2 == 0:
        total += x

print(f"Total is: {total}")

# 3rd
total = 0

for x in range(2, 101, 2):
    total += x

print(f"Total is: {total}")
