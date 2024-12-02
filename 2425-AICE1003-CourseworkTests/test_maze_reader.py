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

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(parent_dir)

from maze import Maze
from maze_runner import maze_reader  # type: ignore
import pytest


def test_maze_reader_maze1() -> None:
    maze: Maze = maze_reader("maze1.mz")
    assert maze.width == 2
    assert maze.height == 1
    assert maze.get_walls(0, 0) == (True, False, True, True)
    assert maze.get_walls(1, 0) == (True, True, True, False)


# Of course, we could just store file names and check against ValueError in the test method
# but that would violate extensibility principle, maybe we will change exceptions for each individual
# file in the future
@pytest.fixture(params=[
    {"file": "maze2.mz", "expectedException": ValueError},
    {"file": "maze3.mz", "expectedException": ValueError},
    {"file": "maze4.mz", "expectedException": ValueError},
    {"file": "maze5.mz", "expectedException": ValueError},
    {"file": "maze6.mz", "expectedException": ValueError}
]
)
def testcase(request) -> dict:
    return request.param

def test_maze_reader_mazes(testcase: dict) -> None:
    file = testcase["file"]
    with pytest.raises(testcase["expectedException"]):
        maze: Maze = maze_reader(file)
