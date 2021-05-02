def moyenne (tab):
    """
     moyenne(list) -> float
     Entrée : un tableau non vide d'entiers
     Sortie : nombre de type float
     Correspondant à la moyenne des valeurs présentes dans le tableau
    """
    total = 0
    for i in tab:
        total+=i
    return total/len(tab)

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5