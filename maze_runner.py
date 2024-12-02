'''
    This module implements maze_reader() function, contains main() function and provides taking input
    from command line. Additionally, this module handles all the thrown exceptions.

    Author: Rasul Abbaszada
'''


from maze import Maze
import argparse
from typing import Optional

# raises Exception if something goes wrong when reading file
def get_file_content(file: str) -> list[str]:
    content: list[str] = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip())
    return content


# checks if dimensions, symbols etc. are correct, raises ValueError if not
def check_content(content: list[str]) -> None:
    # 1 cell in actual maze is represented by 3 x 3 array in maze file
    # that's why minimal size for columns and rows is 3
    if len(content) < 3:
        raise ValueError("Size of rows must be at least 3")

    # size of columns must be bigger than or equal to 3 and their lengths must be equal
    col_sz: int = len(content[0])
    for row in content:
        if len(row) < 3:
            raise ValueError("Size of column must be at least 3")
        if len(row) != col_sz:
            raise ValueError("Size of all columns must be equal")

    wall: str = "#"
    # check if external walls are all '#'
    for i in range(len(content)):
        for j in range(len(content[0])):
            if i == 0 or i + 1 == len(content):
                if (content[i][j] != wall):
                    raise ValueError("Incorrect character in external wall")
            if j == 0 or j + 1 == len(content[0]):
                if (content[i][j] != wall):
                    raise ValueError("Incorrect character in external wall")


def maze_reader(maze_file: str) -> Maze:
    wall: str = "#"
    path: str = "."

    try:
        content: list[str] = get_file_content(maze_file)
    except Exception:
        raise IOError("Something happened when reading the file")

    try:
        # checks content, raises Exception if anything illegal happens
        check_content(content)

        height: int = len(content) // 2  # height of the actual maze grid
        width: int = len(content[0]) // 2   # width of the actual maze grid
        maze: Maze = Maze(width, height)

        # read maze_file
        for i in range(len(content) - 2, 0, -2):
            for j in range(1, len(content[0]) - 1, 2):
                # check if there is an illegal symbol
                if content[i][j] != wall and content[i][j] != path \
                    or content[i - 1][j] != wall and content[i - 1][j] != path \
                    or content[i][j + 1] != wall and content[i][j + 1] != path \
                    or content[i + 1][j] != wall and content[i + 1][j] != path \
                    or content[i][j - 1] != wall and content[i][j - 1] != path:
                    raise ValueError("Incorrect character\n")


                # map the coordinates of maze in file to the coordinates of maze to be stored
                x: int = (j - 1) // 2
                y: int = (len(content) - (i + 2)) // 2

                # proceed adding the walls
                if content[i - 1][j] == wall:
                    maze.add_horizontal_wall(x, y + 1)
                if content[i][j + 1] == wall:
                    maze.add_vertical_wall(y, x + 1)
                if content[i + 1][j] == wall:
                    maze.add_horizontal_wall(x, y)
                if content[i][j - 1] == wall:
                    maze.add_vertical_wall(y, x)

        return maze

    except Exception as e:
        raise e

def check_arguments(content: list[str], starting: Optional[tuple[int, int]], goal: Optional[tuple[int , int]]) -> bool:
    height: int = len(content) // 2  # height of the maze
    width: int = len(content[0]) // 2   # width of the maze

    if goal != None:
        if not isinstance(goal, tuple):
            return False

        # check if out of dimension
        if goal[0] < 0 or goal[0] > width - 1 \
        or goal[1] < 0 or goal[1] > height - 1 :
            return False

    if starting != None:
        if not isinstance(starting, tuple):
            return False

        # check if out of dimension
        if starting[0] < 0 or starting[0] > width - 1 \
        or starting[1] < 0 or starting[1] > height - 1:
                return False

    return True


def str_to_tuple(s: str) -> tuple[int , int]:
    '''
        if input is correct after s.strip, it has to have lengths 3 and s[0] and s[2] must be digit
    '''
    if s == None:
        return None

    s = s.replace(" ", "")
    if len(s) != 3:
        raise ValueError("Incorrect argument\n")

    if not s[0].isdigit() or not s[2].isdigit():
        raise ValueError("Coordinates must be numerical\n")

    return (int(s[0]), int(s[2]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("maze", help="The name of the maze file, e.g., maze1.mz")
    parser.add_argument("--starting", type=str, help='The starting position, e.g., "2, 1"')
    parser.add_argument("--goal", type=str, help='The goal position, e.g., "4, 5"')

    args = parser.parse_args()

    try:
        content = get_file_content(args.maze)

        starting: tuple[int, int] = str_to_tuple(args.starting)
        goal: tuple[int, int] = str_to_tuple(args.goal)

        if not check_arguments(content, starting, goal):
            raise ValueError("Incorrect arguments")

        # create maze and run shortest_path algorithm
        myMaze: Maze = maze_reader(args.maze)

        s_path: list[tuple[int, int]] = myMaze.shortest_path(starting, goal)

        # print the shortest path
        for pair in s_path:
            print(pair, end=" ")

    except Exception as e:
        print(e)




