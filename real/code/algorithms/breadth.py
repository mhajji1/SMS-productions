import queue
from copy import deepcopy
from .randomize import RandomAlgorithm
from ..classes.board import Board

class Breadth():

    def __init__(self, depth, size, car_list):
        self.depth = depth
        self.size = size
        self.car_list = car_list



    def every_step(self, board):
        '''
        shows every possible step every car can take
        '''
        board_list = []

        for car in self.car_list:

            # Determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(car)

            # This while loop is to make sure the car does not stay still
            for difference in range(lower_range, upper_range + 1):
                if difference != 0:
                    # adds the difference to the car
                    if car.orientation == 'H':
                        car.col += difference

                    else:
                        car.row += difference

                    board2 = board.draw_board()
                    # print(car.name)
                    # print(board2)

                    # creates a list of multiple loops where every car makes every move it can make
                    board_list.append([car.name, board2])

        print(board_list)
        return board_list

    def check_win(self, board):

        red_car = self.car_list[-1]
        line = board[red_car.row, :]

        for x, i in enumerate(range(red_car.col + red_car.length, self.size)):

            if line[i] != 0:
                return False
        # if all places in front are zero, the game is won
        return True

    def rush_hour(self):
        # Create the initial board object
        board = Board(self.size, self.car_list)
        # Get the initial board state as a numpy array
        board_numpy = board.draw_board()
        # Initialize the queue with the current board state
        q = queue.Queue()
        q.put(board)
        # Keep track of the states we have already visited
        visited = set()

        while not q.empty():
            # Get the next board object from the queue
            current_board = q.get()
            print(current_board)

            """hier heb ik een probleem, die .get() pakt de object en een getal waardoor de rest van de code niet wilt werken"""
            # Get the current board state as a numpy array
            current_board_numpy = current_board.draw_board()
            # Check if the current board state is the goal state
            if self.check_win(current_board_numpy):
                return current_board_numpy
            # Mark the current board state as visited
            visited.add(hash(str(current_board_numpy)))
            # Generate all possible next moves
            for next_board in self.every_step(current_board):
                next_board_numpy = next_board[1]
                # Check if the next board state has already been visited
                if hash(str(next_board_numpy)) not in visited:
                    # Add the next board state to the queue
                    q.put(next_board[0])
