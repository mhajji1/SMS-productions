from code.algorithms.randomize import RandomAlgorithm
from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth
from code.algorithms.depth import BB
#from code.algorithms.Astar import Astar
from code.algorithms.Astar_update import Astar
from code.classes.car import Car, RedCar
from code.visualisation.visualize import visualise
from tqdm import tqdm
import pandas as pd
import time


def open_file(input):
    data = pd.read_csv(input)
    _list = []

    for key, line in data.iterrows():
        if line['car'] != 'X':
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1)
            _list.append(key)
        else:
            key = RedCar(line['orientation'], line['col'], line['row'], line['length'], key + 1)
            _list.append(key)

    return _list

def open_file2(input):
    data = pd.read_csv(input)
    car_list = []
    other_list = []

    for key, line in data.iterrows():
        if line['orientation'] == 'H':
            car_list.append(line['col'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1)
            other_list.append(key)
        else:
            car_list.append(line['row'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1)
            other_list.append(key)



    return car_list, other_list


if __name__ == '__main__':




    # # --------------------------- Random movement --------------------------
    # number_of_moves = []
    # for i in range(1):
    #     car_list_1 = open_file('data/Rushhour9x9_5.csv')
    #     test = RandomAlgorithm(car_list_1, 9)
    #     test.main_random(1000000)
    #     number_of_moves.append(len(test.made_moves))
    # print(test.made_moves)
    #
    # import matplotlib.pyplot as plt
    # #make the average
    # average = sum(number_of_moves)/len(number_of_moves)
    # max = max(number_of_moves)
    # min = min(number_of_moves)
    # print(f"the average number of moves is {average}, the maximum total moves is {max} and the least number of moves is {min}")
    #
    # number_of = []
    # for i in range(200):
    #     car_list_1 = open_file('data/Rushhour6x6_2.csv')
    #     test = Breadth(car_list_1, 6)
    #     test.run()
    #     number_of.append(len(test.made_moves))
    #
    # average = sum(number_of)/len(number_of)
    # print(f"the average number of moves is {average}, the maximum total moves is {max} and the least number of moves is {min}")
    #
    # #perform analysis
    #
    # # plot the values on a graph
    # plt.hist(number_of_moves, bins = 100, alpha=0.5)
    # plt.hist(number_of, bins=100, alpha=0.5)
    # plt.title("distribution of means")
    # plt.xlabel("the number of moves until it's in the winning position")
    # plt.ylabel("the number of simuilations at a given position")
    # #
    # plt.show()

    # number_of_moves = []
    # low = 100000
    # for i in tqdm(range(2000)):
    #
    #     car_list_1 = open_file('data/Rushhour6x6_2.csv')
    #     test = Greedy(car_list_1, 6)
    #     output = test.main_greedy_4(100000)
    #     if output != None:
    #         if output < low:
    #
    #             low = output
    #             moves = test.made_moves
    #
    #     number_of_moves.append(len(test.made_moves))

    number_of_moves = []
    low = 100000
    input = 'data/Rushhour9x9_5.csv'
    size = 9

    # car_list_1 = open_file(input)
    # test = Breadth(car_list_1, size)
    # moves = test.run()
    # visualise(moves, open_file(input), size)

    car_list, full_list = open_file2(input)
    test = Astar(full_list, car_list, size)
    start = time.time()
    moves = test.run()
    end = time.time()
    print(f"The processing time for this board was: {end - start}")
    visualise(moves, open_file2(input)[1], size)

#[(11, 1), (10, 1), (8, 3), (10, -1), (13, -1), (7, 1), (3, -1), (14, -2), (15, -2), (11, 1), (12, -1), (21, 1), (22, -2), (19, 1), (11, 3), (19, -1), (22, 2)]

    # for i in tqdm(range(100)):
    #
    #     car_list_1 = open_file(input)
    #     test = Greedy(car_list_1,size)
    #     output = test.main_greedy_5()
    #     if output != None:
    #         if output < low:
    #             print(output)
    #             low = output
    #             moves = test.made_moves
    #
    #     number_of_moves.append(len(test.made_moves))
    #
    #
    # print(f"The lowest amount of moves was {low}")
    # average = sum(number_of_moves)/len(number_of_moves)
    # print(f"the average number of moves is {average}")
    # visualise(moves, open_file(input), size)
