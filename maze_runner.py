
from maze import Maze
from runner import Runner

def maze_reader(maze_file: str) -> Maze:
    content: list[str] = []
    try:
        with open(maze_file, 'r') as m:
            for line in m:
                content.append(line.strip())

    except Exception as e:
        raise IOError(f"maze_reader cannot read the file {maze_reader}\n")

    try:
        if len(content) < 3:
            raise ValueError

        # size of columns must be bigger than or equal to 3 and their lengths must be equal
        col_sz: int = len(content[0])
        for row in content:
            if len(row) < 3:
                raise ValueError
            if len(row) != col_sz:
                raise ValueError

        wall: str = "#"
        path: str = "."
        height: int = len(content) // 2
        width: int = len(content[0]) // 2
        maze:Maze = Maze(width, height)
        # read maze_file
        for i in range(len(content) - 2, 0, -2):
            for j in range(1, len(content[0]) - 1, 2):
                # check values of each cell
                if content[i][j] != wall and content[i][j] != path \
                    or content[i - 1][j] != wall and content[i - 1][j] != path \
                    or content[i][j + 1] != wall and content[i][j + 1] != path \
                    or content[i + 1][j] != wall and content[i + 1][j] != path \
                    or content[i][j - 1] != wall and content[i][j - 1] != path:
                    raise ValueError

                if content[i - 1][j] == wall:
                    maze.add_horizontal_wall((j - 1) // 2, ((len(content) - (i + 2)) // 2) + 1)
                if content[i][j + 1] == wall:
                    maze.add_vertical_wall((len(content) - (i + 2)) // 2, ((j - 1) // 2) + 1)
                if content[i + 1][j] == wall:
                    maze.add_horizontal_wall((j - 1) // 2, ((len(content) - (i + 2)) // 2))
                if content[i][j - 1] == wall:
                    maze.add_vertical_wall((len(content) - (i + 2)) // 2, ((j - 1) // 2))

        return maze

    except Exception as d:
        raise ValueError(f"Incorrect dimension or incorrect value in maze\n")



