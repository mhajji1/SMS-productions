from ..classes.board import Board
from .breadth import Breadth
from .Astar import Astar, PrioritizedItem
from tqdm import tqdm
from copy import deepcopy

class BA_star():

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.states = {}
        self.history = []
        self.max_step = 35
        self.b_step = 20
        self.win = False
        self.winning_moves = None
        self.count = 0
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
                keys = self.states.keys()

                if state not in keys and len(new_board.moves) < self.max_step:
                    self.states[state] = len(new_board.moves)
                    self.count += 1
                    self.visited_states.append(self.count)
                    self.history.append(len(self.states))

                    board_list.append(new_board)

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return


                elif state in keys and len(new_board.moves) < self.states[state]:
                    self.states[state] = len(new_board.moves)

                    board_list.append(new_board)


                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return
        return board_list



    def initial_states(self):
        # Initialize the depth to 1
        depth = 1

        # Create the initial board and draw it on the board
        board = Board(self.car_list)
        board.draw_board(self.size, self.full_list)

        # Determine all possible states of the board after the first move
        _list = self.every_step(board)

        # Loop until win or depth exceeds the maximum number of steps
        while self.win == False and depth <= self.b_step:
            next_layer = []

            # Loop through all possible states from the previous step
            for individual_board in tqdm(_list):

                # Determine all possible states from the current board state
                temporary_list = self.every_step(individual_board)

                # Add the new states to the next layer
                if temporary_list:
                    next_layer.extend(temporary_list)

            # Update the list of possible states for the next iteration
            _list = next_layer
            depth += 1

        # Return the final list of possible states
        return _list

    def run(self, with_breadth=False):
        # Flag to indicate if the loop should stop
        stop = False

        # Initialize the list of board states based on the with_breadth flag
        if with_breadth == True:
            board_list = self.initial_states()
        else:
            board = Board(self.car_list)
            board.draw_board(self.size, self.full_list)
            board_list = self.every_step(board)

        # Create a copy of the initial list of board states
        current_list = deepcopy(board_list)

        # Continue looping until the stop flag is set to True
        while stop == False:

            # Continue looping until the win flag is set to True
            if self.win == False:
                # Check if there are any states in the current list
                if len(current_list) > 0:
                    # Get the next state from the current list
                    board2 = current_list.pop()

                    new_list = []

                    # Check if the number of moves for the current state is less than the max_step
                    if len(board2.moves) <= self.max_step:
                        # Determine all possible states from the current state
                        new_list = self.every_step(board2)

                        # Add the new list of states to the current_list
                        if new_list:
                            current_list.extend(new_list)

                else:
                    # If the current_list is empty, print the best result and set the stop flag to True
                    print(f'best result is: {len(self.winning_moves)}')
                    stop = True

            else:
                # If the win flag is set to True, print the winner details and update the max_step
                print('FOUND WINNER')
                print(len(self.winning_moves))
                print(self.winning_moves)
                self.found_winner = True

                if len(self.winning_moves) < self.max_step:
                    self.max_step = len(self.winning_moves)
                self.win = False

        # Return the list of visited states, unique states, and winning moves
        return self.visited_states, self.history, self.winning_moves
