def coordPower(gridSerialNumber, xCoord, yCoord):
  rackID = xCoord + 10
  powerLevel = rackID * yCoord
  powerLevel += gridSerialNumber
  powerLevel *= rackID
  powerLevel = str(powerLevel)[-3] if len(str(powerLevel)) >= 3 else '0'
  powerLevel = int(powerLevel)
  powerLevel -= 5 

  return powerLevel

def threeByThree(grid,i,j,size):
  cell = 0
  for xOff in range(size):
    for yOff in range(size):
      cell += grid[i+xOff][j+yOff]

  return cell

def main(gridSerialNumber):

  grid = [[coordPower(gridSerialNumber, i, j) for j in range(1,301)] for i in range(1,301)] 


  # Part 1
  
  power = [(i,j,threeByThree(grid, i, j, 3)) for j in range(300-3) for i in range(300-3)]
  maxPower = max(power, key=lambda x:x[2])
  print(maxPower[2], maxPower[0]+1, maxPower[1]+1)
  

  # Part 2
  largest = 0

  for s in range(300):
    for i in range(300-s):
      for j in range(300-s):
        if threeByThree(grid, i, j, s) > largest:
          largest = threeByThree(grid, i, j, s)
          print(i, j, s, largest)

main(9110) 