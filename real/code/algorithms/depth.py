from ..classes.board import Board
import queue
from copy import deepcopy
from .randomize import RandomAlgorithm
from collections import deque
from tqdm import tqdm

class Depth():

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.states = set()
        self.max_step = 10
        self.win = False
        self.winning_moves = None
        self.count = 0
        self.history = []
        self.visited_states = []

    def every_step(self, board):
        '''
        shows every possible step every car can take
        '''

        board_list = []
        for car_number, car in enumerate(self.full_list):

            # Determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(self.size, car, car_number)

            # This while loop is to make sure the car does not stay still
            for difference in [*range(lower_range, 0),  *range(1, upper_range + 1)]:


                # adds the difference to the car
                new_board = deepcopy(board)
                # new_board.add_move(car_number, difference)
                state = str(new_board.update_board(car_number, car, difference))
                # print(state)

                if state not in self.states:
                    self.states.add(state)

                    self.count += 1
                    self.visited_states.append(self.count)
                    self.history.append(len(self.states))

                    board_list.append(new_board)

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        print(f'WINNER:{len(self.winning_moves)}')
                        # return something
                        return []

        return board_list

    def step_size(self):
        if self.size == 6:
            return 5
        else:
            return 10


    def run(self, with_breadth=False):
        # Flag to indicate if the loop should stop
        stop = False

        # Initialize the list of board states based on the with_breadth flag
        board = Board(self.car_list)
        board.draw_board(self.size, self.full_list)
        board_list = self.every_step(board)
        partial_list = []

        # Create a copy of the initial list of board states
        current_list = deepcopy(board_list)

        # Continue looping until the stop flag is set to True
        while self.win == False:
            # Check if there are any states in the current list
            if len(current_list) > 0:
                # Get the next state from the current list
                board2 = current_list.pop()
                # print(board2)

                new_list = []

                # Check if the number of moves for the current state is less than the max_step
                if len(board2.moves) <= self.max_step:
                    # Determine all possible states from the current state
                    new_list = self.every_step(board2)

                else:

                    partial_list.extend(self.every_step(board2))
                    # print(partial_list)

                # Add the new list of states to the current_list
                if new_list:
                    current_list.extend(new_list)

            elif self.winning_moves == None:

                    self.max_step += self.step_size()
                    print(self.max_step)
                    current_list.extend(partial_list)
                    partial_list = []

        # Return the list of visited states, unique states, and winning moves
        return self.visited_states, self.history, self.winning_moves
