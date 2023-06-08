def quicksort(liste:list) -> list:
    if len(liste) <= 1:
        return liste
    
    pivot_index = len(liste) - 1
    pivot = liste[pivot_index]
    
    liste_gauche = [elt for elt in liste[:pivot_index] if elt <= pivot]
    liste_droite = [elt for elt in liste[:pivot_index] if elt > pivot]
    
    return quicksort(liste_gauche) + [pivot] + quicksort(liste_droite) 

#print(quicksort([0, 0, 1, 15, 20, -4, 2, 1, 7, 18, 7]))