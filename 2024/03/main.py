import re

def part_1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    input_string = ''.join(lines)

    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.finditer(pattern, input_string)

    result = 0
    for match in matches:
        num1, num2 = match.groups()
        result += int(num1) * int(num2)

    print(result)



def part_2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    input_string = ''.join(lines)

    events = []

    for match in re.finditer(r"mul\((\d+),(\d+)\)", input_string):
        index = match.start()
        num1, num2 = match.groups()
        events.append((index, 'mul', int(num1) * int(num2)))

    for match in re.finditer(r"do\(\)", input_string):
        index = match.start()
        events.append((index, 'do'))

    for match in re.finditer(r"don\'t\(\)", input_string):
        index = match.start()
        events.append((index, 'dont'))

    result = 0
    do_flag = True
    events.sort(key=lambda x: x[0])

    for event in events:
        match event[1]:
            case 'mul':
                if do_flag:
                    result += event[2]
            case 'do':
                do_flag = True
            case 'dont':
                do_flag = False
    

    print(result)

part_1()
part_2()