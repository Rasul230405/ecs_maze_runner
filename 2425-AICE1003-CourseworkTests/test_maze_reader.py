"""
Created on Wed Nov 20 15:32:28 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"

import pytest

from maze import Maze
from maze_runner import maze_reader  # type: ignore


def test_maze_reader_maze1() -> None:
    maze: Maze = maze_reader("maze1.mz")
    assert maze.width == 2
    assert maze.height == 1
    assert maze.get_walls(0, 0) == (True, False, True, True)
    assert maze.get_walls(1, 0) == (True, True, True, False)


def test_maze_reader_maze2() -> None:
    with pytest.raises(ValueError):
        maze: Maze = maze_reader("maze2.mz")
