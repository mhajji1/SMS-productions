# ---- Experiment 1 -----
"""
description
"""
#random
number_of_moves = []
low = 100000
input = 'data/Rushhour6x6_1.csv'
size = 6

number_of_moves =[]

for i in range(1000):
    print(i)
    car_list, full_list = open_file2(input)
    i = Greedy(full_list, car_list, size)
    moves = i.run()
    print(len(moves))
    number_of_moves.append(len(moves))
print(number_of_moves)


plt.hist(number_of_moves)
plt.title("")
plt.xlabel("")
plt.ylabel("number of states")
plt.legend()
plt.show()
