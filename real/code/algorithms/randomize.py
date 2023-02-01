import random
from ..classes.board import Board
from ..classes.car import Car


class RandomAlgorithm:

    def __init__(self, full_list, car_list, size):
        self.full_list = full_list
        self.car_list = car_list
        self.size = size
        self.win = False


    def random_car(self, board):
        '''
        This function picks a random car
        '''
        random_index = random.randrange(len(board.car_list))
        #car = board.full_list[random_index]

        return random_index


    def random_step(self, lower_range, upper_range):
        '''
        Take a random step within a range of free spaces
        '''

        # This while loop is to make sure the car does not stay still
        difference = 0

        while difference == 0:
            difference = random.randrange(lower_range, upper_range + 1)

        # return the difference
        return difference


    def run(self, max_iterations = 100000):
        '''
        This function runs all commands in order to run the random simulation
        '''

        self.board = Board(self.car_list, [])

        while self.win == False:

            lower_range = 0
            upper_range = 0

            self.board.draw_board(self.size, self.full_list)

            if self.board.check_win(self.size, self.full_list[-1]):
                self.win = True
                #print(len(board.moves))

                return self.car_list

            while lower_range == 0 and upper_range == 0:
                car_number = self.random_car(self.board)
                lower_range, upper_range = self.board.check_movement(self.size, self.full_list[car_number], car_number)

            difference = self.random_step(lower_range, upper_range)

            self.board.add_move(car_number, difference)
