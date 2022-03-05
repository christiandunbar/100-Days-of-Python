import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
optionNames = ["Rock", "Paper", "Scissors"]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choiceName = optionNames[choice]
machineChoice = random.randint(0, 2)
machineChoiceName = optionNames[machineChoice]

print(f"Your choice: {choiceName}")
print(options[choice])
print(f"Machine choice: {machineChoiceName}")
print(options[machineChoice])

results = [
    {
        "left": "Rock",
        "right": "Rock",
        "result": "draw"
    },
    {
        "left": "Rock",
        "right": "Paper",
        "result": "lose"
    },
    {
        "left": "Rock",
        "right": "Scissors",
        "result": "win"
    },
    {
        "left": "Paper",
        "right": "Rock",
        "result": "win"
    },
    {
        "left": "Paper",
        "right": "Paper",
        "result": "draw"
    },
    {
        "left": "Paper",
        "right": "Scissors",
        "result": "lose"
    },
    {
        "left": "Scissors",
        "right": "Rock",
        "result": "lose"
    },
    {
        "left": "Scissors",
        "right": "Paper",
        "result": "win"
    },
    {
        "left": "Scissors",
        "right": "Scissors",
        "result": "draw"
    }
]

result = [x for x in results if x["left"] == choiceName and x["right"] == machineChoiceName][0]
print(f"You {result['result']}!")
