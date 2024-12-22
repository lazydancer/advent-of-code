

def next_secret(s):
    s = ((s * 64) ^ s) % 16777216
    s = ((s // 32) ^ s) % 16777216
    s = ((s * 2048) ^ s) % 16777216
    return s



def part1():
    with open('input', 'r') as f:
        secret_numbers = [int(line.rstrip('\n')) for line in f]

    result = 0
    for secret_number in secret_numbers:
        for i in range(2000):
            secret_number = next_secret(secret_number)

        result += secret_number

    print(result)


from itertools import pairwise
from collections import defaultdict


def part2():
    with open('input', 'r') as f:
        secret_numbers = [int(line.rstrip('\n')) for line in f]

    result = defaultdict(int)
    for s in secret_numbers:
        nums = [s] + [s := next_secret(s) for _ in range(2000)]

        diffs = [b%10 - a%10 for a,b in pairwise(nums)]

        seen = set()
        for i in range(len(nums)-4):
            pat = tuple(diffs[i:i+4])
            if pat not in seen:
                result[pat] += nums[i+4] % 10
                seen.add(pat)

    print(max(result.values()))

part1()
part2()