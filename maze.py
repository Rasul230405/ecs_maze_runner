class Square:
    def __init__(self, North: bool, East: bool, South: bool, West: bool):
        self.North = North
        self.East = East
        self.South = South
        self.West = West

    def __str__(self):
        return f"({self.North}, {self.East}, {self.South}, {self.West})"


class Maze:
    def __init__(self, width: int = 5, height: int = 5):
        self._width = width
        self._height = height
        self._maze: list[list[Square]] = [[Square(False, False, False, False) for _ in range(width)] for _ in range(height)]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def maze(self):
        return self._maze

    def add_horizontal_wall(self, x_coordinate, horizontal_line) -> None:
        self._maze[horizontal_line - 1][x_coordinate].North = True
        self._maze[horizontal_line][x_coordinate].South = True

    def add_vertical_wall(self, y_coordinate, vertical_line) -> None:
        self._maze[y_coordinate][vertical_line - 1].East = True
        self._maze[y_coordinate][vertical_line].West = True

    def get_wall(self, x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
        square: Square = self._maze[y_coordinate][x_coordinate]
        return (square.North, square.East, square.South, square.West)


m = Maze(11, 5)
m.add_horizontal_wall(5, 2)
m.add_vertical_wall(2, 4)
print(m.get_wall(4, 2))
print(m.get_wall(5, 2))

mz = m.maze

for line in mz:
    for square in line:
        print(square, end=" ")
    print()
