def printLights(lights):

  minX = min(lights, key=lambda light:light[0])[0]
  minY = min(lights, key=lambda light:light[1])[1]

  for light in lights:
    light[0] -= minX
    light[1] -= minY
  
  width = max(lights, key=lambda light:light[0])[0] + 1
  height = max(lights, key=lambda light:light[1])[1] + 1

  print(width, height)

  array = [['.' for i in range(width)] for j in range(height)]
  
  print('after array')
  for light in lights:
    array[light[1]][light[0]] = '#'

  
  for y in range(height):
    print(''.join(array[y]))

def run(lights):

  for light in lights:
    light[0] += light[2]
    light[1] += light[3]

  return lights


def main():

  inputFile = open('input', 'r')
  lines = inputFile.readlines()

  lights = []
  for line in lines:
    lights.append([int(line[10:16]), int(line[18:24]), int(line[36:38]), int(line[40:42])])

  for i in range(10888):
    lights = run(lights)
  
  printLights(lights)
  print("")

main()


