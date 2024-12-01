import re

def manhatten(p1, p2):
  return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1]) + abs(p2[2]-p1[2])  + abs(p2[3]-p1[3]) 

def search_constellations(coord, constellations):
  result = set()
  for i, constellation in enumerate(constellations):
    for point in constellation:
      if manhatten(coord, point) <= 3:
        result.add(i)
  return list(result)

def main(coords):
  constellations = [];
  for coord in coords:
    in_cons = search_constellations(coord, constellations)
    if len(in_cons) is 0:
      constellations.append([coord])
    if len(in_cons) is 1:
      constellations[in_cons[0]].append(coord)
    if len(in_cons) >= 2:
      new_cons = [coord]
      for con in in_cons:
        new_cons += constellations[con]

      constellations[in_cons[0]] = new_cons

      for con in sorted(in_cons[1:], reverse=True):
        del constellations[con]
    
  print(len(constellations))

  return

lines = open('input').read().strip().split('\n')
coords = []
for line in lines:
  coords.append(list(map(int, re.findall(r'-?\d+', line))))

main(coords)