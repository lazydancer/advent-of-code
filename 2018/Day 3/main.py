import re
from itertools import product

def readClaims(lines):
  claims = []
  for claimStr in lines:
    result = claimStr.rstrip() 
    result = result.replace(" ","") 
    result = re.split('@|,|:|x', claimStr[1:])

    claims.append(list(map(lambda x: int(x), result)))

  return claims

def applyClaims(claims, fabric):
  for id,x,y,sx,sy in claims:
    patches = product(range(x, x+sx), range(y, y+sy))

    for p in patches:
      if p not in fabric:
        fabric[p] = 0
      else:
        fabric[p] += 1

  return fabric

def countOverlap(fabric):
  return sum(1 for k in fabric if fabric[k] > 0)

def idNotOverlaping(claims, fabric):
  for id, x, y, sx, sy in claims:
    patches = product(range(x, x+sx), range(y, y+sy))
  
    if sum(1 for p in patches if fabric[p] > 0) is 0:
      return id

def main():
  inputFile = open('input', 'r')
  lines = inputFile.readlines()
  claims = readClaims(lines)

  fabric = {}
  fabric = applyClaims(claims, fabric)

  print("Part 1 - The count of the overlap is", countOverlap(fabric)) # 120408
  print("Part 2 - The only id not overlaping is", idNotOverlaping(claims, fabric)) 

main()