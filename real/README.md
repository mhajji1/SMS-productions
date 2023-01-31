# Readme for Rush hour 
## Introduction
This project implements the A* algorithm to solve the popular sliding puzzle game called Traffic Jam. The game involves sliding cars in a grid to clear a path for the red car to escape to the right.

## Requirements
The following packages are required to run the code:
- numpy
- dataclasses
- queue
- copy
- Code Explanation

## The code consists of two main classes:

Board class to represent the state of the game and perform actions such as updating the board and checking if the red car has escaped
Astar class which implements the A* algorithm to find the solution to the game.
The Astar class initializes with a list of all the cars, their starting positions and the size of the grid. The every_step method generates all the possible moves that can be taken by each car and adds them to the priority queue. The calculate method calculates the heuristic value for each state which is used to determine the priority of the state in the queue. The A* algorithm terminates when the red car has escaped or the maximum number of steps is reached.

Usage
python
Copy code
from ..classes.board import Board
from ..algorithms.astar import Astar

## Conclusion
The A* algorithm is a powerful technique for solving problems such as the Traffic Jam game. The algorithm efficiently finds a solution to the game by exploring states with higher priority values first. The code can be further optimized by improving the heuristics used to determine the priority of each state.
