## Using genetic algorithm to find a path

Small project made in one day by a team of two developers.

We were learning how to use genetic algorithm and the objective was to : 
- Be able to analyze a huge list of points
- Return a very good path (not the best one, but near it)
- Make crossbreed and mutations to get new path from the ones that we randomly generated

### ***Steps*** :

#### 1) **Generate a population of paths**
Create a huge number of random path from a list of points to browse.
#### 2) **Evaluate our population**
Calculate the distance to browse every point of each paths.
#### 3) **Sort our population**
Sort our population using a sort algorithm (we used the quicksort method for more efficiency).
#### 4) **Crossbreed and mutate**
Create new paths by crossing values of two random paths (taking the first half of one and completing by adding the other values in the right order of the second) 
</br> 
Create mutations by swapping values at random index (switching two index points) 