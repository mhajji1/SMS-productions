from copy import deepcopy
from ..classes.board import Board


class Breadth():
    '''
    This Algorithm goes through all next possibilities till the best solution is found
    '''

    def __init__(self, full_list, car_list, size):
        self.size = size
        self.full_list = full_list
        self.car_list = car_list
        self.win = False
        self.states = set()
        self.winning_moves = None


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


                new_board = deepcopy(board)
                # adds the difference to the car
                state = new_board.update_board(car_number, car, difference)

                if state not in self.states:
                    board_list.append(new_board)
                    self.states.add(state)

                    if new_board.check_win(self.size, self.full_list[-1]):
                        self.win = True
                        self.winning_moves = new_board.moves
                        # return something
                        return [0]

        return board_list


    def run(self):
        '''
        This function runs all methods to run the Breadth First Algorithm with archive
        '''

        board = Board(self.car_list)
        self.states.add(board.draw_board(self.size, self.full_list))
        _list = self.every_step(board)

        while self.win == False:

            next_layer = []

            for individual_board in _list:

                temporary_list = self.every_step(individual_board)
                next_layer.extend(temporary_list)

            _list = next_layer

        else:
            return self.winning_moves
