"""
    This module implement the Maze class. Maze has m(width) x n(height) dimensions.
    It consists of cells which have walls. That's why I have created helper Cell class which has 4 properties
    to describe 4 walls of a cell. Collection of m x n cells give us the Maze.

    Author: Rasul Abbaszada
    Last edited: 25/11/2024
"""

from runner import Runner
from typing import Optional

class Cell:
    def __init__(self, North: bool, East: bool, South: bool, West: bool):
        self.north = North
        self.east = East
        self.south = South
        self.west = West

    def __str__(self):
        return f"({self.north}, {self.east}, {self.south}, {self.west})"

class Maze:

    def __init__(self, width:int = 5, height:int = 5):
        self._width = width
        self._height = height
        self._maze: list[list[Cell]] = self._initialize_maze(width, height)
    def _initialize_maze(self, width, height) -> list[list[Cell]]:
        '''create maze and external walls'''

        # width x height
        maze = [[Cell(False, False, False, False) for _ in range(height)] for _ in range(width)]

        for row in range(height):
            for col in range(width):
                if row == 0:    # bottom row
                    maze[col][row].south = True
                if col == 0:    # left most column
                    maze[col][row].west = True
                if row == height - 1:   # top row
                    maze[col][row].north = True
                if col == width - 1:    # right most column
                    maze[col][row].east = True
        return maze

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def add_horizontal_wall(self, x_coordinate, horizontal_line) -> None:
        # when we add wall, it causes 2 squares to change, therefore update both of them
        self._maze[x_coordinate][horizontal_line - 1].north = True
        self._maze[x_coordinate][horizontal_line].south = True

    def add_vertical_wall(self, y_coordinate, vertical_line) -> None:
        # when we add wall, it causes 2 squares to change, therefore update both of them
        self._maze[vertical_line - 1][y_coordinate].east = True
        self._maze[vertical_line][y_coordinate].west = True

    def get_walls(self, x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
        cell: Cell = self._maze[x_coordinate][y_coordinate]
        return (cell.north, cell.east, cell.south, cell.west)

    def sense_walls(self, myRunner: Runner) -> tuple[bool, bool, bool]:  # tuple(Left, Front, Right)
        cell: Cell = self._maze[myRunner.x][myRunner.y]

        if myRunner.orientation == 'N':
            return (cell.west, cell.north, cell.east)
        if myRunner.orientation == 'E':
            return (cell.north, cell.east, cell.south)
        if myRunner.orientation == 'S':
            return (cell.east, cell.south, cell.west)
        if myRunner.orientation == 'W':
            return (cell.south, cell.west, cell.north)

    def go_straight(self, myRunner: Runner) -> Runner:
        cell: Cell = self._maze[myRunner.x][myRunner.y]

        if myRunner.orientation == 'N':
            if cell.north == True:
                raise ValueError("There is a wall in front of the runner")
            myRunner.forward()

        elif myRunner.orientation == 'E':
            if cell.east == True:
                raise ValueError("There is a wall in front of the runner")
            myRunner.forward()

        elif myRunner.orientation == 'S':
            if cell.south == True:
                raise ValueError("There is a wall in front of the runner")
            myRunner.forward()

        elif cell.orientation == 'W':
            if cell.west == True:
                raise ValueError("There is a wall in front of the runner")
            myRunner.forward()

        return myRunner

    def move(self, myRunner: Runner) -> tuple[Runner, str]:
        '''left hug'''
        cell: Cell = self._maze[myRunner.x][myRunner.y]
        walls = self.sense_walls(myRunner)
        sequence: str = ""

        if walls[0] == False:
            myRunner.turn("Left")
            sequence += "LF"

        elif walls[1] == False:
            sequence += "F"

        elif walls[2] == False:
            myRunner.turn("Right")
            sequence += "RF"

        else:
            myRunner.turn("Left")
            myRunner.turn("Left")
            sequence += "LLF"

        myRunner = self.go_straight(myRunner)
        return (myRunner, sequence)

    def explore(self, myRunner: Runner, goal : Optional[tuple[int, int]]) -> str:
        sequence: str = ""
        if goal == None:
            goal = (self.width - 1, self.height - 1)

        while (myRunner.get_position() is not goal):
            (myRunner, move_seq) = self.move(myRunner)
            sequence += move_seq

        return sequence

    def display(self):
        pass










'''
m = Maze(11, 5)
m.add_horizontal_wall(5, 2)
m.add_vertical_wall(2, 4)
print(m.get_walls(4, 2))
print(m.get_walls(5, 2))
print(m.get_walls(0, 0))

mz = m.maze

for line in mz:
    for square in line:
        print(square, end=" ")
    print()
'''