def part1(lines):
  twiceCount, triceCount = 0, 0

  for line in lines:
    twiceFlag, triceFlag = False, False

    for char in line:
      count = line.count(char)
      if count is 2:
        twiceFlag = True
      if count is 3:
        triceFlag = True

    if twiceFlag:
      twiceCount += 1
    if triceFlag:
      triceCount += 1

  print("Result of part 1: ", twiceCount * triceCount) #6723
  
def part2(lines):
  for line in lines:
    for secondLine in lines:
      count = 0
      for i in range(len(line)):
        if line[i] != secondLine[i]:
          count += 1

      if count is 1:
        print("string couple for part 2: ", line, secondLine) 
        #prtkqyluiusocwvaezjmhmfbgx prtkqyluiusocwvaezjmhmfngx
        return



def main():
  inputFile = open('input', 'r')
  lines = inputFile.readlines()
  part1(lines)
  part2(lines)


main()