import networkx

def mapCave(depth, size):
  x_size, y_size = size
  cave = {}

  for y in range(y_size+1):
    for x in range(x_size+1):
      if y == 0:
        geologic_index = x * 16807
      elif x == 0:
        geologic_index = y * 48271
      else:
        geologic_index = cave[(x-1, y)] * cave[(x, y-1)]
      cave[(x, y)] = ((geologic_index + depth) % 20183)

  cave[(x_size, y_size)] = (0 + depth) % 20183

  # returns rock type and risk level
  for y in range(y_size+1):
    for x in range(x_size+1):
      cave[(x,y)] %= 3

  return cave


def caveRisk(cave, target):
  x_target, y_target = target
  totalRisk = 0
  for y in range(y_target+1):
    for x in range(x_target+1):
      totalRisk += cave[(x, y)]

  return totalRisk

def mapNetwork(cave, size, tools):
  x_size, y_size = size

  graph = networkx.Graph()
  for y in range(y_size+1):
    for x in range(x_size+1):
      items = tools[cave[(x, y)]]
      # Add changing item time
      graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
      # Find adjacent coords 
      next_coords = []
      for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= x+dx <= size[0] and 0 <= y+dy <= size[1]:
          next_coords.append((x +dx, y+dy))
      # Link if items match
      for next_x, next_y in next_coords:
        new_items = tools[cave[(next_x, next_y)]]
        for item in filter(lambda x: x in items, new_items):
            graph.add_edge((x, y, item), (next_x, next_y, item), weight=1)
  return graph


depth = 9171
target = (7,721)
size = (7+50, 721)

tools = {
  0: ('climbing gear', 'torch'),  #rocky
  1: ('climbing gear', 'neither'),  #wet
  2: ('torch', 'neither')  #narrow
}

cave = mapCave(depth, size)

# Part 1
print(caveRisk(cave, target)) 

# Part 2
graph = mapNetwork(cave, size, tools)
print(networkx.dijkstra_path_length(graph, (0, 0, 'torch'), (target[0], target[1], 'torch')))



