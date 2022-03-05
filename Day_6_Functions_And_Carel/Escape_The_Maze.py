# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Following code is functions available only at above website, but added here to avoid warnings.

def turn_left():
    doSomething = "yes"


def move():
    doSomething = "yes"


def at_goal():
    doSomething = "yes"


def front_is_clear():
    doSomething = "yes"


def right_is_clear():
    doSomething = "yes"


# Code above is functions available only at above website, but added here to avoid warnings.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
