
def run(instructions):
	pointer = 0
	accumulator = 0
	return_code = ''

	pointer_history = []

	while True:
		if pointer in pointer_history:
			return_code = 'loop'
			break # program loops

		pointer_history.append(pointer)

		if pointer >= len(instructions):
			return_code = 'normal'
			break # program terminates

		op, arg = instructions[pointer]

		if op == 'nop':
			pointer += 1
		elif op == 'acc':
			accumulator += arg
			pointer += 1
		elif op == 'jmp':
			pointer += arg
		else:
			raise Error('operation', op, 'unknown')


	return return_code, accumulator


def get_instructions():
	def clean_instruction(x):
		x = x.replace('\n', '').split(' ')
		x[1] = int(x[1])
		return x

	with open('input.txt', 'r') as f:
		instructions = list(map(clean_instruction, f.readlines()))

	return instructions

def main():

	instructions = get_instructions()


	# Part 1
	return_code, result = run(instructions)
	print(result)


	# Part 2
	ids = [i for i in range(len(instructions)) if instructions[i][0] == 'nop' or instructions[i][0] == 'jmp']
	for i in ids:
		instructions[i][0] = 'nop' if instructions[i][0] == 'jmp' else 'jmp'
			

		return_code, result = run(instructions)
		if return_code == 'normal':
			print(result)


		instructions[i][0] = 'nop' if instructions[i][0] == 'jmp' else 'jmp'


	a = 675_412

	print(a)

main()	