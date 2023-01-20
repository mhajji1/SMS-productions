import queue
from copy import deepcopy
from .randomize import RandomAlgorithm
from ..classes.board import Board
from tqdm import tqdm

class Breadth():

    def __init__(self, car_list, size):
        # self.depth = depth
        self.size = size
        self.car_list = car_list
        self.win = False
        self.winning_board = None



    def every_step(self, board):
        '''
        shows every possible step every car can take
        '''
        board_list = []

        board.draw_board()

        for i, car in enumerate(board.car_list):

            # Determines the possible movements the car can take
            lower_range, upper_range = board.check_movement(car)
            # print(car.name, lower_range, upper_range)

            # This while loop is to make sure the car does not stay still
            for difference in range(lower_range, upper_range + 1):
                if difference != 0:

                    # adds the difference to the car
                    board2 = deepcopy(board)

                    if car.orientation == 'H':
                        board2.car_list[i].col += difference

                    else:
                        board2.car_list[i].row += difference

                    board2.draw_board()
                    if board2.check_win():
                        self.win = True
                        self.winning_board = board2.board
                        return
                    # creates a list of multiple loops where every car makes every move it can make
                    board_list.append(board2)

        return board_list



    def run(self):
        counter = 1

        board = Board(self.size, self.car_list)
        _list = self.every_step(board)

        while self.win == False:

            next_layer = []
            counter += 1
            print(counter)

            for individual_board in tqdm(_list):
                # if counter == 2:
                #     print(individual_board)

                temporary_list = self.every_step(individual_board)
                next_layer.extend(temporary_list)
                #print(next_layer)

            _list = next_layer
            print(len(_list))




    def rush_hour(self):
        # Create the initial board object
        board = Board(self.size, self.car_list)
        # Get the initial board state as a numpy array

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
