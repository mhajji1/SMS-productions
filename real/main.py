# from code.algorithms.randomize import RandomAlgorithm
from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth
from code.algorithms.branch_and_bound import BB
from code.algorithms.Astar import Astar
from code.algorithms.depth import Depth
#from code.algorithms.Astar_update import Astar
from code.classes.car import Car
from code.visualisation.visualize import visualise
from tqdm import tqdm
import pandas as pd
import time
import argparse
import itertools
import matplotlib.pyplot as plt


def open_file2(input):
    data = pd.read_csv(input)
    car_list = []
    other_list = []

    for key, line in data.iterrows():
        if line['orientation'] == 'H':
            car_list.append(line['col'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1, 'ok')
            other_list.append(key)
        else:
            car_list.append(line['row'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1, 'ok')
            other_list.append(key)





    return car_list, other_list

class main():

    def __init__(self, algorithm_name, board_number):
        self.algorithm_name = algorithm_name
        self.board_number = board_number


    def run_algorithms(self):
        algorithm_list = ["RandomAlgorithm", "Greedy", "Breadth", "Depth", "Astar", "BB"]
        starting_boards = {"Rushhour6x6_1.csv": 6, "Rushhour6x6_2.csv": 6
        , "Rushhour6x6_3.csv": 6, "Rushhour9x9_4.csv": 9, "Rushhour9x9_5.csv":9,
         "Rushhour9x9_6.csv":9, "Rushhour12x12_7.csv":12}


        for i, algorithm in enumerate(algorithm_list):
            if self.algorithm_name == algorithm:
                print(algorithm)
                index = i

        for i, board_file in enumerate(starting_boards.keys()):
            if self.board_number - 1 == i:
                file = board_file
                size = starting_boards[board_file]


        car_list, full_list = open_file2(f"data/{file}")

# ---------------------------------- Random ------------------------------------
        if index == 0:
            random_model = RandomAlgorithm(full_list, car_list, size)
            start = time.time()
            moves = random_model.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")
            visualise(moves, open_file2(input)[1], size)

# ---------------------------------- Greedy ------------------------------------
        if index == 1:
            greedy = Greedy(full_list, car_list, size)
            start = time.time()
            moves = greedy.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")
        #
# ---------------------------------- Breadth -----------------------------------
        if index == 2:
            breadth = Breadth(full_list, car_list, size)
            start = time.time()
            moves = breadth.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")
            visualise(moves, open_file2(input)[1], size)

# ------------------------------- Branch & Bound -------------------------------
        if index == 3:
            branch_and_bound = BB(full_list, car_list, size)
            start = time.time()
            moves = branch_and_bound.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")
            visualise(moves, open_file2(input)[1], size)

# ---------------------------------- Astar -------------------------------------
        if index == 4:
            astar = Astar(full_list, car_list, size)
            start = time.time()
            moves = astar.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")

# ---------------------------------- Astar -------------------------------------
        if index == 5:
            BA = BA_star(full_list, car_list, size)
            start = time.time()
            moves = BA.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")
            print(moves)

if __name__ == '__main__':

    # # Set-up parsing command line arguments
    # parser = argparse.ArgumentParser(description = "solve the rush hour puzzle")
    #
    # # Adding arguments
    # parser.add_argument("algorithm_name", help = "algoritm name")
    # parser.add_argument("-b", "--board_number",   type=int, default =1 , help="chooses board_file from 1 to 7 (default: 1)")
    # # parser.add_argument("-s", "--size",   type=int, default =6 , help="board size (default: 6)")
    #
    #
    #
    # # Read arguments from command line
    # args = parser.parse_args()
    #
    # # Run main with provide arguments
    # test = main(args.algorithm_name, args.board_number)
    # test.run_algorithms()

# ------------------------------------------------------------------------------
    # number_of_moves = []
    # low = 100000
    # input = 'data/Rushhour12x12_7.csv'
    # size = 12

    counter = 0
    # list_of_colours = [[1.0, 0.7019607843137254, 0.0], [0.5019607843137255, 0.24313725490196078, 0.4588235294117647], [1.0, 0.40784313725490196, 0.0], [0.6509803921568628, 0.7411764705882353, 0.8431372549019608], [0.7568627450980392, 0.0, 0.12549019607843137], [0.807843137254902, 0.6352941176470588, 0.3843137254901961], [0.5058823529411764,0.4392156862745098, 0.4], [0.0, 0.49019607843137253, 0.20392156862745098], [0.9647058823529412, 0.4627450980392157, 0.5568627450980392], [0.0, 0.3254901960784314, 0.5411764705882353], [1.0, 0.47843137254901963, 0.3607843137254902], [0.3254901960784314, 0.21568627450980393, 0.47843137254901963], [1.0, 0.5568627450980392, 0.0], [0.7019607843137254, 0.1568627450980392, 0.3176470588235294], [0.9568627450980393, 0.7843137254901961, 0.0], [0.4980392156862745, 0.09411764705882353, 0.050980392156862744], [0.5764705882352941, 0.6666666666666666, 0.0], [0.34901960784313724, 0.2, 0.08235294117647059], [0.9450980392156862, 0.22745098039215686,0.07450980392156863], [0.13725490196078433, 0.17254901960784313, 0.08627450980392157]]
    number_of_moves = []
    low = 100000
    input = 'data/Rushhour6x6_2.csv'

    size = 6
    car_list, full_list = open_file2(input)

    # start = time.time()
    # test = BB(full_list, car_list, size)
    # visted_states, history, moves = test.run(with_breadth = True)
    # end = time.time()
    # print(f"The processing time for this board was: {end - start}")
    # plt.plot(visted_states, history, label='breadth & branch and bound')

    start = time.time()
    test = BB(full_list, car_list, size)
    visted_states, history, moves = test.run()
    end = time.time()
    print(f"The processing time for this board was: {end - start}")
    plt.plot(visted_states, history, label='branch and bound')

    # start = time.time()
    # test = Depth(full_list, car_list, size)
    # visted_states, history, moves = test.run()
    # end = time.time()
    # print(f"The processing time for this board was: {end - start}")
    # plt.plot(visted_states, history, label='Iterative deepening')


    # plt.yscale('log')
    plt.title("Memory growth")
    plt.xlabel("considered states")
    plt.ylabel("number of states")
    plt.legend()
    plt.show()




    # test = Astar(full_list, car_list, size)
    # moves = test.run()
    #
    # visualise(moves, open_file2(input)[1], size)
    #final_board = mode(endstates)
    #print(final_board)
    #print(test.made_moves)

    # test = BB(full_list, car_list, size)
    #
    # start = time.time()
    # moves = test.run()
    # end = time.time()
    # print(f"The processing time for this board was: {end - start}")
    # visualise(moves, open_file2(input)[1], size)

    #
    # import matplotlib.pyplot as plt
    # #make the average
    # average = sum(number_of_moves)/len(number_of_moves)
    # max = max(number_of_moves)
    # min = min(number_of_moves)
    # print(f"the average number of moves is {average}, the maximum total moves is {max} and the least number of moves is {min}")

    #[(11, 1), (10, 1), (8, 3), (10, -1), (13, -1), (7, 1), (3, -1), (14, -2), (15, -2), (11, 1), (12, -1), (21, 1), (22, -2), (19, 1), (11, 3), (19, -1), (22, 2)]
