# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

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


def wall_in_front():
    doSomething = "yes"


# Code above is functions available only at above website, but added here to avoid warnings.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def climb():
    turn_left()
    move()

    while not right_is_clear():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if front_is_clear():
        move()

    if wall_in_front():
        climb()
