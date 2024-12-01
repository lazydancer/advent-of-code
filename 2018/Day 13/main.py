import re
import copy

def tick(tracks, carts):

  # Move
  for cart in carts:
    if cart[2] == 'up':
      cart[0] -= 1
    elif cart[2] == 'right':
      cart[1] += 1
    elif cart[2] == 'down':
      cart[0] += 1
    elif cart[2] == 'left':
      cart[1] -= 1
    else:
      print("ERROR: No direction for the cart")

  #Direction for next move

  for cart in carts:
    track = tracks[cart[0]][cart[1]]
    if track == '-' or track == '|':
      continue
    elif track == '/':
      
      if cart[2] == 'up':
        cart[2] = 'right' 
      elif cart[2] == 'right':
        cart[2] = 'up'
      elif cart[2] == 'down':
        cart[2] = 'left'
      elif cart[2] == 'left':
        cart[2] = 'down'


    elif track == '?':
      
      if cart[2] == 'up':
        cart[2] = 'left' 
      elif cart[2] == 'right':
        cart[2] = 'down'
      elif cart[2] == 'down':
        cart[2] = 'right'
      elif cart[2] == 'left':
        cart[2] = 'up'

    elif track == '+':
      if cart[3] == 'left':
        
        if cart[2] == 'up':
          cart[2] = 'left'
        elif cart[2] == 'right':
          cart[2] = 'up'
        elif cart[2] == 'down':
          cart[2] = 'right'
        elif cart[2] == 'left':
          cart[2] = 'down'

        cart[3] = 'straight'

      elif cart[3] == 'straight':
        cart[3] = 'right'

      elif cart[3] == 'right':
        if cart[2] == 'up':
          cart[2] = 'right'
        elif cart[2] == 'right':
          cart[2] = 'down'
        elif cart[2] == 'down':
          cart[2] = 'left'
        elif cart[2] == 'left':
          cart[2] = 'up'

        cart[3] = 'left'

  return True

def collision(carts):

  collisionCarts = set()

  cartsCopy = copy.deepcopy(carts)

  cartLocations = [[y, x] for y,x,_,_ in cartsCopy]
  
  # Move
  for i in range(len(cartsCopy)):
    if cartsCopy[i][2] == 'up':
      cartsCopy[i][0] -= 1
    elif cartsCopy[i][2] == 'right':
      cartsCopy[i][1] += 1
    elif cartsCopy[i][2] == 'down':
      cartsCopy[i][0] += 1
    elif cartsCopy[i][2] == 'left':
      cartsCopy[i][1] -= 1
    else:
      print("ERROR: No direction for the cartsCopy[i]")

    for j in range(len(cartsCopy)):
      for k in range(len(cartsCopy)):
        if j!=k and cartsCopy[j][:2] == cartsCopy[k][:2]:
          collisionCarts.add(j)
          collisionCarts.add(k)

  for index in sorted(collisionCarts, reverse=True):
    del carts[index]



  return carts

def getCartLocations(tracks):
  #carts = [[y, x, direction, nextIntersectionDir],...]
  #direction: up, right, down, left
  #nextIntersectionDir: left, straight, right 
  carts = []

  cartOptions = {
    "^" : "up",
    ">" : "right",
    "v" : "down",
    "<" : "left",
  }

  for y in range(len(tracks)):
    for x in range(len(tracks[0])):
      if tracks[y][x] in cartOptions:
        carts.append([y, x, cartOptions[tracks[y][x]], 'left'])

  return carts


def printState(tracks, carts):
  
  tracksList = copy.deepcopy(tracks)
  tracksList = [[x for x in l] for l in tracksList] 

  cartSymbols = {
    'up': '^',
    'right': '>',
    'down': 'v',
    'left': '<',
  }

  for cart in carts:
    tracksList[cart[0]][cart[1]] = cartSymbols[cart[2]]

  tracksList = ["".join(l) for l in tracksList]
  print("\n".join(tracksList))

def main(tracks):

    

  # \ is a difficult char to work with, replace with ?
  for track in tracks:
    track = re.sub(r'[\\]','?', track) 
  
  carts = getCartLocations(tracks)

  #Remove carts from track
  for track in tracks:
    track = re.sub(r'>|<','-', track)
    track = re.sub(r'\^|v','|', track)

  #While nothing has hit:
  #Part 1
  #for i in range(1000):
  #  tick(tracks, carts)
  #  printState(tracks, carts)
  #  collision(carts)

  #Part 2
  for i in range(100000):
    tick(tracks, carts)
    printState(tracks, carts)
    carts = collision(carts)

    if len(carts) <= 1:
      tick(tracks, carts)
      #printState(tracks, carts)
      print('Part2:', carts[0][1], carts[0][0])
      return


  return

inputFile = open('input', 'r')
#tracks = inputFile.readlines()

tracks = ['/->--\\','|    |','|    ^','|    |','\\-->-/']
#tracks = "/->-\\        \n|   |  /----\\\n| /-+--+-\\  |\n| | |  | v  |\n\\-+-/  \\-+--/\n  \\------/   \n"

main(tracks)

