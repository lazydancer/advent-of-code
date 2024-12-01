def runGeneration(state, spread):
  updatedState = list(state)
  for note in spread:
    i = 0
    while i+5 < len(state):
      if note[0] == state[i:i+5]:
        updatedState[i+2] = note[1]
      i += 1  

  return "".join(updatedState)

def main():
  inputFile = open('input', 'r')
  lines = inputFile.readlines()

  initalState = lines[0][15:]
  initalState = initalState.rstrip()

  spread = lines[2:]
  spread = [x.rstrip() for x in spread]
  spread = [x.split(' => ') for x in spread]


  end = '.' * 1000
  state = '..........' + initalState + end
  for gen in range(200):
    state = runGeneration(state, spread)

  result = 0
  constVel200 = []
  for i in range(len(state)):
    if state[i] == '#':
      constVel200.append(i-10)
      result += (i -10)
  
  print(result)

  part2 = 0
  for index in constVel200:
    part2 += (index + 50000000000 - 200)

  print('part2:', part2)

main()