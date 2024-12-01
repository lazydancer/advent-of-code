from collections import Counter


def read_input():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    first_list = []
    second_list = []

    for line in lines:
        a = line.split() 
        first_list.append(int(a[0]))
        second_list.append(int(a[1]))
    return first_list, second_list



def part_1():
    first_list, second_list = read_input()

    first_list = sorted(first_list)
    second_list = sorted(second_list)


    result = 0
    for i in range(len(first_list)):
        result += abs(first_list[i] - second_list[i])


    print(result)


def part_2():
    first_list, second_list = read_input()


    second_counter = Counter(second_list)
    result = sum(x * second_counter.get(x, 0) for x in first_list)
    print(result)


part_1()
part_2()


