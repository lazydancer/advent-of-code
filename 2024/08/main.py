from collections import defaultdict

def part1():
    with open('input', 'r') as f:
        city_scan = [list(line.strip()) for line in f]

    rows, cols = len(city_scan), len(city_scan[0])
    antennas = defaultdict(list)

    for y, row in enumerate(city_scan):
        for x, char in enumerate(row):
            if char != '.':
                antennas[char].append((x,y))

    antinodes = set()
    for char in antennas:
        nodes = antennas[char]

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i == j: 
                    continue

                x = nodes[j][0] + nodes[j][0] - nodes[i][0]
                y = nodes[j][1] + nodes[j][1] - nodes[i][1]

                if 0 <= x < cols and 0 <= y < rows:
                    antinodes.add((x,y))

    print(len(antinodes))



def part2():
    with open('input', 'r') as f:
        city_scan = [list(line.strip()) for line in f]

    rows, cols = len(city_scan), len(city_scan[0])
    antennas = defaultdict(list)

    for y, row in enumerate(city_scan):
        for x, char in enumerate(row):
            if char != '.':
                antennas[char].append((x,y))

    antinodes = set()
    for char in antennas:
        nodes = antennas[char]

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i == j: 
                    continue

                x = nodes[j][0]
                y = nodes[j][1]

                while (0 <= x < cols) and (0 <= y < rows):
                    antinodes.add((x,y))

                    x += nodes[j][0] - nodes[i][0]
                    y += nodes[j][1] - nodes[i][1]


    print(len(antinodes))


part1()
part2()




