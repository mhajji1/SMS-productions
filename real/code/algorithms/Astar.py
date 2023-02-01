from copy import deepcopy
from ..classes.board import Board
from ..algorithms.randomize import RandomAlgorithm

from tqdm import tqdm

from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
import ast
import copy
import numpy as np


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class Astar():
    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.win = False
        self.states = {}
        self.winning_moves = None
        self.max_step = 100
        self.queue = PriorityQueue()

    def every_step(self, board):
        """
        creates every possible state for a given board
        """

        for car_number, car in enumerate(self.full_list):

            # Determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(self.size, car, car_number)

            # This while loop is to make sure the car does not stay still
            for difference in [*range(lower_range, 0),  *range(1, upper_range + 1)]:

                # adds the difference to the car
                new_board = deepcopy(board)
                state = new_board.update_board(car_number, car, difference)
                keys = self.states.keys()

                if state not in keys and len(new_board.moves) < self.max_step:

                    self.states[state] = len(new_board.moves)
                    self.queue.put(PrioritizedItem(self.calculate(new_board),new_board))

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves

                elif state in keys and len(new_board.moves) < self.states[state]:

                    self.states[state] = len(new_board.moves)
                    self.queue.put(PrioritizedItem(self.calculate(new_board),new_board))

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves

    def calculate(self, board):
        """
        In this function we can implement heuristics to improve the breadth first search
        1. heuristic: check the first car of cars which blocks the red car (and all the other cars which block red)
        2. heuristic: manhattan distance (how far is the red car from the exit)
        3. heuristic: check the depth at which the board is found
        4. heuristic: end_state, makes a score based on the difference between the coordinates of the current board and the end board
            this is a board which is the most common end board for 100 random simulation
        """
        cost_function = 0
        red_car = board.car_list[-1]

        # plus two because of the length of the red car
        numbers = set(board.board[self.full_list[-1].row, red_car+self.full_list[-1].length:])
        numbers.discard(0)

        if len(numbers) > 0:
            i = list(numbers)[0]

            #car_list[i-1] is the car object
            car = self.full_list[i-1]

            upper = set(board.board[board.car_list[i-1]+car.length:, car.col])
            lower = set(board.board[:car.row-1, car.col])
            upper.discard(0)
            lower.discard(0)
            min_score = min([len(lower),len(upper)])
            cost_function += min_score

        #The manhattan distance
        manhattan_distance = self.size - (red_car + 1)

        #The number of steps already taken
        steps_taken = len(board.moves)

        cost_function += manhattan_distance + len(numbers) + self.priority(board) + steps_taken

        return cost_function


    def deterimine_end_state(self, itterations = 100):
        """
        This function creates an array of the end states of x amount of itterations
        """

        endstates = []

        for i in range(itterations):
            carlist = deepcopy(self.car_list)
            test = RandomAlgorithm(self.full_list, carlist, self.size)
            endstate = test.run(1000000)

            endstates.append(str(endstate))


        self.common_end = np.array(ast.literal_eval(max(set(endstates), key=endstates.count)))


    def priority(self, board):
        """
        creates the most common end board (use the mode)
        """
        return np.sum(np.absolute(np.array(board.car_list) - self.common_end))


    def run(self):
        """
        The main running function which can be called upon in the main class
        """

        self.deterimine_end_state()
        board = Board(self.car_list)
        board.draw_board(self.size, self.full_list)

        self.queue.put(PrioritizedItem(self.calculate(board), board))


        while self.win == False:
            self.every_step(self.queue.get().item)

            if self.win == True:

                self.max_step = len(self.winning_moves) - 1

                #if you turn self.win to true you can create an alogirthm which also checks if the given solution is the best (effectively a breadth search backwards)
                # self.win = False
                return self.winning_moves
