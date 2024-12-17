def extract(text):
    register_text, program_text = text.split("\n\n")

    registers = list(map(int, register_text.split()[2::3]))
    program = list(map(int, program_text.split()[1].split(',')))

    return registers, program


def run_program(a,b,c, program):
    instruction_pointer = 0
    output = []
    registers = [a, b, c]

    while instruction_pointer < len(program):

        code = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        combo = None
        if operand in [0,1,2,3]:
            combo = operand
        elif operand == 4:
            combo = registers[0]
        elif operand == 5:
            combo = registers[1]
        elif operand == 6:
            combo = registers[2]

        instruction_pointer += 2

        match code:
            case 0: #adv 
                registers[0] = registers[0] // (2**combo)
            case 1: #bxl
                registers[1] = registers[1] ^ operand
            case 2: #bst
                registers[1] = combo % 8
            case 3: #jnz
                if registers[0] != 0:
                    instruction_pointer = operand
            case 4: #bxc
                registers[1] = registers[1] ^ registers[2]
            case 5: #out
                output.append(combo % 8)
            case 6: #bdv
                registers[1] = registers[0] // (2**combo)
            case 7: #cdv
                registers[2] = registers[0] // (2**combo)

    return output




def part1():
    with open('input', 'r') as f:
        registers, program = extract(f.read())

    return run_program(registers[0], registers[1], registers[2], program)



def part2():
    with open('input', 'r') as f:
        _, program = extract(f.read())


    start_cursor = len(program) -1

    stack = [(start_cursor, 0, 0)]
    
    while stack:
        cursor, sofar, candidate = stack.pop()
        
        if candidate >= 8:
            continue
        
        new_sofar = sofar * 8 + candidate
        if run_program(new_sofar, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return new_sofar
            
            stack.append((cursor, sofar, candidate + 1))
            stack.append((cursor - 1, new_sofar, 0))
        else:
            stack.append((cursor, sofar, candidate + 1))



print(part1())
print(part2())