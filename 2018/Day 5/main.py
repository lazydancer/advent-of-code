def runCycle(inputStr):
  inputLen = len(inputStr)

  pos = 0
  while pos < inputLen-1:
    if inputStr[pos] == inputStr[pos+1].swapcase():
     
      inputStr = inputStr[:pos] + inputStr[(pos+2):]
      inputLen -= 2
      pos -= 2
    pos += 1

  return inputStr

inputFile = open('input', 'r')
inputStr = inputFile.readlines()[0]

inputStr = runCycle(inputStr)
print("Part 1:", len(inputStr.strip()))

minimum = 11476
for char in set(inputStr.lower()):
  modString = inputStr
  modString = modString.replace(char, "")
  modString = modString.replace(char.swapcase(), "")

  modString = runCycle(modString)

  if len(modString.strip()) < minimum:
    minimum = len(modString.strip())

print("Part 2:", minimum)