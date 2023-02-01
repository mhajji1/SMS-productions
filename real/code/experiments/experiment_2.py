#------Experiment 2 ---------
"""
description 
"""
  counter = 0

  number_of_moves = []
  low = 100000
  input = 'data/Rushhour6x6_3
  .csv'
  size = 6
  car_list, full_list = open_file2(input)

  l = [False, True]
  combo = list(itertools.product(l, repeat = 4))
  for i in combo:
      label_value = "heuristic used:"
      print(f"{list_of_colours[counter]}")

      if i[0] == True:
          label_value += " endstate"

      if i[1] == True:
          label_value += " manhattan"

      if i[2] == True:
          label_value += " breadth"

      if i[3] == True:
          label_value += " blocking"

      print(label_value)

      test = Astar(full_list, car_list, size, *i)
      visted_states, history, moves = test.run()
      plt.plot(visted_states, history, c=list_of_colours[counter], label=f'{label_value} in {len(moves)} solved')

      counter += 1

  plt.yscale('log')
  plt.title("Memmory growth")
  plt.xlabel("considered states")
  plt.ylabel("number of states")
  plt.legend()
  plt.show()
