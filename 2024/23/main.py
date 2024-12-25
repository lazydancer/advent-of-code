import networkx as nx

def part1():
    with open('input', 'r') as f:
        connections = [tuple(line.strip().split("-")) for line in f]

    graph = nx.Graph()
    graph.add_edges_from(connections)
    triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3] 

    filtered_t = [t for t in triangles if any(node.startswith('t') for node in t)]

    print(len(filtered_t))


def part2():
    with open('input', 'r') as f:
        connections = [tuple(line.strip().split("-")) for line in f]

    graph = nx.Graph()
    graph.add_edges_from(connections)

    for i in range(4,100):
        triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == i]

        if len(triangles) == 0:
            print(','.join(sorted(prev[0])))

        prev = triangles 



part2()