from ..classes.board import Board
from .breadth import Breadth

from copy import deepcopy
from collections import deque
import queue

class BB():

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.states = set()
        self.win = False
        self.winning_board = None
        self.infinite = False
        self.depth = 10000


    def run(self, max_steps=15):
        breadth = Breadth(self.full_list, self.car_list, self.size)
        board = Board(self.car_list)
        board_list = breadth.every_step(board)
        print(board_list)

        current_list = deepcopy(board_list)
        board2 = 1

        win_list = []
        visited = {}

        # Continue looping until the infinite flag is set to True
        while self.infinite == False:

            # Continue looping until the win flag is set to True
            while self.win == False:

                # Check if there are still elements in the current list
                if len(current_list) > 0:

                    # Pop the next board from the list and convert it to a tuple

                    board2 = current_list.pop()
                    if board2 == 0:
                        print('WINNER IS FOUND')
                        win_list.append([board2, self.depth])
                        self.depth = len(breadth.winning_moves)
                    else:
                        state = tuple(board2.board.flatten())

                # If the list is empty, print the best result and set flags to True
                else:
                    print(win_list)
                    print('The best is:')
                    print(f'steps: {self.depth}')
                    print(len(breadth.winning_moves))
                    self.infinite = True
                    breadth.win = True
                    break

                # Check if the number of moves made on the board is less than max steps
                if board2 == 0:
                    print('something')
                    if self.depth <= max_steps:
                        # If it is, update max steps and print the depth
                        max_steps = self.depth
                        print('Found a winner at: ')
                        print(self.depth)
                        # print(board2.moves)

                    # Reset the win flag to false
                    self.win = False

                else:
                    if len(board2.moves) < max_steps:
                        new_list = []

                        # Check if the state has been visited before
                        if state in visited:

                            # If it has and the number of moves is less than the previous one
                            # update the value in the visited dictionary
                            if len(board2.moves) < visited[state]:
                                visited[state] = len(board2.moves)
                                new_list = breadth.every_step(board2)


                        # If it hasn't been visited before, add it to the dictionary
                        # with the number of moves
                        else:
                            visited[state] = len(board2.moves)
                            new_list = breadth.every_step(board2)

                        # Add the new list of moves to the current_list
                        if new_list:
                            current_list.extend(new_list)

                # If the number of moves is less than max steps, print the number of moves and board
                    if len(board2.moves) < max_steps:
                        print(len(board2.moves))
                        print(board2)

            # If win flag is set to true, check if the depth is less than max steps
