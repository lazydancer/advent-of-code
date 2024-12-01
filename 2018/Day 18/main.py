import copy

def adjacent(state, coord):
  x_coord, y_coord = coord
  result = {'.': 0, '|': 0, '#': 0}
  directions = [(x_coord-1, y_coord+1), (x_coord, y_coord+1), (x_coord+1, y_coord+1),
                (x_coord-1, y_coord), (x_coord+1, y_coord),
                (x_coord-1, y_coord-1), (x_coord, y_coord-1), (x_coord+1, y_coord-1)]
  
  for x,y in directions:
    if 0 <= x < len(state[0]) and 0 <= y < len(state):
      result[state[y][x]] += 1 
  return result

def countSolution(state):
  woodedAreas = 0
  lumberyards = 0
  for line in state:
    for char in line:
      if char == '|':
        woodedAreas += 1
      elif char == '#':
        lumberyards += 1

  return woodedAreas * lumberyards

def nextState(state):

  newState = copy.deepcopy(state)

  for y in range(len(state)):
    for x in range(len(state[0])):
      adjacents = adjacent(state, (x, y))

      if state[y][x] == '.':
        if adjacents['|'] >= 3:
          newState[y][x] = '|'
      
      if state[y][x] == '|':
        if adjacents['#'] >= 3:
          newState[y][x] = '#'

      if state[y][x] == '#':
        if not(adjacents['#'] >= 1 and adjacents['|'] >= 1):
          newState[y][x] = '.'

  return newState

def main():
  
  lines = open('input').read().strip().split('\n')
  lines = [list(line) for line in lines]

  print('\n'.join([''.join(line) for line in lines]))
  
  for i in range(100):
    lines = nextState(lines)
    if i == 9:
      print('part 1:', countSolution(lines))
  
  print('\n'.join([''.join(line) for line in lines]))
  print(countSolution(lines))

main()