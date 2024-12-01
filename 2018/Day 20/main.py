import networkx

# ^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$

maze = networkx.Graph()

#paths = open('input').read()[1:-1]
paths = 'N(E|W)N'

pos = {0} #the current positions that we're building on
stack = [] # a stack to keep track of (start, ends) for groups
starts, ends = {0}, set() # current possible starting and ending positions

for c in paths:
  if c == '|':
    ends.update(pos)
    pos = starts
  elif c in 'NESW':
    direction = {'N': 1j, 'E': 1, 'S':-1j, 'W': -1}[c]
    maze.add_edges_from((p, p + direction) for p in pos)
    pos = {p + direction for p in pos}
  elif c == '(':
    stack.append((starts, ends))
    starts, ends = pos, set()
  elif c == ')':
    pos.update(ends)
    starts, ends = stack.pop()

  print(c, pos, starts, ends, 'stack:', stack)

lengths = networkx.algorithms.shortest_path_length(maze, 0)
print('part1:', max(lengths.values()))
print('part2:', sum(1 for length in lengths.values() if length >= 1000))
