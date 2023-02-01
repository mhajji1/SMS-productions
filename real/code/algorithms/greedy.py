import random
from .randomize import RandomAlgorithm
from ..classes.board import Board
from ..classes.car import Car



class Greedy(RandomAlgorithm):

    def __init__(self, full_list, car_list, size):
        super().__init__(full_list, car_list, size)
        self.full_list = full_list
        self.car_list = car_list
        self.size = size
        self.win = False

        self.last_car = None
        self.current_car = None


    def max_step(self, difference, car):
        '''
        This function always moves the maximum amount of steps
        '''
        if car.orientation == 'H':
            car.col += difference
            self.made_moves.append((car.name, difference))
        else:
            car.row += difference
            self.made_moves.append((car.name, difference))


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


    def list_movement(self, board, indeces):
        # only works in one direction
        if indeces == None:
            return False

        random.shuffle(indeces)
        for i in indeces:
            if board.check_movement(self.car_list[i])[0] < 0:
                self.current_car = self.car_list[i]
                return True

        return False


    def return_states(self, length, orientation):
        '''
        This function returns the indeces of cars with the given attributes
        '''
        indeces = []
        for i, car in enumerate(self.car_list):
            if car.length == length and car.orientation == orientation:
                indeces.append(i)

        return indeces


    def main_greedy_5(self, max_iterations = 10000):

        board = Board(self.size, self.car_list)
        car = self.random_car(board)

        vertical_trucks_i = self.return_states(3, 'V')
        horizontal_cars_i = self.return_states(2, 'H')
        horizontal_trucks_i = self.return_states(3, 'H')
        horizontal_i = horizontal_trucks_i.extend(horizontal_cars_i)

        for i in range(max_iterations):

            board.draw_board()

            if board.check_win() == True:
                print(i)
                return self.made_moves

            lower, upper = board.check_movement(board.car_list[-1])
            chance = random.random()

            # if upper > 0 and self.last_car != board.car_list[-1] and chance > 0.98:
            #     self.max_step(upper, board.car_list[-1])
            #     self.last_car = board.car_list[-1]
            #     #print('red')

            if self.list_movement(board, horizontal_cars_i) and self.last_car != self.current_car and chance > 0.6:
                self.max_step(board.check_movement(self.current_car)[0], self.current_car)
                self.last_car = self.current_car
                #print('car')

            elif self.list_movement(board, vertical_trucks_i) and self.last_car != self.current_car and chance > 0.3:
                #print("truck")
                self.max_step(board.check_movement(self.current_car)[0], self.current_car)
                self.last_car = self.current_car

            elif lower < 0 and self.last_car != board.car_list[-1] and chance < 0.1:
                self.max_step(lower, board.car_list[-1])
                self.last_car = board.car_list[-1]
                #print('red')

            else:
                lower_range = 0
                upper_range = 0
                counter = 0
                #print('random')

                while lower_range == 0 and upper_range == 0 or car == self.last_car and counter < 40:

                    car = self.random_car(board)
                    lower_range, upper_range = board.check_movement(car)
                    counter += 1


                if counter >= 40:
                    car = self.last_car
                    lower_range, upper_range = board.check_movement(car)
                self.random_step(lower_range, upper_range, car)
                self.last_car = car


    def main_greedy_4(self, max_iterations = 10000):

        board = Board(self.size, self.car_list)
        car = self.random_car(board)

        vertical_trucks_i = self.return_states(3, 'V')
        horizontal_cars_i = self.return_states(2, 'H')
        horizontal_trucks_i = self.return_states(3, 'H')
        horizontal_i = horizontal_trucks_i.extend(horizontal_cars_i)

        for i in range(max_iterations):

            board.draw_board()

            if board.check_win() == True:

                return self.made_moves

            lower, upper = board.check_movement(board.car_list[-1])
            chance = random.random()

            if upper > 0 and self.last_car != board.car_list[-1] and chance > 0.95:
                self.max_step(upper, board.car_list[-1])
                self.last_car = board.car_list[-1]
                #print('red')

            elif self.list_movement(board, horizontal_cars_i) and self.last_car != self.current_car and chance > 0.4:
                self.max_step(board.check_movement(self.current_car)[0], self.current_car)
                self.last_car = self.current_car


            elif self.list_movement(board, vertical_trucks_i) and self.last_car != self.current_car and chance > 0.2:
                self.max_step(board.check_movement(self.current_car)[0], self.current_car)
                self.last_car = self.current_car


            else:
                lower_range = 0
                upper_range = 0
                counter = 0

                while lower_range == 0 and upper_range == 0 or car == self.last_car and counter < 40:

                    car = self.random_car(board)
                    lower_range, upper_range = board.check_movement(car)
                    counter += 1


                if counter >= 40:
                    car = self.last_car
                    lower_range, upper_range = board.check_movement(car)
                self.random_step(lower_range, upper_range, car)
                self.last_car = car



    def main_greedy_3(self, max_iterations = 10000):
        # make it so every turn a new car is used
        # prioritize the red car moving right
        # focus on other horizontal cars to move left
        # move vertical trucks down
        board = Board(self.size, self.car_list)
        car = self.random_car(board)

        for i in range(max_iterations):

            counter = 0
            lower_range = 0
            upper_range = 0

            board.draw_board()

            if board.check_win() == True:

                return i

            while lower_range == 0 and upper_range == 0 or car == self.last_car and counter < 40:

                car = self.random_car(board)
                lower_range, upper_range = board.check_movement(car)
                counter += 1


            if counter >= 40:
                car = self.last_car
                lower_range, upper_range = board.check_movement(car)

            self.random_step(lower_range, upper_range, car)
            self.last_car = car



    def main_greedy(self, max_iterations = 10000):

        board = Board(self.size, self.car_list)
        counter = 0
        counter_2 = 0

        for i in range(max_iterations):

            lower_range = 0
            upper_range = 0

            board.draw_board()

            if board.check_win() == True:

                return (i)
                break

            lower, upper = board.check_movement(board.car_list[-1])

            if counter_2 > 3 and upper > 0:
                self.max_step(upper, board.car_list[-1])
                counter = 0

            if counter > 3 and lower < 0:
                self.max_step(lower, board.car_list[-1])


            else:
                if upper == 0:
                    counter +=1

                if lower == 0:
                    counter_2 +=1

                while lower_range == 0 and upper_range == 0:
                    car = self.random_car(board)
                    lower_range, upper_range = board.check_movement(car)

                self.random_step(lower_range, upper_range, car)


    def main_greedy_2(self, max_iterations = 4000):

        board = Board(self.size, self.car_list)

        for i in range(max_iterations):

            lower_range = 0
            upper_range = 0

            board.draw_board()

            if board.check_win() == True:

                return (i)
                break

            while lower_range == 0 and upper_range == 0:
                car = self.random_car(board)
                lower_range, upper_range = board.check_movement(car)


            if random.random() > 0.8:

                if upper_range > 0:
                    self.max_step(upper_range, car)
                else:
                    self.max_step(lower_range, car)
            else:

                self.random_step(lower_range, upper_range, car)
