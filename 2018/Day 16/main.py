def applyOpCode(instruction, register, opCode):
  _, A, B, C = instruction
  result = register[:]

  if opCode is 'addr':
    result[C] = result[A] + result[B]
    return result
  if opCode is 'addi':
    result[C] = result[A] + B
    return result
  
  if opCode is 'mulr':
    result[C] = result[A] * result[B]
    return result
  if opCode is 'muli':
    result[C] = result[A] * B
    return result

  if opCode is 'banr':
    result[C] = result[A] & result[B]
    return result
  if opCode is 'bani':
    result[C] = result[A] & B
    return result

  if opCode is 'borr':
    result[C] = result[A] | result[B]
    return result
  if opCode is 'bori':
    result[C] = result[A] | B
    return result

  if opCode is 'setr':
    result[C] = result[A]
    return result
  if opCode is 'seti':
    result[C] = A
    return result

  if opCode is 'gtir':
    result[C] = 1 if A > result[B] else 0
    return result
  if opCode is 'gtri':
    result[C] = 1 if result[A] > B else 0
    return result
  if opCode is 'gtrr':
    result[C] = 1 if result[A] > result[B] else 0
    return result
  
  if opCode is 'eqir': 
    result[C] = 1 if A == result[B] else 0
    return result
  if opCode is 'eqri':
    result[C] = 1 if result[A] == B else 0
    return result
  if opCode is 'eqrr':
    result[C] = 1 if result[A] == result[B] else 0
    return result


def testSample(sample):

  instruction, before, after = sample

  opCodes = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

 
  matches = 0
  for opCode in opCodes:
    if after == applyOpCode(instruction, before, opCode):
      matches += 1
      if matches >= 3:
        return True

def part1(inputSamples):

  samples = []

  while inputSamples:


    before = inputSamples.pop(0)[9:19].split(',')
    before = [int(x) for x in before]

    instruction = inputSamples.pop(0).split(' ')
    instruction = [int(x) for x in instruction]

    after = inputSamples.pop(0)[9:19].split(',')
    after = [int(x) for x in after]

    inputSamples.pop(0) # pop blank
    
    samples.append([instruction, before, after])
  

  result = 0
  for sample in samples:
    if testSample(sample):
      result += 1


  print("Part 1: ",result)

def part2(inputSamples):

  instructions = []

  while inputSamples:
    instruction = inputSamples.pop(0).split(' ')
    instruction = [int(x) for x in instruction]
    instructions.append(instruction)

  opCodesDic = {
    15: 'banr',
    3: 'bani',
    10: 'setr',
    9: 'gtir',
    14: 'gtrr',
    0: 'eqri',
    5: 'eqrr',
    11: 'eqir',
    7: 'gtri',
    4: 'seti',
    12: 'mulr',
    13: 'muli',
    6: 'addr',
    2: 'addi',
    1: 'bori',
    8: 'borr'
  }
  
  result = [0,0,0,0]
  for instruction in instructions:
    result = applyOpCode(instruction, result, opCodesDic[instruction[0]])
  
  print('Part 2:',result[0])

inputSamples = open('input', 'r')
inputSamples = inputSamples.readlines()

part1(inputSamples)


collectedSamples = open('inputPart2', 'r')
collectedSamples = collectedSamples.readlines()
part2(collectedSamples)


