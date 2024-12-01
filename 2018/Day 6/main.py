GRID_WIDTH = 500
GRID_HEIGHT = 500

def manhattenDistance(coord1, coord2):
  return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) 

def addDistances(coord, grid):

  loc = {}
  for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
      loc = grid[x][y]
      loc[coord['id']] = manhattenDistance((x, y), (coord['x'], coord['y']))

  return grid

def createAreaGrid(grid):
  areaGrid = [[9999 for i in range(GRID_HEIGHT)] for j in range(GRID_WIDTH)]

  for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
      min1 = min(grid[x][y], key=grid[x][y].get)
      min1d = grid[x][y][min1]

      grid[x][y].pop(min1)

      min2 = min(grid[x][y], key=grid[x][y].get)
      min2d = grid[x][y][min2]

      if min1d is not min2d:
        areaGrid[x][y] = min1

  return areaGrid

def part1(grid):
  areaGrid = createAreaGrid(grid)
  
  # Create list of largest zones
  zones = []
  for i in range(50):
    zones.append((i, sum(x.count(i) for x in areaGrid)))
        
  infiniteIds = set()
  # Remove infinite zones
  for x in range(GRID_WIDTH):
    infiniteIds.add(areaGrid[x][0])
    infiniteIds.add(areaGrid[x][GRID_HEIGHT-1])
  for y in range(GRID_HEIGHT):
    infiniteIds.add(areaGrid[0][y])
    infiniteIds.add(areaGrid[GRID_WIDTH-1][y])

  # Return largest result

  zones = [(x1, x2) for x1, x2 in zones if x1 not in infiniteIds]
  result = max(zones, key=lambda x:x[1])
  
  print("Part 1:", result[1]) #4011

def part2(grid):
  flatGrid = [item for sublist in grid for item in sublist]
  safePoint = [sum(d.values()) for d in flatGrid if sum(d.values()) < 10000]
  print('Part2:',len(safePoint)) #46054


def main():
  inputFile = open('input', 'r')
  lines = inputFile.readlines()
  coords = [line.strip().split(', ') for line in lines]
  coords = [{'id': id, 'x': int(x[0]), 'y': int(x[1])} for id, x in enumerate(coords)]

  # Create a grid bigger than coords
  grid = [[{} for i in range(GRID_HEIGHT)] for j in range(GRID_WIDTH)]

  # Find closest co-ord at each location
  for coord in coords:
    grid = addDistances(coord, grid)
  
  part1(grid)
  part2(grid)

   

main()