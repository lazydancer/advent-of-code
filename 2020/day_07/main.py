from collections import namedtuple


class Bag:
	def __init__(self, count, colour, contents):
		self.count = count
		self.colour = colour
		self.contents = contents

	def __str__(self):
		s = str(self.count) + ' ' + str(self.colour)

		s += ' ['
		for b in self.contents:
			s += ' ' + b.count + ' ' + b.colour + ','
		s += ']'

		return s


def extract_bags():
	
	bags = dict()

	with open('input.txt', 'r') as file:
		for line in file:
			line = line.split(' ')
			colour = line[0] + ' ' + line[1]

			contents = []
			if line[4] + ' ' + line[5] != 'no other':
				for i in range(int((len(line) - 4) / 4)):
					contents.append((int(line[4*i+4]), line[4*i+5] + ' ' + line[4*i+6]))

			bags[colour] = contents

	return bags


def contains_colour(b, bags, colour):


	if b == colour:
		return True

	is_found = False
	for a in bags[b]:
		if contains_colour(a[1], bags, colour):
			is_found = True

	return is_found


def count_bags(bags, colour):
	result = 1

	for a in bags[colour]:
		result += a[0]*count_bags(bags, a[1])
		print(colour, a, result)

	return result


def main():
	bags = extract_bags()	
	
	result = 0
	for b in bags.keys():
		print(b, result)
		if contains_colour(b, bags, 'shiny gold'):
			result += 1


		# print(b)

	result -= 1 # remove self

	print(result)

	print(count_bags(bags, 'shiny gold') - 1)

main()