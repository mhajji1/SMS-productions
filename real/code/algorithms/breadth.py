from copy import deepcopy
from ..classes.board import Board
from tqdm import tqdm
import functools
import operator
import numpy as np

class Breadth():

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.win = False
        self.states = set()
        self.winning_moves = None


    def generate_next_states(self, board):
        '''
        shows every possible step every car can take
        '''

        next_states = []
        np_board = board.draw_board(self.size, self.full_list)[1]

        for car_number, car in enumerate(self.full_list):

            # determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(self.size, car, car_number, np_board)

            # check all possible options per car, except 0 (no movement)
            for difference in [*range(lower_range, 0),  *range(1, upper_range + 1)]:

                # copy the numpy board
                np_new = np.copy(np_board)
                new_board = deepcopy(board)

                # adds the difference to the car
                state, np_board2 = new_board.update_board(car_number, car, difference, np_new)

                # check the archive
                if state not in self.states:
                    next_states.append(new_board)
                    self.states.add(state)

                    if new_board.check_win(self.size, self.full_list[-1], np_board2):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something so run() keeps working
                        return [0]

        return next_states


    def run(self):
        '''
        This function runs all commands necessary for each breadth layer
        '''

        # create the starting state
        board = Board(self.car_list)
        # add to archive
        state, np_board = board.draw_board(self.size, self.full_list)
        self.states.add(state)
        # create all next states
        _list = self.generate_next_states(board)

        while self.win == False:
            next_layer = []

            for individual_board in tqdm(_list):
                next_layer.extend(self.generate_next_states(individual_board))

            _list = next_layer

        else:
            return self.winning_moves
