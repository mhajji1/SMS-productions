from code.algorithms.randomize import RandomAlgorithm
from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth
from code.algorithms.Astar import Astar
# from code.algorithms.Breadth_and_Astar import BA_star
#from code.algorithms.Astar_update import Astar
from code.classes.car import Car
from code.visualisation.visualize import visualise
from tqdm import tqdm
import pandas as pd
import time
import matplotlib.pyplot as plt
import argparse



def open_file2(input):
    '''
    This function loads the csv into two list
    '''
    data = pd.read_csv(input)
    car_list = []
    other_list = []

    for key, line in data.iterrows():
        if line['orientation'] == 'H':
            car_list.append(line['col'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1, line['car'])
            other_list.append(key)
        else:
            car_list.append(line['row'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1, line['car'])
            other_list.append(key)

    return car_list, other_list


def convert_output(full_list, moves):
    '''This function changes the algorithm integers back to the official car names, 1 -> A etc.'''
    car_name = []
    step = []
    for i, move in enumerate(moves):
        car_name.append(full_list[move[0]-1].signature)
        step.append(move[1])
    output = pd.DataFrame(list(zip(car_name, step)), columns =['Car', 'Move'])
    output.to_csv('output/output.csv', index=False)
    print("Saved output in output")


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

# ---------------------------------- Breadth -----------------------------------
        if index == 2:
            breadth = Breadth(full_list, car_list, size)
            start = time.time()
            moves = breadth.run()
            end = time.time()
            print(moves)
            print(f"The processing time for this board was: {end - start}")
            visualise(moves, open_file2(f"data/{file}")[1], size)

# ------------------------------- Branch & Bound -------------------------------
        if index == 3:
            branch_and_bound = BB(full_list, car_list, size)
            start = time.time()
            moves = branch_and_bound.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")
            visualise(moves, open_file2(f"data/{file}")[1], size)

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

        # visualise(moves, open_file2(input)[1], size)


if __name__ == '__main__':

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "solve the rush hour puzzle")

    # Adding arguments
    parser.add_argument("algorithm_name", help = "algoritm name")
    parser.add_argument("-b", "--board_number",   type=int, default =1 , help="chooses board_file from 1 to 7 (default: 1)")
    # parser.add_argument("-s", "--size",   type=int, default =6 , help="board size (default: 6)")



    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    test = main(args.algorithm_name, args.board_number)
    test.run_algorithms()












# ---------------------------------- check frequency of endstates for random ------------------------------------
    # endstate = []
    # for i in range(100):
    #     print(i)
    #     car_list, full_list = open_file2(input)
    #     i = RandomAlgorithm(full_list, car_list, size)
    #     end_board = i.run()
    #     endstate.append(f"{end_board}")
    # print(endstate)
    # frequency = {}
    # # iterating over the list
    # for item in endstate:
    #    # checking the element in dictionary
    #    if item in frequency:
    #       # incrementing the counr
    #       frequency[item] += 1
    #    else:
    #       # initializing the count
    #       frequency[item] = 1
    # print(frequency)
    # plt.hist(list(frequency.values()), bins= 100)
    # plt.title("Distribution of endstates of random")
    # plt.xlabel("boord configuraties")
    # plt.ylabel("number of iterations")
    # plt.show()


#-----------------------------------experiment ---------------------------------
# for i in range(1000):
#     print(i)
#     car_list, full_list = open_file2(input)
#     i = RandomAlgorithm(full_list, car_list, size)
#     i.run()
#     moves = i.board.moves
#     number_of_moves.append(len(moves))
# print(number_of_moves)
#
#
# plt.hist(number_of_moves, bins=35)
# plt.title("Distribution of random")
# plt.xlabel("number of moves")
# plt.ylabel("number of iterations")
# plt.legend()
# plt.show()

# ---------------------------------- Random ------------------------------------
# random_model = RandomAlgorithm(full_list, car_list, size)
# start = time.time()
# moves = random_model.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
# visualise(moves, open_file2(input)[1], size)

# ---------------------------------- Greedy ------------------------------------
# greedy = Greedy(full_list, car_list, size)
# start = time.time()
# moves = greedy.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
#
# ---------------------------------- Breadth -----------------------------------
# _list = []
# for i in range(100):
#     print(i)
#     car_list, full_list = open_file2(input)
#     astar = RandomAlgorithm(full_list, car_list, size)
#     start = time.time()
#     moves = astar.run()
#     _list.append(len(moves))
# print(sum(_list)/len(_list))

# ------------------------------- Branch & Bound -------------------------------
# branch_and_bound = BB(full_list, car_list, size)
# start = time.time()
# moves = branch_and_bound.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
# visualise(moves, open_file2(input)[1], size)

# ---------------------------------- Astar -------------------------------------
# astar = Astar(full_list, car_list, size)
# start = time.time()
# moves = astar.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
# print(convert_output(full_list, moves))

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
