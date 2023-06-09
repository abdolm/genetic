class Genetic_Computation :
    
    def __init__(self, points_to_visit:list[tuple]) -> None:
        self.points_to_visit = points_to_visit
        self.population = []

    def generate_path_population(self, population_size:int) -> list[dict]:
        """Generate (population_count) random paths from origin to a random point 
        and return a list of dictionary corresponding to those paths

        Args:
            population_count (int): How many paths to generate

        Returns:
            list[dict]: a list of dictionary corresponding to the paths created
        """
        from random import shuffle

        for _ in range(population_size) :
            points_index = [i for i in range(1, len(self.points_to_visit))]
            shuffle(points_index)
            points_index.insert(0, 0)

            path_dict = {
                "path" : points_index,
                "length" : 0
            }
            self.population.append(path_dict)

    def evaluate_path_population(self) :
        """Calculate distance for each path and set in each of their dictionaries

        Args:
            population_count (int): How many paths to generate

        Returns:
            list[dict]: a list of dictionary corresponding to the paths created
        """

        from distance_calculation import calculate_path_sum
        
        for path_dict in self.population :
            path_dict['length'] = calculate_path_sum(path_dict['path'], self.points_to_visit)

    def select_best_paths(self) :
        """Sort all paths from the smallest dist to browse all points to the biggest and
        devide the result to save 1/3 of the best paths only"""
        
        best_paths = self.quicksort_dict(self.population.copy())
        tier_best_paths = best_paths[:len(best_paths) // 3]
        return tier_best_paths

    def quicksort_dict(self, possible_paths:list[dict]) -> list[dict] :
        """Use the quick sort algorithm on list of dictionary to compare the length of many paths
        and return a sorted list from smallest length ot biggest"""
        if len(possible_paths) <= 1:
            return possible_paths
    
        pivot_index = len(possible_paths) - 1
        pivot = possible_paths[pivot_index]
        liste_gauche = [dict_path for dict_path in possible_paths[:pivot_index] if dict_path['length'] <= pivot['length']]
        liste_droite = [dict_path2 for dict_path2 in possible_paths[:pivot_index] if dict_path2['length'] > pivot['length']]
        
        return self.quicksort_dict(liste_gauche) + [pivot] + self.quicksort_dict(liste_droite)

    def crossbreed_and_mutate(self, possible_paths:list[dict]) -> list[dict] :
        """Generate crossbreed of paths and mutations to try to obtain a new
        set of path wih a possibility of a more interesting result (lower distance)

        Args:
            possible_paths (list[dict]): List which contains each paths of points with their lengths 

        Returns:
            list[dict]: A new list of paths of points generated after crossbreeding and mutations
        """
        from random import randint
        
        new_generation_of_paths:list[dict] = []
        desired_number_of_paths = len(possible_paths) * 3
        
        # First: save the first path which is currently the best option.
        new_generation_of_paths.append(possible_paths[0])

        # Let's make crossbreeding between random paths to create our new generation.
        while len(new_generation_of_paths) < desired_number_of_paths :
            first_path_index = randint(0, len(possible_paths)-1)
            second_path_index = randint(0, len(possible_paths)-1)
            if first_path_index == second_path_index : continue # Avoid having the same path...

            path_points_count = len(possible_paths[first_path_index]['path'])
            fracture_position = randint(
                path_points_count //3, 
                2* (path_points_count // 3)
                )
            print(possible_paths[first_path_index]['path'])

            new_path = [elt for elt in possible_paths[first_path_index]['path'][:fracture_position]]
            print(f"New path beginning : {new_path} with {fracture_position} elements")
            print(f"Second path : {possible_paths[second_path_index]['path']}")
            new_path += [point for point in possible_paths[second_path_index]['path'] if 
                         point not in new_path]
            print(f"Full new path : {new_path}")
            break
            


