def part_1():
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]

    reports = [[int(n) for n in line.split()] for line in lines]

    count = 0
    for report in reports:
        diffs = [b - a for a, b in zip(report, report[1:])]
        if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
            count += 1

    print(count)

def part_2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    reports = [[int(n) for n in line.split()] for line in lines]
    
    count = 0
    for report in reports:
        for i in range(len(report)):
            sub = report[:i] + report[i+1:]
            sub_diffs = [b - a for a, b in zip(sub, sub[1:])]
            if all(1 <= d <= 3 for d in sub_diffs) or all(-3 <= d <= -1 for d in sub_diffs):
                count += 1
                break

    print(count)

part_1()
part_2()