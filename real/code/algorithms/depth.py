from ..classes.board import Board
import queue
from copy import deepcopy
from .randomize import RandomAlgorithm
from collections import deque
from tqdm import tqdm

class BB():

    def __init__(self, car_list, size):
        # self.depth = depth
        self.size = size
        self.car_list = car_list
        self.win = False
        self.winning_board = None
        self.infinite = False
        self.depth = 10000



    def every_move(self, board):
        '''
        shows every possible step every car can take
        '''
        board_list = []

        board.draw_board()

        for i, car in enumerate(board.car_list):

            # Determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(car)
            # print(car.name, lower_range, upper_range)

            # This while loop is to make sure the car does not stay still
            for difference in range(lower_range, upper_range + 1):
                if difference != 0:

                    # adds the difference to the car
                    board2 = deepcopy(board)

                    if car.orientation == 'H':
                        board2.car_list[i].col += difference
                        board2.moves.append((car.name, difference))

                    else:
                        board2.car_list[i].row += difference
                        board2.moves.append((car.name, difference))

                    board2.draw_board()
                    if board2.check_win():
                        self.depth = len(board2.moves)
                        self.win = True
                        self.winning_board = board2.board
                        return
                    # creates a list of multiple loops where every car makes every move it can make
                    board_list.append(board2)

        return board_list

    def branch_and_bound(self, max_steps=25):

        # Initialize a new board and a stack of moves
        board = Board(self.size, self.car_list)
        stack = self.every_move(board)
        current_list = deepcopy(stack)
        visited = {}

        # Continue looping until the infinite flag is set to True
        while self.infinite == False:

            # Continue looping until the win flag is set to True
            while self.win == False:

                # Check if there are still elements in the current list
                if len(current_list) > 0:

                    # Pop the next board from the list and convert it to a tuple
                    board2 = current_list.pop()
                    # print(board2)
                    state = tuple(board2.board.flatten())

                # If the list is empty, print the best result and set flags to True
                else:
                    print('The best is:')
                    print(f'steps: {self.depth}')
                    print(self.winning_board)
                    self.infinite = True
                    self.win = True

                # Check if the number of moves made on the board is less than max steps
                if len(board2.moves) < max_steps:
                    new_list = []

                    # Check if the state has been visited before
                    if state in visited:

                        # If it has and the number of moves is less than the previous one
                        # update the value in the visited dictionary
                        if len(board2.moves) < visited[state]:
                            visited[state] = len(board2.moves)
                            new_list = self.every_move(board2)

                    # If it hasn't been visited before, add it to the dictionary
                    # with the number of moves
                    else:
                        visited[state] = len(board2.moves)
                        new_list = self.every_move(board2)

                    # Add the new list of moves to the current_list
                    if new_list:
                        current_list.extend(new_list)

                # If the number of moves is less than max steps, print the number of moves and board
                # if len(board2.moves) < max_steps:
                #     print(len(board2.moves))
                #     # print(board2)

            # If win flag is set to true, check if the depth is less than max steps
            if self.win:

                if self.depth < max_steps:
                    # If it is, update max steps and print the depth
                    max_steps = self.depth
                    print('Found a winner at: ')
                    print(self.depth)
                    # print(board2.moves)

                # Reset the win flag to false
                self.win = False
