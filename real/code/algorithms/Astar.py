from copy import deepcopy
from ..classes.board import Board
from tqdm import tqdm
import heapq
from tqdm import tqdm

#

class Astar():

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.win = False
        self.states = {}
        self.winning_moves = None
        self.max_step = 100

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

                    new_board.score = self.calculate(new_board)
                    self.states[state] = len(new_board.moves)

                    board_list.append(new_board)


                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return [0]


                elif state in keys and len(new_board.moves) < self.states[state]:
                    new_board.score = self.calculate(new_board)
                    self.states[state] = len(new_board.moves)

                    board_list.append(new_board)


                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return [0]


        return board_list



    def calculate(self, board):
        """
        In this function we can implement heuristics to improve the breadth first searh
        1. heuristic: check the first car of cars which blocks the red car
        2. heuristic: manhattan distance (how far is the red car from the exit)
        3. heuristic: check the depth of the board it's found

        Calculate number of cars blocking the way for the red car
        This function only works when the board has been drawn
        """
        score = 0
        extra = 0

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

            #adding the manhattan distance
            manhattan_distance = self.size - (red_car+ 1)

            #adding the number of steps already taken
            steps_taken = len(board.moves)

            #adding the number of intersections in the puzzle
            # for i in board.car_list:
            #     counter += i.check_movement()

            cost_function = min_score + len(numbers) - manhattan_distance + steps_taken

            return cost_function

        else:
            return 0

    def run(self):
        new_list = []
        board = Board(self.car_list)
        board.draw_board(self.size, self.full_list)

        _list = self.every_step(board)

        board.score = self.calculate(board)
        # board.score_2 = self.heuristic_1(board)

        while self.win == False:

            value = min([x.score for x in _list])

            lowest_state = []
            other_states = []
            for x in _list:
                if x.score == value:
                    lowest_state.append(x)
                else:
                    other_states.append(x)

            for individual_board in tqdm(lowest_state):
                temporary_list = self.every_step(individual_board)
                #create scores for all the boards

                if self.win == True:

                    self.max_step = len(self.winning_moves) - 1
                    print(self.winning_moves)
                    # self.win = False
                    return self.winning_moves

                #start from the one with the lowest score
                # REMOVE THE LOWEST SCORES
                other_states.extend(temporary_list)

            _list = other_states
