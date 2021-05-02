def moyenne(tab):
    if not tab:
        return 'erreur'
    else:
        total = 0
        for i in tab:
            total += i
        return total / len(tab)


print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([]))