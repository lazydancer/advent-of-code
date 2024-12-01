import fileinput


# def main():

# 	customs_forms = list(map(str,fileinput.input()))
# 	customs_forms = ''.join(customs_forms)

# 	# TODO: replace with double new line for cross platform
# 	groups = customs_forms.split('\n\n')


# 	result = 0
# 	for grp in groups:
# 		grp = grp.replace('\n','')
		
# 		print(set(grp))
# 		result += len(set(grp))


# 	print(result)

# 	breakpoint()



def main2():

	group = []
	result = 0

	for line in fileinput.input():
		line = line.replace('\n', '')		

		if line != '':
			group.append(set(line))
		else:
			charaters = set.intersection(*group)
			print(charaters)
			result += len(charaters)
			group = []


	charaters = set.intersection(*group)
	result += len(charaters)


	print(result)

def main1():

	customs_forms = list(map(str,fileinput.input()))
	customs_forms = ''.join(customs_forms)

	groups = customs_forms.split('\n\n')

	result = 0
	for grp in groups:
		grp = grp.replace('\n','')
		
		print(set(grp))
		result += len(set(grp))


	print(result)

main1()
main2()