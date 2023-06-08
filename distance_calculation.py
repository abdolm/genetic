import math

def calculate_distance(first_point:tuple, second_point:tuple) -> float :
    """Take two points (vector 2) and return the distance between them (float)"""
    x1, y1 = first_point
    x2, y2 = second_point
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

def calculate_path_sum(path_of_points:list[tuple]) -> float:
    """Calculate the distance to move to every point in the given order by 
    calculating the distance between a point and the next point."""
    distance = 0
    for i in range(len(path_of_points)-1):
       distance += calculate_distance(path_of_points[i],path_of_points[i+1])
    return distance
        
    
