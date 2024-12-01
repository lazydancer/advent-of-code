import re
from datetime import datetime

def readInput():

  inputFile = open('input', 'r')
  lines = inputFile.readlines()
  
  input = [l[1:].split('] ') for l in lines]
  input = [(datetime.strptime(d, '%Y-%m-%d %H:%M'),s) for d,s in input]
  input = sorted(input, key= lambda x:x[0])

  return input

def createRecord(input):
  record = {}  
  while input:

    guard = int(input.pop(0)[1].split(' ')[1][1:])

    while input and input[0][1][0] != 'G':
      t1 = input.pop(0)[0].minute
      t2 = input.pop(0)[0].minute

      record[guard] = record.get(guard, {})
      record[guard].update({ t : record[guard].get(t,0)+1 for t in range(t1, t2)})

  return record

def part1(record):

  id = max(record, key=lambda g: sum(record[g].values()))
  minute = max(record[id], key=lambda t: record[id][t])
  print('Part 1: ' + str(id*minute))

def part2(record):

  id = max(record, key=lambda g: max(record[g].values()))
  minute = max(record[id], key=lambda t: record[id][t])
  print('Part 2: ' + str(id* minute))


input = readInput()
record = createRecord(input)
part1(record)
part2(record)