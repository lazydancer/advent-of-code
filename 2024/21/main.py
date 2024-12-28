from collections import deque
from functools import cache

KEYS = {
    "numerical": [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ],
    "directional": [
        [None, "^", "A"],
        [ "<", "v", ">"]
    ]
}

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def next(vacy, vacx, rady, radx, tempy, tempx, action):
    
    if action == "A":
        temp = get_key(KEYS["directional"], (tempy, tempx))
        if temp is None:
           return (None,) * 7
        
        if temp  == "A":
            rad = get_key(KEYS["directional"], (rady, radx))
            if rad is None:
                return (None,) * 7

            if rad == "A":
                return vacy, vacx, rady, radx, tempy, tempx, get_key(KEYS["numerical"], (vacy, vacx))
            
            if rad in DIRECTIONS.keys():
                dy, dx = DIRECTIONS[rad]

                if get_key(KEYS["numerical"], (vacy + dy, vacx + dx)) is None:
                    return (None,) * 7

                return vacy + dy, vacx + dx, rady, radx, tempy, tempx, None
        
        if temp in DIRECTIONS.keys():
            
            dy, dx = DIRECTIONS[temp]

            if get_key(KEYS["directional"], (rady + dy, radx + dx)) is None:
                return (None,) * 7

            return vacy, vacx, rady + dy, radx + dx, tempy, tempx, None

    if action in DIRECTIONS.keys():

        dy, dx = DIRECTIONS[action]


        if get_key(KEYS["directional"], (tempy + dy, tempx + dx)) is None:
            return (None,) * 7

        return vacy, vacx, rady, radx, tempy + dy, tempx + dx, None






def find_coordinates(matrix, char):
    for y, row in enumerate(matrix):
        for x, element in enumerate(row):
            if element == char:
                return y, x



def get_key(matrix, loc):
    y, x = loc

    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
        return matrix[y][x]

    return None



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

        vacy, vacx, rady, radx, tempy, tempx, pressed = next(vacy, vacx, rady, radx, tempy, tempx, action)
        
        if vacy is None: # invalid state
            continue

        if pressed == to_key:
            return presses

        if pressed is None:
            queue += [(vacy, vacx, rady, radx, tempy, tempx, action, presses + 1) for action in actions]




def part1():
    with open('input', 'r') as f:
        codes = [line.rstrip('\n') for line in f]



    overall_result = 0
    for code in codes:
        result = 0
        result += bps("A"    , code[0])
        print(result)
        result += bps(code[0], code[1])
        print(result)
        result += bps(code[1], code[2])
        print(result)
        result += bps(code[2], code[3])
        print(result)
        print("final:", result + 4)
        print("final:", int(code[:-1]))
        overall_result += ((result + 4) * int(code[:-1]))


    print(overall_result)


part1()