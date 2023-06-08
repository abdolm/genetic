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

    def quicksort_dict(path_dist:dict) -> dict :
        """"""
        if len(path_dist) <= 1:
            return path_dist
    
        pivot_index = len(path_dist) - 1
        pivot = path_dist[pivot_index]
        
        liste_gauche = [elt for elt in path_dist[:pivot_index] if elt <= pivot]
        liste_droite = [elt for elt in path_dist[:pivot_index] if elt > pivot]
        
        return quicksort_dict(liste_gauche) + [pivot] + quicksort_dict(liste_droite)

    def select_best_paths(self) :
        from quicksort import quicksort
        """"""
