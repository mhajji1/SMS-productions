from ..classes.board import Board
import queue
from copy import deepcopy
from .randomize import RandomAlgorithm
from tqdm import tqdm

class Depth():

    def __init__(self, car_list, size):
        # self.depth = depth
        self.size = size
        self.car_list = car_list
        self.win = False
        self.winning_board = None



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


    def depth_step(self, max_steps=200):
        count = 0
        board = Board(self.size, self.car_list)
        stack = self.stack_moves(board)
        current_list = deepcopy(stack)
        step_count = 0
        visited = set()

        while self.win == False:

            for i, board2 in enumerate(current_list):
                state = tuple(board2.board.flatten())
                print(len(current_list))
                if state not in visited:
                    visited.add(state)
                    step_count += 1
                    print(step_count)
                    if step_count > max_steps:
                        break
                    print(board2)
                    new_list = self.stack_moves(board2)
                    if new_list:
                        copy_list = deepcopy(new_list)
                        current_list[:0] = copy_list
        if self.win:
            print('The winner is: ')
            print(step_count)
            print(self.winning_board)
            return self.winning_board
        else:
            return None
    # def depth_step(self):
    #     board = Board(self.size, self.car_list)
    #     stack_dict = self.stack_moves(board)
    #
    #     for car in stack_dict.keys():
    #         visited = []
    #
    #         while self.win == False:
    #             visited = stack_dict[car]
    #             self.stack_moves(visited[0])
    #             print(stack_dict)
    #             # stack_moves(stack_dict[car])
