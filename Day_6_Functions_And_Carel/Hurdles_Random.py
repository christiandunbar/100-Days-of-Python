# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Following code is functions available only at above website, but added here to avoid warnings.

def turn_left():
    doSomething = "yes"


def move():
    doSomething = "yes"


def at_goal():
    doSomething = "yes"


# Code above is functions available only at above website, but added here to avoid warnings.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    move()
    jump()
    turn_left()
