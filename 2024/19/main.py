from functools import cache


def part1():
    with open('input', 'r') as f:
        patterns_text, designs_text = f.read().strip().split("\n\n")
        patterns = patterns_text.split(', ')
        towels = designs_text.split('\n')

    @cache
    def arrange(towel):
        if towel == "":
            return True

        for pattern in patterns:
            if towel.startswith(pattern):
                match = arrange(towel[len(pattern):])
                if match:
                    return True

        return False


    result = 0
    for towel in towels:
        if arrange(towel):
            result += 1

    print(result)



def part2():
    with open('input', 'r') as f:
        patterns_text, designs_text = f.read().split("\n\n")
        patterns = patterns_text.split(', ')
        towels = designs_text.split('\n')

    @cache
    def arrange(towel):
        if towel == "":
            return 1

        total = 0
        for pattern in patterns:
            if towel.startswith(pattern):
                total += arrange(towel[len(pattern):])

        return total

    result = 0
    for towel in towels:
        count = arrange(towel)
        result += count
    print(result)


part1()
part2()
