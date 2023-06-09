import random
from random import randint
from genetic_path_calculation import Genetic_Computation

# dict of str : tuple
poins_to_visit:list[tuple] = []
random.seed(66)

for i in range(20) :
    poins_to_visit.append((randint(-500, 500), randint(-500, 500)))
    
my_genetic_paths = Genetic_Computation(poins_to_visit)
my_genetic_paths.generate_path_population(40)
my_genetic_paths.evaluate_path_population()
#print(my_genetic_paths.population)

ordered_genetic_paths = my_genetic_paths.select_best_paths()
for path in ordered_genetic_paths : # Check if the quicksort of the paths takes effect.
    print(path['length'])

my_genetic_paths.crossbreed_and_mutate()