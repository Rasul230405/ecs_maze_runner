"""
Created on Wed Nov 20 18:53:45 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"

from maze import Maze


def test_shortest_path() -> None:
    """A Unit test for :py:func:`~maze.shortest_path`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (0, 1).

    3. Add a vertical wall at (1, 1).

    4. Run short_path function to get the path (with default start and goal).

    5. Check that the result is a valid path, starting from (0,0) and end at
       (10, 4).
    """
    maze = Maze(11, 5)
    maze.add_horizontal_wall(0, 1)
    maze.add_vertical_wall(1, 1)
    path = maze.shortest_path()
    assert path[0] == (0, 0)
    assert path[-1] == (10, 4)
    prefix = []
    for location in path:
        assert location not in prefix, f"{location} is repeated"
        prefix.append(location)