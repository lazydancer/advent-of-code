def readNode(input):
  result = 0

  childrenCount = input.pop()
  metadataCount = input.pop()

  for _ in range(childrenCount): 
    result += readNode(input)

  for _ in range(metadataCount):
    result += input.pop()

  return result

def rootNode(input):
  
  childrenCount = input.pop()
  metadataCount = input.pop()

  result = 0
  meta = 0
  children = []

  if childrenCount is 0:
    for _ in range(metadataCount):
      result += input.pop()
  
  else:  
    for _ in range(childrenCount):
      children.append(rootNode(input))

    for _ in range(metadataCount):
      meta = input.pop()
      if meta <= len(children) and meta > 0:
        result += children[meta-1]
  
  return result

def main(line):

  input = [int(x) for x in line.split(" ")]
  input = input[::-1] #reverse
  inputCopy = input.copy()

  print('Part 1 :', readNode(input)) #36566
  print('Part 2 :', rootNode(inputCopy)) #30548

inputFile = open('input', 'r')
main(inputFile.readlines()[0])
