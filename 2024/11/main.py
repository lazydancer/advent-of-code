def part1():
    with open('input', 'r') as f:
        stones = [int(n) for n in f.read().strip().split()]


    def apply_rules(stones):
        result = []
        for stone in stones:
            if stone == 0:
                result.append(1)
                continue

            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                left = int(stone_str[:len(stone_str)//2])
                right = int(stone_str[len(stone_str)//2:])
                result.append(left)
                result.append(right)
                continue

            result.append(stone * 2024)

        return result


    print(0, stones)
    for i in range(75):
        stones = apply_rules(stones)
        print(i, len(stones))


from collections import defaultdict

def part2():
    with open('input', 'r') as f:
        stones = [int(n) for n in f.read().strip().split()]

    def rules(stone):
        if stone == 0:
            return [1]

        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            left = int(stone_str[:len(stone_str)//2])
            right = int(stone_str[len(stone_str)//2:])
            return [left, right]

        return [stone * 2024]



    stone_dict = defaultdict(int)
    for s in stones:
        stone_dict[s] += 1

    for i in range(75):
        new_state = defaultdict(int)
        for s in stone_dict:
            for n in rules(s):
                new_state[n] += stone_dict[s]

        stone_dict = new_state
    

    result = sum(stone_dict.values())

    print(result)

part2()

