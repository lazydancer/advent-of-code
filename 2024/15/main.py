def extract(text):
    DIR = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }

    warehouse = []
    moves = []

    warehouse_text, moves_text = text.strip().split('\n\n')
    warehouse = [list(l) for l in warehouse_text.split()]

    moves = [DIR[c] for c in list(moves_text.replace('\n',''))]

    return warehouse, moves




def step(warehouse, move):
    rob_y, rob_x = next((r, c) for r, line in enumerate(warehouse) for c, char in enumerate(line) if char == "@")

    dy, dx = move

    next_y = rob_y + dy
    next_x = rob_x + dx
    front_cell = warehouse[next_y][next_x]

    if front_cell == '.':
        warehouse[next_y][next_x] = '@'
        warehouse[rob_y][rob_x] = '.'
        return

    if front_cell == 'O':
        chain_positions = []
        cur_y, cur_x = next_y, next_x
        
        while warehouse[cur_y][cur_x] == 'O':
            chain_positions.append((cur_y, cur_x))
            cur_y += dy
            cur_x += dx

        end_cell = warehouse[cur_y][cur_x]

        if end_cell == '.':
            warehouse[cur_y][cur_x] = 'O'

            for i in reversed(range(len(chain_positions))):
                y_pos, x_pos = chain_positions[i]
                if i == 0:
                    warehouse[y_pos][x_pos] = '@'
                else:
                    prev_y, prev_x = chain_positions[i-1]
                    warehouse[y_pos][x_pos] = 'O'
                    warehouse[prev_y][prev_x] = '.'

            warehouse[rob_y][rob_x] = '.'
        else:
            return




def part1():
    with open('input', 'r') as f:
        warehouse, moves = extract(f.read())

    for move in moves:
        step(warehouse, move)

    [print(''.join(x)) for x in warehouse]
    print()

    result = 0
    for y, row in enumerate(warehouse):
        for x, val in enumerate(row):
            if val == "O":
                result += 100*y + x

    print(result)


def extract_2(text):
    DIR = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }

    WIDE = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    }

    warehouse = []
    moves = []

    warehouse_text, moves_text = text.strip().split('\n\n')

    warehouse = []
    for line in warehouse_text.split():
        wl = []
        for c in list(line):
            wl += WIDE[c]

        warehouse.append(wl)

    moves = [DIR[c] for c in list(moves_text.replace('\n',''))]

    return warehouse, moves




def step_2(warehouse, move):
    rob_y, rob_x = next((r, c) for r, line in enumerate(warehouse) for c, char in enumerate(line) if char == "@")

    dy, dx = move

    next_y = rob_y + dy
    next_x = rob_x + dx

    if warehouse[next_y][next_x] == '.':
        warehouse[next_y][next_x] = '@'
        warehouse[rob_y][rob_x] = '.'
        return

    if warehouse[next_y][next_x] in ['[',']']:
        chain_positions = []

        cur_y, cur_x = next_y, next_x

        # Horizontal push
        if dy == 0:
            while warehouse[cur_y][cur_x] in ['[',']']:
                chain_positions.append((cur_y, cur_x))
                cur_y += dy
                cur_x += dx

            end_cell = warehouse[cur_y][cur_x]

            if end_cell == '.':
                for y_pos, x_pos in reversed(chain_positions):
                    warehouse[y_pos + dy][x_pos + dx] = warehouse[y_pos][x_pos]
                    warehouse[y_pos][x_pos] =  '.'

                warehouse[rob_y + dy][rob_x + dx] = '@'
                warehouse[rob_y][rob_x] = '.'
            else:
                return

        # Veritical push
        if dx == 0:
            queue = []
            queue.append((cur_y, cur_x))
            chain_positions.append((cur_y, cur_x))

            if warehouse[cur_y][cur_x] == '[':
                queue.append((cur_y, cur_x+1))
                chain_positions.append((cur_y, cur_x+1))
            elif warehouse[cur_y][cur_x] == ']':
                queue.append((cur_y, cur_x-1))
                chain_positions.append((cur_y, cur_x-1))

            move = False
            next_queue = []

            while True:

                if queue:
                    cur_y, cur_x = queue.pop()
                    cur_y += dy
                    cur_x += dx

                    if warehouse[cur_y][cur_x] == "#":
                        break
                    if warehouse[cur_y][cur_x] == '[':
                        if (cur_y, cur_x) not in chain_positions:
                            next_queue += [(cur_y, cur_x), (cur_y, cur_x + 1)]
                            chain_positions += [(cur_y, cur_x), (cur_y, cur_x + 1)]
                    elif warehouse[cur_y][cur_x] == ']':
                        if (cur_y, cur_x) not in chain_positions:
                            next_queue += [(cur_y, cur_x), (cur_y, cur_x - 1)]
                            chain_positions += [(cur_y, cur_x), (cur_y, cur_x - 1)]

                elif next_queue:
                    queue = next_queue
                    next_queue = []
                    continue

                else:
                    move = True
                    break

            if move:
                for y_pos, x_pos in reversed(chain_positions):
                    warehouse[y_pos + dy][x_pos + dx] = warehouse[y_pos][x_pos]
                    warehouse[y_pos][x_pos] =  '.'

                warehouse[rob_y + dy][rob_x + dx] = '@'
                warehouse[rob_y][rob_x] = '.'




def part2():
    with open('input', 'r') as f:
        warehouse, moves = extract_2(f.read())


    for move in moves:
        step_2(warehouse, move)


    result = 0
    for y, row in enumerate(warehouse):
        for x, val in enumerate(row):
            if val == "[":
                result += 100*y + x

    print(result)




part1()
part2()