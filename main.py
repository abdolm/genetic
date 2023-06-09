import random
from random import randint
from genetic_path_calculation import Genetic_Computation

# dict of str : tuple
points_to_visit:list[tuple] = []

for i in range(20) :
    points_to_visit.append((randint(-500, 500), randint(-500, 500)))
    
my_genetic_paths = Genetic_Computation(points_to_visit)
my_genetic_paths.generate_path_population(200)
my_genetic_paths.evaluate_path_population()
#print(my_genetic_paths.population)

my_genetic_paths.sort_best_paths()
my_genetic_paths.divide_best_paths()
# print(my_genetic_paths.population[0]) # Show the current better path

# Generate mutations and crossbreed and create a new population
my_genetic_paths.crossbreed_and_mutate()
my_genetic_paths.evaluate_path_population()
my_genetic_paths.sort_best_paths()
my_genetic_paths.divide_best_paths()
print(f"The best path founded is : {my_genetic_paths.population[0]['path']} \n"
        f"for a distance of : {my_genetic_paths.population[0]['length']}")

while(input("Do you want to continue ?\ny or n : "))=='y':

    my_genetic_paths.crossbreed_and_mutate()
    my_genetic_paths.evaluate_path_population()
    my_genetic_paths.sort_best_paths()
    my_genetic_paths.divide_best_paths()
    print(f"The best path founded is : {my_genetic_paths.population[0]['path']} \n"
          f"for a distance of : {my_genetic_paths.population[0]['length']}")

print('Good bye')
