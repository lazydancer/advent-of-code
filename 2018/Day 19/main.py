def apply(operation, parameters, register):
  A, B, C = parameters
  result = register[:]


  if operation == 'addr':
    result[C] = result[A] + result[B]
    return result
  if operation == 'addi':
    result[C] = result[A] + B
    return result
  
  if operation == 'mulr':
    result[C] = result[A] * result[B]
    return result
  if operation == 'muli':
    result[C] = result[A] * B
    return result

  if operation == 'banr':
    result[C] = result[A] & result[B]
    return result
  if operation == 'bani':
    result[C] = result[A] & B
    return result

  if operation == 'borr':
    result[C] = result[A] | result[B]
    return result
  if operation == 'bori':
    result[C] = result[A] | B
    return result

  if operation == 'setr':
    result[C] = result[A]
    return result
  if operation == 'seti':
    result[C] = A
    return result

  if operation == 'gtir':
    result[C] = 1 if A > result[B] else 0
    return result
  if operation == 'gtri':
    result[C] = 1 if result[A] > B else 0
    return result
  if operation == 'gtrr':
    result[C] = 1 if result[A] > result[B] else 0
    return result
  
  if operation == 'eqir': 
    result[C] = 1 if A == result[B] else 0
    return result
  if operation == 'eqri':
    result[C] = 1 if result[A] == B else 0
    return result
  if operation == 'eqrr':
    result[C] = 1 if result[A] == result[B] else 0
    return result


lines = open('input').read().strip().split('\n')

pointer = int(lines.pop(0)[4])

register = [1,0,0,0,0,0]

instructions = {}
for i, line in enumerate(lines):
  line = line.split()
  function = line[0]
  parameters = [int(x) for x in line[1:]]
  instructions[i] = (function, parameters)


i = 0
#while register[pointer] < len(lines):
for _ in range(20):

  operation, parameters =  instructions[register[pointer]]
  
  if register[pointer] == 3:
    if register[5] != 0 and register[1] % register[5] == 0:
      register[3] = register[1];
      register[4] = 1;
      register[pointer] = 7;
    else:
      register[3] = register[1] + 1;
      register[4] = 1;
      register[pointer] = 12;
    continue

  result = apply(operation, parameters, register)
  result[pointer] += 1

  print(i, register[pointer], operation, parameters, register, result)

  register = result[:]
  i += 1

print(register)

