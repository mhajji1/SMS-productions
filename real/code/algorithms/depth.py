from ..classes.board import Board
import queue
from copy import deepcopy
from .randomize import RandomAlgorithm
from collections import deque
from tqdm import tqdm

class Depth():

    def __init__(self, car_list, size):
        # self.depth = depth
        self.size = size
        self.car_list = car_list
        self.win = False
        self.winning_board = None
        self.infinite = False



    def stack_moves(self, board):
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

                    else:
                        board2.car_list[i].row += difference

                    board2.draw_board()
                    if board2.check_win():
                        self.win = True
                        self.winning_board = board2.board
                        return
                    # creates a list of multiple loops where every car makes every move it can make
                    board_list.append(board2)

        return board_list


    # def depth_step(self, max_steps=50000):
    #
    #     board = Board(self.size, self.car_list)
    #     stack = self.stack_moves(board)
    #     current_list = deepcopy(stack)
    #     visited = set()
    #
    #     while self.infinite == False:
    #
    #         while self.win == False:
    #
    #             step_count = 0
    #
    #             for i, board2 in enumerate(current_list):
    #                 state = tuple(board2.board.flatten())
    #
    #                 if state not in visited:
    #                     visited.add(state)
    #                     step_count += 1
    #                     # print(step_count)
    #
    #                     # if step_count > max_steps:
    #                     #     break
    #                     # print(board2)
    #                     new_list = self.stack_moves(board2)
    #                     if new_list:
    #                         copy_list = deepcopy(new_list)
    #                         current_list[:0] = copy_list
    #
    #         if self.win:
    #             print('The winner is: ')
    #             print(step_count)
    #             print(self.winning_board)
    #             self.win = False

    def depth_step(self, max_steps=50000):
        count = 0
        board = Board(self.size, self.car_list)
        stack = self.stack_moves(board)
        current_list = deepcopy(stack)
        visited = set()

        while self.infinite == False:
            step_count = 0
            while self.win == False:

                if len(current_list) > 0:
                    board2 = current_list.pop()
                    state = tuple(board2.board.flatten())
                    step_count += 1
                else:
                    print('list is empty')
                    self.infinite = True
                    self.win = True

                if state not in visited:
                    visited.add(state)
                    # print(step_count)

                    # if step_count > max_steps:
                    #     break
                    # print(board2)
                    node = self.stack_moves(board2)
                    if new_list:
                        copy_list = deepcopy(node)
                        current_list.extend(copy_list)

            if self.win:
                count += 1
                print(count)
                print('The winner is: ')

                print(self.winning_board)
                self.win = False
