row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
treasureMap = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

columnId = int(position[0]) - 1
rowId = int(position[1]) - 1
treasureMap[rowId][columnId] = "X"

print(f"{row1}\n{row2}\n{row3}")
