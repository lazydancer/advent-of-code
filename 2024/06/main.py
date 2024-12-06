def part1():
    with open('input', 'r') as f:
        lab = [list(line.strip()) for line in f]

    turn_right = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}

    pos = None
    for y, row in enumerate(lab):
        for x, cell in enumerate(row):
            if cell == '^':
                pos = (x, y)

    dir = (0, -1)
    seen = set()

    while True:
        seen.add(pos)
        x, y = pos[0] + dir[0], pos[1] + dir[1]
        if y < 0 or y >= len(lab) or x < 0 or x >= len(lab[0]):
            break

        if lab[y][x] == '#':
            dir = turn_right[dir]
        else:
            pos = (x, y)


    print(len(seen))

import time

DIRECTION_DELTAS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def part2():
    start_time = time.perf_counter()

    with open('input', 'r') as f:
        lab = [list(line.strip()) for line in f]

    rows, cols = len(lab), len(lab[0])

    for y in range(rows):
        for x in range(cols):
            if lab[y][x] == '^':
                start_x, start_y = (x, y)
                break

    def run():
        direction = 0
        x, y = start_x, start_y

        for _ in range(10_000):
            dx, dy = DIRECTION_DELTAS[direction]
            nx, ny = x + dx, y + dy

            if not (0 <= ny < rows and 0 <= nx < cols):
                return True 

            if lab[ny][nx] == '#':
                direction = (direction + 1) % 4 
            else:
                x, y = nx, ny  # Move forward

        return False

    count = 0
    for x in range(len(lab[0])):
        for y in range(len(lab)):
            if lab[y][x] == '.':
                lab[y][x] = '#'

                if not run():
                    count += 1

                lab[y][x] = '.'

    print(count)

    end_time = time.perf_counter()
    print(f"time = {end_time-start_time:.6f} s")











part2()