import os
import time
from collections import Counter

def extract(text):
    result = []
    for line in text.strip().split('\n'):
        parts = line.split()
        p_x, p_y = map(int, parts[0].split('=')[1].split(','))
        v_x, v_y = map(int, parts[1].split('=')[1].split(','))
        result.append([(p_x, p_y), (v_x, v_y)])

    return result


def segment(robots, width, height):
    half_w, half_h = width // 2, height // 2
    a = b = c = d = 0
    for r in robots:
        x, y = r[0]
        if   x < half_w and y < half_h:
            a += 1
        elif x > half_w and y < half_h:
            b += 1
        elif x < half_w and y > half_h:
            c += 1
        elif x > half_w and y > half_h:
            d += 1

    return a*b*c*d


def part1():
    with open('input', 'r') as f:
        robots = extract(f.read())

    width, height = 101, 103

    for _ in range(100):
        robots = [(((x + dx) % width, (y + dy) % height), (dx, dy)) for (x, y), (dx, dy) in robots]

    print(segment(robots, width, height))


def part2():
    with open('input', 'r') as f:
        robots = extract(f.read())

    width, height = 101, 103

    for i in range(10000):
        robots = [(((x + dx) % width, (y + dy) % height), (dx, dy)) for (x, y), (dx, dy) in robots]

        seg = segment(robots, width, height)
        
        if seg < 100000000:
            os.system('clear')
            print(i + 1, seg)
            positions = Counter(pos for pos, _ in robots)

            for y in range(height):
                print("".join(str(positions.get((x, y), '.')) for x in range(width)))
            time.sleep(2)    

part1()
part2()
