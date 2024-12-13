
def process(part):
    with open('input', 'r') as f:
        garden_plot = [list(n) for n in f.read().split()]

    DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

    def group_region(start):
        region = [start]
        val = garden_plot[start[0]][start[1]]

        queue = [start]
        while queue != []:
            y, x = queue.pop()

            for dy,dx in DIRS:
                if (
                    0 <= ( ny := y + dy ) < len(garden_plot) and 
                    0 <= ( nx := x + dx ) < len(garden_plot[0]) and 
                    (ny, nx) not in region and
                    val == garden_plot[ny][nx]
                ):
                    region.append((ny, nx))
                    queue.append((ny, nx))

        return region

    regions = []
    seen = []
    for y in range(len(garden_plot)):
        for x in range(len(garden_plot[0])):
            if (y, x) not in seen:
                new_region = group_region((y,x))
                regions.append(new_region)
                seen += new_region

    def perimeter(region):
        edges = set()
        for y, x in region:
            for dy, dx in DIRS:
                ny, nx = y + dy, x + dx
                if (ny, nx) not in region:
                    edges.add(((y, x), (ny, nx)))
        return edges

    def sides(edges):
        filtered = set()
        for (p1, p2) in edges:
            keep = True
            for (dy, dx) in [(1,0), (0,1)]:
                p1n = (p1[0] + dy, p1[1] + dx)
                p2n = (p2[0] + dy, p2[1] + dx)
                if (p1n, p2n) in edges:
                    keep = False
                    break
            if keep:
                filtered.add((p1, p2))
        return filtered


    result = 0
    if part == 1:
        for region in regions:
            result += len(region) * len(perimeter(region))

    if part == 2:
        for region in regions:
            result += len(region) * len(sides(perimeter(region)))

    print(result)


process(2)

