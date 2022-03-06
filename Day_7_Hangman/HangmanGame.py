import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

guesses = []
display = []
for i in range(0, len(chosen_word)):
    display.append('_')
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if len(guess) > 1:
        print("A guess can only be a single letter!")
        return

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
        else:
            print("Wrong")

    print(display)
