from code.algorithms.randomize import RandomAlgorithm
from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth
from code.classes.car import Car, RedCar
from code.visualisation.visualize import visualise
from tqdm import tqdm
import pandas as pd


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


if __name__ == '__main__':




    # --------------------------- Random movement --------------------------
    # for i in range(1000):
    #     car_list_1 = open_file('data/Rushhour6x6_2.csv')
    #     test = RandomAlgorithm(car_list_1, 6)
    #     test.main_random(100000)
    #     number_of_moves.append(len(test.made_moves))
    # print(test.made_moves)
    #
    # #perform analysis
    # import matplotlib.pyplot as plt
    # #make the average
    # average = sum(number_of_moves)/len(number_of_moves)
    # max = max(number_of_moves)
    # min = min(number_of_moves)
    # print(f"the average number of moves is {average}, the maximum total moves is {max} and the least number of moves is {min}")
    #
    # # plot the values on a graph
    # plt.hist(number_of_moves, bins = 100)
    # plt.title("distribution of means")
    # plt.xlabel("the number of moves until it's in the winning position")
    # plt.ylabel("the number of simuilations at a given position")
    #
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
    input = 'data/Rushhour6x6_2.csv'
    size = 6

    car_list_1 = open_file(input)
    test = Breadth(car_list_1, size)
    test.run()



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
