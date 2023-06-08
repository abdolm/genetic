import random
from random import randint

# dict of str : tuple
planet_positions = []
random.seed(67)
for i in range(20) :
    planet_positions.append((randint(-500, 500), randint(-500, 500)))
    
print(planet_positions)    
  
