from functools import cache
from collections import deque

KEYS = {
    "numerical": [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ],
    "directional": [
        [None, "^", "A"],
        [ "<", "^", ">"]
    ]
}

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


# incomplete

def next(vacy, vacx, rady, radx, tempy, tempx, action):
    if action == "A":

        temp = get_key(KEYS["directional"], (tempy, tempx))
        if temp is None:
           return None, None, None, None, None, None, None
        
        if temp  == "A":
            rad = get_key(KEYS["directional"], (rady, radx))
            if rad is None:
                return None, None, None, None, None, None, None

            if rad == "A":
                return vacy, vacx, rady, radx, tempy, tempx, get_key(KEYS["numerical"], (vacy, vacx))
            
            if rad in DIRECTIONS.keys():
                return vacy + DIRECTIONS[rad][0], vacx + DIRECTIONS[rad][1], rady, radx, tempy, tempx, None
        
        if temp in DIRECTIONS.keys():
            return vacy, vacx, rady + DIRECTIONS[temp][0], radx + DIRECTIONS[temp][1], tempy, tempx, None

    if action in DIRECTIONS.keys():
        return vacy, vacx, rady, radx, tempy + DIRECTIONS[action][0], tempx + DIRECTIONS[action][1], None






def find_coordinates(matrix, char):
    for y, row in enumerate(matrix):
        for x, element in enumerate(row):
            if element == char:
                return y, x



def get_key(matrix, loc):
    y, x = loc

    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
        return matrix[y][x]



def bps(from_key, to_key):
    vacy, vacx = find_coordinates(KEYS['numerical'], from_key)
    rady, radx = find_coordinates(KEYS['directional'], "A")
    tempy, tempx = find_coordinates(KEYS['directional'], "A")

    actions = ['^', '>', 'v', '<', 'A']

    queue = deque([(vacy, vacx, rady, radx, tempy, tempx, action, 0) for action in actions])

    visited = set()

    while queue:

        vacy, vacx, rady, radx, tempy, tempx, action, presses = queue.popleft()


        state = (vacy, vacx, rady, radx, tempy, tempx, action)
        if state in visited:
            continue
        visited.add(state)

        if len(queue) % 1000 == 0:
            print(presses)

        vacy, vacx, rady, radx, tempy, tempx, pressed = next(vacy, vacx, rady, radx, tempy, tempx, action)
        
        if vacy is None: # invalid state
            continue

        if pressed == to_key:
            return pressed

        if pressed is None:
            queue += [(vacy, vacx, rady, radx, tempy, tempx, action, presses + 1) for action in actions]





def part1():
    with open('input_test', 'r') as f:
        codes = [line.rstrip('\n') for line in f]

    print(bps("A", "0"))




part1()