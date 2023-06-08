import random
from random import randint
from genetic_path_calculation import Genetic_Computation

# dict of str : tuple
poins_to_visit:list[tuple] = []
random.seed(67)

for i in range(20) :
    poins_to_visit.append((randint(-500, 500), randint(-500, 500)))
    
my_genetic_paths = Genetic_Computation(poins_to_visit)
my_genetic_paths.generate_path_population(2)