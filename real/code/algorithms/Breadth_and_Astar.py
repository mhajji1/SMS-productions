from ..classes.board import Board
from .breadth import Breadth
from .Astar import Astar, PrioritizedItem
from tqdm import tqdm
from copy import deepcopy
from .Astar import Astar

from tqdm import tqdm

from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
import ast
import copy
import numpy as np


class BA_star():

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.states = {}
        self.max_step = 20
        self.win = False
        self.winning_moves = None

    def every_step(self, board):
        '''
        shows every possible step every car can take
        '''

        board_list = []
        for car_number, car in enumerate(self.full_list):

            # Determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(self.size, car, car_number)
            #print(car_number + 1, lower_range, upper_range)

            # This while loop is to make sure the car does not stay still
            for difference in [*range(lower_range, 0),  *range(1, upper_range + 1)]:


                # adds the difference to the car
                new_board = deepcopy(board)
                # new_board.add_move(car_number, difference)
                # state = str(new_board.draw_board(self.size, self.full_list, return_board = True))
                state = new_board.update_board(car_number, car, difference)
                keys = self.states.keys()

                if state not in keys and len(new_board.moves) < self.max_step:
                    self.states[state] = len(new_board.moves)

                    board_list.append(new_board)

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return


                elif state in keys and len(new_board.moves) < self.states[state]:
                    self.states[state] = len(new_board.moves)
                    # self.queue.put(PrioritizedItem(self.calculate(new_board),new_board))

                    board_list.append(new_board)

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return

        return board_list



    def initial_states(self):
        depth = 1
        board = Board(self.car_list)
        board.draw_board(self.size, self.full_list)
        _list = self.every_step(board)

        while self.win == False and depth <= 10:
            print(depth)
            next_layer = []

            for individual_board in tqdm(_list):

                temporary_list = self.every_step(individual_board)
                next_layer.extend(temporary_list)

            _list = next_layer
            depth += 1

        else:
            # print(self.states.values())
            # print(self.winning_moves)
            return _list

    def run(self):

        test = Astar(self.full_list, self.car_list, self.size)

        test.queue.put((PrioritizedItem(test.calculate(i), i) for i in self.initial_states()))
        test.states = self.states
        test.run()
