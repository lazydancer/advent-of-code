def extract(text):
    schematics = [t.split('\n') for t in text.split('\n\n')]

    locks, keys = [], []

    for schematic in schematics:
        columns_counts = [-1,-1,-1,-1,-1]
        for row in schematic:
            for col_index, char in enumerate(row):
                if char == "#":
                    columns_counts[col_index] += 1

        if schematic[0][0] == "#":
            locks.append(columns_counts)
        else:
            keys.append(columns_counts)


    return locks, keys

def part1():
    with open('input', 'r') as f:
        locks, keys = extract(f.read().strip())


    breakpoint()

    fit = 0
    for lock in locks:
        for key in keys:
            is_fit = True
            for i in range(5):
                if (lock[i] + key[i]) > 5:
                    is_fit = False


            if is_fit:
                fit += 1


    print(fit)

part1()