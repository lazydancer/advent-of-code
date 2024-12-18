from collections import deque

COLS = 71
ROWS = 71


def bfs(corrupted):
    queue = deque([(0,0,0)])
    visited = set()
    visited.add((0,0))

    while queue:
        x, y, c = queue.popleft()

        if (x, y) == (COLS-1, ROWS-1):
            return c

        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in corrupted and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, c + 1))

    return -1

def process(part):
    BYTES = 1024

    with open('input', 'r') as f:
        bytes_text = [n.strip().split(',') for n in f.readlines()]
        byte_coords = [(int(x), int(y)) for x, y in bytes_text]

    if part == 1:
        corrupted = set(byte_coords[:BYTES])
        print(bfs(corrupted))

    if part == 2:
        for i in range(1024, len(byte_coords)):
            corrupted = set(byte_coords[:i])
            steps = bfs(corrupted)

            if steps == -1:
                print(i, byte_coords[i-1])
                return


process(1)
process(2)