import re

def printMap(clay, flowing, still):
    x1, x2 = 450, 680
    y1, y2 = 0, 1000

    def char(p):
        if p == SPRING:
            return '+'
        elif p in clay:
            return '#'
        elif p in still:
            return '~'
        elif p in flowing:
            return '|'
        else:
            return '.'

    print('\n'.join(''.join(char((x, y)) for x in range(x1, 1 + x2)) for y in range(y1, 1 + y2)))
 

def add(tuple, x, y):
  return (tuple[0] + x, tuple[1] + y)


def spread(pos, clay, flowing, still):
    # Sstill broken
    temp = set()
    print(temp)
    pl = spread_r(pos, LEFT, clay, still, temp)
    pr = spread_r(pos, RIGHT, clay, still, temp)
    if not pl and not pr:
        still.update(temp)

    else:
        flowing.update(temp)
    return pl, pr


def spread_r(pos, off, clay, still, temp):
  # Sstill broken
    pos1 = pos
    while pos1 not in clay:
        temp.add(pos1)
        pos2 = pos1 + DOWN
        if pos2 not in clay and pos2 not in still:
            return pos1
        pos1 = pos1 + off
    return None

def main():

  ### Clay Inputs
  clay = set()

  lines = open('input').read().strip().split('\n')
  for line in lines:
    
    nums = list(map(int, re.findall('-?\d+', line)))

    if line[0] == 'x':
      for y in range(nums[1], 1 + nums[2]):
        clay.add((nums[0], y))
    elif line[0] == 'y':
      for x in range(nums[1], 1 + nums[2]):
        clay.add((x, nums[0]))
  

  ### Water flowing logic
  flowing, still, toFall, toSpread = set(), set(), set(), set()

  toFall.add(SPRING)

  while toFall:
    blockToFall = toFall.pop()
    posd = add(blockToFall, 0, 1)
    if posd not in clay:
      flowing.add(posd)
      toFall.add(posd) 
    else:
      toSpread.add(posd)

  while toSpread:
    blockToSpread = toSpread.pop()
    rl, rr = spread(blockToSpread, clay, flowing, still)

    if not rr and not rl:
        to_spread.add(ts + UP)
    else:
        if rl:
            to_fall.add(rl)
        if rr:
            to_fall.add(rr)

    print(blockToFall)
    


  printMap(clay, flowing, {})

SPRING = (500, 0)

main()