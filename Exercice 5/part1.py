def convertir(T):
    """
     T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
     représentant un entier écrit en binaire. Renvoie l'écriture
     décimale de l'entier positif dont la représentation binaire
     est donnée par le tableau T
    """
    total = 0
    for i in range(len(T)):
        if T[i] == 1:
            total += 2**(len(T)-i-1)
    return total


print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))