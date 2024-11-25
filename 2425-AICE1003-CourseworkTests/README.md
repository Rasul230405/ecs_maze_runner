# 2425 - AICE1003 - Coursework Tests
This repository contains some tests for the ECS Maze Runner coursework (AY2024-25).

## Getting Started
- You are recommended to clone this repository using SSH
```
git clone git@git.soton.ac.uk:tsh2n14/2425-AICE1003-CourseworkTests.git
```
or using HTTPS
```
https://git.soton.ac.uk/tsh2n14/2425-AICE1003-CourseworkTests.git
```
The advantage of using git is that you will get the updated versions of the test
suit when they are released.

- Alternatively, you can download the various files directly from this repository.

- The test suit is organised in several test files. You are expected to extend
the test suit with more tests of your own.
  
  - `test_runner.py`: Some unit tests for testing the functionality of 
    `runner.py` including creating a runner, turn, and move the runner forward.
  - `test_maze.py`: Some unit tests for testing the functionality of the `Maze`
    class, including creating a maze, add horizontal and vertical walls.
  - `test_maze_runner.py`: Some unit tests for testing the functionality of the
    runner to explore the maze including sensing the walls and turning left,
    right and to go straight.
  - `test_shortest_path.py`: Some unit tests for testing the `shortest_path`
    function (in `maze.py` for Part 4).
  - `test_maze_reader.py`: Some initial unit tests for testing the
    `maze_reader()` function (in `maze_runner.py` for Part 5).

- Folder `mazes` contains some mazes of different sizes for manual testing.

- More tests will be added as the coursework specification evolves.

## Authors and Acknowledgement
The current maintainer for this repository is
[T.S.Hoang](mailto:T dot S dot Hoang at soton dot ac dot uk).

## License
The code in this repository is licenced under the MIT License and can be seen in
the `LICENSE.md` file.
