def extract(text, part):
    blocks = text.strip().split('\n\n')

    results = []

    for block in blocks:
        lines = {line.split(':')[0]: line.split(':')[1].strip() for line in block.splitlines()}

        a_coords = tuple(map(int, lines["Button A"].replace("X+", "").replace("Y+", "").split(', ')))
        b_coords = tuple(map(int, lines["Button B"].replace("X+", "").replace("Y+", "").split(', ')))
        prize_coords = tuple(map(int, lines["Prize"].replace("X=", "").replace("Y=", "").split(', ')))

        if part == 1:
            results.append({
                "A": a_coords,
                "B": b_coords,
                "Prize": prize_coords
            })

        if part == 2:
            results.append({
                "A": a_coords,
                "B": b_coords,
                "Prize": (prize_coords[0] + 10000000000000, prize_coords[1] + 10000000000000)
            })


    return results

import numpy as np
from scipy.optimize import linprog


def solve_machine(machine):
    A = machine["A"]
    B = machine["B"]
    Prize = machine["Prize"]

    c = np.array([3, 1]) 

    A_eq = np.array([
        [A[0], B[0]],
        [A[1], B[1]] 
    ])
    b_eq = np.array([Prize[0], Prize[1]])

    bounds = [(0, None), (0, None)]

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if result.success:
        a_presses, b_presses = map(round, result.x)
        x = a_presses * A[0] + b_presses * B[0]
        y = a_presses * A[1] + b_presses * B[1]

        if x == Prize[0] and y == Prize[1]:
            cost = 3 * a_presses + 1 * b_presses
            return (a_presses, b_presses, cost)
        else:
            return (0,0,0)
    else:
        return (0,0,0)



def process(part):
    with open('input', 'r') as f:
        machines = extract(f.read(), part)

    tokens = 0
    for machine in machines:
        a, b, c = solve_with_numpy(machine)

        if part == 1 and  a < 100 and b < 100:
            tokens += c
        if part == 2:
            tokens += c


    print(tokens)


process(2)
