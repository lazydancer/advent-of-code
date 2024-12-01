from itertools import combinations

def get_input():
	with open('input.txt', 'r') as f:
		input_numbers = list(map(int, f.read().split('\n')[:-1]))

	return input_numbers


def not_sum_previous(xs):
	preamble_len = 25

	for i in range(preamble_len,len(xs)):

		preamble = xs[i-preamble_len: i]

		sums = [x1 + x2 for (x1, x2) in combinations(preamble, 2)]

		if xs[i] not in sums:
			return xs[i]


def find_sublist(xs, target):

	result = 0
	for i in range(len(xs)):
		for j in range(i, len(xs)):
			result = sum(xs[i:j])
			
			if result == target:
				return xs[i:j]
		
		if result > target:
			continue

def main():


	xs = get_input()


	print(not_sum_previous(xs))

	target = 373803594

	sublist = find_sublist(xs, target)

	print(max(sublist) + min(sublist))

main()