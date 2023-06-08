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
            points_index = self.points_to_visit.copy()
            points_index.pop(0)
            shuffle(points_index)
            points_index.insert(0, self.points_to_visit[0])
            self.population.append(points_index)        

    def evaluate_path_population(self) :
        """"""

    def select_best_paths(self) :
        """"""