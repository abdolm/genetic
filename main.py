import random
from random import randint

# dict of str : tuple
planet_positions = {
    "origin" : (0, 0)
}
random.seed(67)

char = 'a'
for i in range(0,20) :
    print (char)  
    planet_positions[char] = (randint(-500, 500), randint(-500, 500))
    char = chr(ord(char) + 1)
    
  
