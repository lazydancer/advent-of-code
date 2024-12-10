def process(part):
    with open('input', 'r') as f:
        map_data = [[int(n) for n in line.strip()] for line in f]

    def neighbours(loc):
        y, x = loc

        result = []
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            if 0 <= (ny := y + dy) < len(map_data) and 0 <= (nx := x + dx) < len(map_data[0]) and map_data[y][x] + 1 == map_data[ny][nx]:
                result.append((ny, nx))

        return result

    trailheads = [(y, x) for y, row in enumerate(map_data) for x, val in enumerate(row) if val == 0]

    trails = []
    for trailhead in trailheads:
        queue = [trailhead]

        while queue:
            node = queue.pop()

            if map_data[node[0]][node[1]] == 9:
                trails.append((trailhead, node))
                continue

            queue += neighbours(node)    


    if part == 1:
        print(len(set(trails)))
    else:
        print(len(trails))

process(1)
process(2)
