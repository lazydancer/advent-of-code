import heapq

def part1():
    with open('input', 'r') as f:
        maze = [list(n) for n in f.read().split()]

    reindeer = next((r, c) for r, line in enumerate(maze) for c, char in enumerate(line) if char == "S")
    direction = (0,1)
    end = next((r, c) for r, line in enumerate(maze) for c, char in enumerate(line) if char == "E")


    heap = []
    visited = {}
    heapq.heappush(heap, (0, reindeer, None, direction))
    while heap:

        score, loc, prev, dir = heapq.heappop(heap)

        if loc == end:
            return score

        y,x = loc

        if (y, x, dir) in visited and visited[(y, x, dir)] <= score:
            continue
        visited[(y, x, dir)] = score

        for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            if (0 <= (ny := y + dy) < len(maze) and 
                0 <= (nx := x + dx) < len(maze[0]) and 
                maze[ny][nx] != "#"
               ):

                if (ny, nx) == prev:
                    continue

                points = 1
                if (dy, dx) != dir:
                    points += 1000

                heapq.heappush(heap, (score + points, (ny, nx), (y, x), (dy, dx) ))





def part2(min_score):
    with open('input_test', 'r') as f:
        maze = [list(n) for n in f.read().split()]

    reindeer = next((r, c) for r, line in enumerate(maze) for c, char in enumerate(line) if char == "S")
    end = next((r, c) for r, line in enumerate(maze) for c, char in enumerate(line) if char == "E")

    heap = []
    best_paths = []


    heapq.heappush(heap, (0, reindeer, None, (0, 1), [reindeer]))


    while heap:
        score, loc, prev, dir, path = heapq.heappop(heap)
        y,x = loc

        if score > min_score:
            continue

        if loc == end:
            if score == min_score:
                best_paths.append(path)
            continue


        for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            if (0 <= (ny := y + dy) < len(maze) and 
                0 <= (nx := x + dx) < len(maze[0]) and 
                maze[ny][nx] != "#"):

                if (ny, nx) == prev:
                    continue

                points = 1
                if (dy, dx) != dir:
                    points += 1000

                heapq.heappush(heap, (score + points, (ny, nx), (y, x), (dy, dx), path + [(ny, nx)]))




minimum_score = part1()
print(minimum_score)
part2(minimum_score)