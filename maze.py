"""
    This module implement the Maze class. Maze has m(width) x n(height) dimensions.
    It consists of cells which have walls. That's why I have created helper Cell class which has 4 properties
    to describe 4 walls of a cell. Collection of m x n cells give us the Maze.

    Unfortunately, origin of maze is bottom left corner. To make coordinates of 'stored-maze'(self._maze)
    consistent with the given maze, I have chosen length of the maze array to be height of the given maze, width of
    the maze array to be width of the given array.
    For example:

    if w == width and h == height

    Given maze:                Stored maze(self._maze):
                                   0  1  2
    2 |  |  |  |  |            0 |  |  |  |
    1 |  |  |  |  |            1 |  |  |  |
    0 |  |  |  |  |            2 |  |  |  |
       0  1  2   3             3 |  |  |  |

       h x w                       w x h

    Author: Rasul Abbaszada
    Last edited: 29/11/2024
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
        self._explored_coordinates: list[tuple[int, int]] = []

    @staticmethod
    def _initialize_maze(width, height) -> list[list[Cell]]:
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
        # when we add wall, it causes 2 cells to change, therefore update both of them
        self._maze[x_coordinate][horizontal_line - 1].north = True
        self._maze[x_coordinate][horizontal_line].south = True

    def add_vertical_wall(self, y_coordinate, vertical_line) -> None:
        # when we add wall, it causes 2 cells to change, therefore update both of them
        self._maze[vertical_line - 1][y_coordinate].east = True
        self._maze[vertical_line][y_coordinate].west = True

    def get_walls(self, x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
        cell: Cell = self._maze[x_coordinate][y_coordinate]
        return (cell.north, cell.east, cell.south, cell.west)

    def sense_walls(self, myRunner: Runner) -> tuple[bool, bool, bool]:  # tuple(Left, Front, Right)
        '''Returns the information about the walls on the Left, Right and in Front of the runner'''
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
        '''If there is no wall, go straight, otherwise raise ValueError'''
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

        elif myRunner.orientation == 'W':
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

    def explore(self, myRunner: Runner, goal: Optional["tuple[int, int]"]=None) -> str:
        # sequence represents the actions the runner took, for instance Left(L) or Right(R) till the runner
        # reaches the goal
        sequence: str = ""
        if goal == None:
            goal = (self.width - 1, self.height - 1)

        self._explored_coordinates.append((myRunner.x, myRunner.y))
        while (myRunner.get_position() != goal):
            (myRunner, move_seq) = self.move(myRunner)
            self._explored_coordinates.append((myRunner.x, myRunner.y))
            sequence += move_seq

        return sequence

    @staticmethod
    def _visualize(maze: list[list[Cell]], width: int, height: int, myRunner: Runner) -> list[list[str]]:
        '''
            Our maze is not stored in the order it should be visualized. (Refer to the top of the document)
            To make origin of maze_array(array to be printed) to represent the origin of given maze correctly,
            we will start the index at the bottom left of maze_array and fill that row with the help of 'stored
            maze'(self._maze), then we will work our way to the top. 'maze_array' will be filled from the bottom to top, while
            we iterate the 'stored maze' from top to bottom.
            Remember the number of columns in 'stored maze' represents the actual height of the given maze,
            the number of rows in 'stored maze' represents the actual width of the given maze.

            Then we first iterate the 1st column of 'stored maze', then 2nd, then 3rd...(we iterate the 1st row in
            given maze, 2nd row, then 3rd row...)

            So, 1st column of 'stored maze' fills the bottom row of the 'maze_array'(which is the bottom row of
            given original maze!!!), and it continues like this.

            Second point: Each wall fills 3 coordinate in the maze_array.

            This function returns the maze_array.
            For printing, see the print function below.

            Hopefully, I made my point clear:)
        '''
        wall: str = "#"
        path: str = "."
        vertical_line: int = width + 1    # length of vertical line
        horizontal_line: int = height + 1  # length of horizontal line
        maze_array_width:int = width + vertical_line
        maze_array_height:int = height + horizontal_line


        maze_array: list[list[str]] = [["." for _ in range(maze_array_width)] for _ in range(maze_array_height)]

        # maze_array_height - 1 = last row of the maze array, but last row is only walls, so
        # to get the index that represents the bottom 'cells':
        i: int = maze_array_height - 2

        # each time we decrease j and i by 2. because actual Cells come after each 2 coordinate of maze_array
        # we can fill neighbouring coordinates according to the info we got in the stored maze(self._maze)
        for col in range(0, height):
            j: int = 1
            for row in range(0, width):
                maze_array[i][j] = "."

                if maze[row][col].north:
                    maze_array[i - 1][j] = "#"
                    maze_array[i - 1][j + 1] = "#"
                    maze_array[i - 1][j - 1] = "#"

                if maze[row][col].east:
                    maze_array[i][j + 1] = "#"
                    maze_array[i + 1][j + 1] = "#"
                    maze_array[i - 1][j + 1] = "#"

                if maze[row][col].south:
                    maze_array[i + 1][j] = "#"
                    maze_array[i + 1][j + 1] = "#"
                    maze_array[i + 1][j - 1] = "#"

                if maze[row][col].west:
                    maze_array[i][j - 1] = "#"
                    maze_array[i + 1][j - 1] = "#"
                    maze_array[i - 1][j - 1] = "#"
                j += 2
            i -= 2

        # maps the actual coordinate of the runner in given maze to the maze_array
        # cost me an hour of my life, could I do it in an easy way? yes, but linear mapping has always been interesting for me
        x: int = maze_array_height - 2 * myRunner.y - 2
        y: int = 2 * myRunner.x + 1
        sign: str = ">"

        if myRunner.orientation == "N":
            sign = "^"
        elif myRunner.orientation == "E":
            sign = ">"
        elif myRunner.orientation == "S":
            sign = "v"
        else:
            sign = "<"

        maze_array[x][y] = sign
        return maze_array

    def print_visualization(self, myRunner: Runner) -> None:
        maze_array = self._visualize(self._maze, self._width, self._height, myRunner)

        for col in maze_array:
            for row in col:
                print(row, end="")
            print()


    def shortest_path(self, starting: Optional[tuple[int, int]] = None, goal: Optional[tuple[int, int]] = None) -> list[tuple[int, int]]:
        ''' Return the shortest path from start to the goal. (Not the actual shortest path)
            Firstly, runner explores the maze and stores the coordinates that it stumbled
            Then we run our algorithm.
            We keep adding coordinates from explored_coordinates to shortest_path. When we have reached
            to the visited coordinate that means we have already been in that coordinate. And of course previous
            path to that coordinate was in shorter distance than the current one, so delete the coordinates from
            shorter_path after first instance of that coordinate.
        '''

        if starting == None:
            myRunner = Runner()
        else:
            myRunner = Runner(starting[0], starting[1])

        seq = self.explore(myRunner, goal)

        visited: list[tuple[int, int]] = []
        shortest_path: list[tuple[int, int]] = []

        for coordinate in self._explored_coordinates:
            if coordinate not in visited:
                visited.append(coordinate)
                shortest_path.append(coordinate)
            else:
                for i in range(len(shortest_path)):
                    if shortest_path[i] == coordinate:
                        # delete the elements after i
                        i += 1
                        del shortest_path[i:]
                        break

        return shortest_path

