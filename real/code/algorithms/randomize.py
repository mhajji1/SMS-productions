import random
from ..classes.board import Board
from ..classes.car import Car, RedCar
# from code.classes.car import RedCar


class RandomAlgorithm:

    def __init__(self, car_list, size):
        self.car_list = car_list
        self.size = size
        self.made_moves = []

    def random_car(self, board):
        '''
        This function picks a random car
        '''
        random_index = random.randrange(len(board.car_list))
        car = board.car_list[random_index]

        return car


    def random_step(self, lower_range, upper_range, car):
        '''
        Take a random step within a range of free spaces
        '''

        # This while loop is to make sure the car does not stay still
        difference = 0

        while difference == 0:
            difference = random.randrange(lower_range, upper_range + 1)

        # add the difference to the car
        if car.orientation == 'H':
            car.col += difference
            self.made_moves.append((car.name, difference))
        else:
            car.row += difference
            self.made_moves.append((car.name, difference))



    def main_random(self, max_iterations = 10):
        '''
        This function runs all commands in order to run the random simulation
        '''

        board = Board(self.size, self.car_list)

        for i in range(max_iterations):

            lower_range = 0
            upper_range = 0
 
            board.draw_board()

            if board.check_win() == True:
                print(i)
                break

            while lower_range == 0 and upper_range == 0:
                car = self.random_car(board)
                lower_range, upper_range = board.check_movement(car)

            self.random_step(lower_range, upper_range, car)
