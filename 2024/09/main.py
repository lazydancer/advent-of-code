def part1():
    with open('input', 'r') as f:
        numbers = [int(n) for n in f.read().strip()]


    current_id = 0
    memory = []
    for i, num in enumerate(numbers):
        if( i % 2 ):
            memory += [-1] * num # -1 is the empty number
        else: 
            memory += [current_id] * num
            current_id += 1


    while True:
        left_index = memory.index(-1)

        for i, right_value in enumerate(reversed(memory)):
            if right_value != -1:
                right_index = len(memory) - 1 - i
                break

        if left_index >= right_index:
            break

        memory[left_index] = right_value
        memory[right_index] = -1

    checksum = 0
    for i, v in enumerate(memory):
        if(v == -1): continue
        checksum += i * v

    print(checksum)


def part2():
    with open('input', 'r') as f:
        numbers = [int(n) for n in f.read().strip()]

    current_id = 0
    compacted_memory = []
    for i, num in enumerate(numbers):
        if( i % 2 ): # odd
            compacted_memory.append([-1, num]) # -1 is the empty number
        else: # even
            compacted_memory.append([current_id, num])
            current_id += 1


    for i, right_value in enumerate(reversed(compacted_memory)):
        if (right_value[0] == -1 ): continue

        right_index = len(compacted_memory) - 1 - i
        for left_index, left_value in enumerate(compacted_memory):
            if left_index >= right_index:
                break

            if left_value[0] == -1 and left_value[1] >= right_value[1]:
                compacted_memory[right_index - 1][1] += right_value[1]
                compacted_memory.pop(right_index)

                compacted_memory.insert(left_index, right_value)
                compacted_memory[left_index + 1][1] -= right_value[1]
                break


    memory = []
    for cell in compacted_memory:
        memory += [cell[0]] * cell[1]

    checksum = 0
    for i, v in enumerate(memory):
        if(v == -1): continue
        checksum += i * v

    print(checksum)

part1()
part2()
