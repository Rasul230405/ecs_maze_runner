"""
    This module implements runner class and all the functions related to runner
    Magic constants:
    'N' - North
    'S' - South
    'W' - West
    'E' - East
    Last edited: 08/11/2024
    Author: Rasul Abbaszada
"""


# I think the best data type for runner is to define its own data type. why not?
class Runner:
    def __init__(self, x: int, y: int, orientation: str):
        self.x = x
        self.y = y
        self.orientation = orientation


def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> Runner:
    return Runner(x, y, orientation)

# it would be best to implement this function within class, but anyway
def get_x(runner: Runner) -> int:
    return runner.x

def get_y(runner: Runner) -> int:
    return runner.y

def get_orientation(runner) -> str:
    return runner.orientation

def turn(runner: Runner, direction: str) -> Runner:
    if direction == "Right":
        if runner.orientation == "N":
            runner.orientation = "E"
        elif runner.orientation == "W":
            runner.orientation = "N"
        elif runner.orientation == "S":
            runner.orientation = "W"
        else:
            runner.orientation = "S"

    else:
        if runner.orientation == "N":
            runner.orientation = "W"
        elif runner.orientation == "W":
            runner.orientation = "S"
        elif runner.orientation == "S":
            runner.orientation = "E"
        else:
            runner.orientation = "N"

    return runner

def forward(runner):
    if runner.orientation == "N":
        runner.y += 1
    elif runner.orientation == "S":
        runner.y -= 1
    elif runner.orientation == "W":
        runner.x -= 1
    else:
        runner.x += 1

    return runner



