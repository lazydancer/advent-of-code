def nextAssignment(graph):
  emptyDep = []
  for key in graph:
    if(len(graph[key]) == 0):
      emptyDep.append(key) 

  emptyDep.sort()

  return emptyDep

def removeFromGraph(graph,node):
    graph.pop(node)

    for key in graph:
      if node in graph[key]:
        graph[key].remove(node)

    return graph


def part1(graph):
  solution = []

  for i in range(26):
    emptyDep = nextAssignment(graph)
    doNode = emptyDep[0]
    solution.append(doNode)
    
    graph = removeFromGraph(graph, doNode)

  print('Part1:',''.join(solution))


def part2(graph):

  time = 0
  workers = []

  emptyDep = []
  for key in graph:
    if(len(graph[key]) == 0):
      emptyDep.append(key) 

  emptyDep.sort()

  while graph != {}:

    toRemoveDep = set()
    for dep in emptyDep:
      if len(workers) < 5:
        workers.append([dep,ord(dep.lower())-36])
        toRemoveDep.add(dep)

    emptyDep = [v for v in emptyDep if v not in toRemoveDep]

    toRemoveWorker = set()
    for i, worker in enumerate(workers):
      worker[1] -= 1
      if worker[1] is 0:
        graph = removeFromGraph(graph, worker[0])
        emptyDep = nextAssignment(graph)
        workingOn = [x[0] for x in workers]
        emptyDep = [x for x in emptyDep if x not in workingOn]
        toRemoveWorker.add(i)
        
    workers = [v for i, v in enumerate(workers) if i not in toRemoveWorker]
    
    time += 1 
 
  print('Part2:',time)

def main():
  inputFile = open('input', 'r')
  lines = inputFile.readlines()

  graph = {}

  for line in lines:

    fromNode = line[5]
    toNode = line[36]
    
    if fromNode not in graph:
      graph[fromNode] = set()

    if toNode not in graph:
      graph[toNode] = set()

    graph[toNode].add(fromNode)  

  part1(graph) #FMOXCDGJRAUIHKNYZTESWLPBQV
  part2(graph) #1053
 
main()