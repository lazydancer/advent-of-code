from itertools import product

from operator import add, mul
def cat(a, b): return int(f"{a}{b}")


def part1():
    with open('input', 'r') as f:
        content = [line.strip() for line in f]
        equations = []
        for c in content:
            test_value, rest = c.split(":")
            test_value = int(test_value)
            input_values = [int(v) for v in rest.split()]
            equations.append((test_value, input_values))

    total_calibration_result = 0
    for eq in equations:

        test_value = eq[0]
        input_values = eq[1]

        items = [add, mul]
        for ops in product(items, repeat=len(input_values)-1):

            test_sum = input_values[0] 
            for i, op in enumerate(ops):
                test_sum = op(test_sum, input_values[i+1])

                if test_sum > test_value:
                    break

            
            if test_sum == test_value:
                total_calibration_result += test_value
                break


    print(total_calibration_result)


import time

def part2():
    start_time = time.perf_counter()

    with open('input', 'r') as f:
        content = [line.strip() for line in f]
        equations = []
        for c in content:
            test_value, rest = c.split(":")
            test_value = int(test_value)
            input_values = [int(v) for v in rest.split()]
            equations.append((test_value, input_values))

    total_calibration_result = 0
    for eq in equations:

        test_value = eq[0]
        input_values = eq[1]

        items = [add, mul, cat]
        for ops in product(items, repeat=len(input_values)-1):

            test_sum = input_values[0] 
            for i, op in enumerate(ops):
                test_sum = op(test_sum, input_values[i+1])

                if test_sum > test_value:
                    break

            
            if test_sum == test_value:
                total_calibration_result += test_value
                break


    print(total_calibration_result)


    end_time = time.perf_counter()
    print(f"time = {end_time-start_time:.6f} s")





part2()