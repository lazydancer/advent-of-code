def main():

	inputFile = open('day1_input', 'r')
	
	changeOfFrequencies = [int(line) for line in inputFile.readlines()]

	print('Part 1 result is: ', sum(changeOfFrequencies)) # 493

	seenFrequencies = set()
	i = 0
	frequency = 0

	while frequency not in seenFrequencies:
		
		seenFrequencies.add(frequency)

		frequency += changeOfFrequencies[i]

		if i < len(changeOfFrequencies)-1:
			i += 1
		else: 
			i = 0


	print('Part 2 result is: ', frequency) # 413

main()