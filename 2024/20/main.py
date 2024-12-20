from collections import deque


def bfs(maze, start, end):    
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, 0)])  
    visited = set([start])

    while queue:
        (y, x), dist = queue.popleft()

        if (y, x) == end:
            return dist

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols:
                if maze[ny][nx] != '#' and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append(((ny, nx), dist + 1))

    # No path found
    return None


def potential_cheats(maze):
    result = set()

    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            if char == '#' and 1 <= r < len(maze)-1 and 1 <= c < len(maze[0])-1:

                if maze[r-1][c] == '.' and maze[r+1][c] == '.':
                    result.add(((r-1, c),(r+1, c)))
                    result.add(((r+1, c),(r-1, c)))

                if maze[r][c-1] == '.' and maze[r][c+1] == '.':
                    result.add(((r, c-1),(r, c+1)))
                    result.add(((r, c+1),(r, c-1)))

    return result

def part1():
    with open('input', 'r') as f:
        maze = [list(line) for line in f.read().splitlines()]

    start = None
    end = None
    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
                maze[r][c] = '.'
            elif char == 'E':
                end = (r, c)
                maze[r][c] = '.'


    shortest_distance = bfs(maze, start, end)


    result = []

    print(len(potential_cheats(maze)))

    for i, (cheat_from, cheat_to) in enumerate(potential_cheats(maze)):

        if i % 100 == 0:
            print(i)

        before_dist = bfs(maze, start, cheat_from)
        after_dist = bfs(maze, cheat_to, end)


        cheated = before_dist + after_dist - 2

        if cheated > shortest_distance:
            result.append(cheated - shortest_distance)


    sum = 0
    for r in result:
        if r >= 100:
            sum += 1

    print(sum)


def bfs_path(maze, start, end):    
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, 0)])
    visited = set([start])
    parent = {start: None}

    while queue:
        (y, x), dist = queue.popleft()

        if (y, x) == end:
            path = []
            cur = (y, x)
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return dist, path

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols:
                if maze[ny][nx] != '#' and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
                    queue.append(((ny, nx), dist + 1))

    return None, None


from itertools import combinations

def part2():
    with open('input', 'r') as f:
        maze = [line.rstrip('\n') for line in f]

    grid = {}
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch != '#':
                grid[(r, c)] = ch


    start = None
    end = None
    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
            elif char == 'E':
                end = (r, c)


    dist = {start: 0}
    queue = deque([start])

    while queue:
        pos = queue.popleft()
        r, c = pos
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in grid and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[pos] + 1
                queue.append((nr, nc))

    result = 0
    for (p, i), (q, j) in combinations(dist.items(), 2):
        pr, pc = p
        qr, qc = q
        d = abs(pr - qr) + abs(pc - qc)

        if d < 21 and j - i - d >= 100:
            result += 1

    print(result)



part2()

