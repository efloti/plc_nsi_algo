"""Implémentation de différents algorithmes de tris."""

def tri_selection(tab):
    for i in range(len(tab) - 1):
        k = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[k]:
                k = j
        tab[i], tab[k] = tab[k], tab[i]
    return tab

def tri_insertion(tab):
    for i in range(1, len(tab)):
        j = i
        k = tab[i]
        while j > 0 and tab[j - 1] > k:
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = k
    return tab

def tri_bulle(tab):
    for i in range(0, len(tab) - 1):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab

def tri_fusion(tab):
    pass