"""Implémentation de différents algorithmes de tris."""

def tri_selection(tab):
    for i in range(len(tab) - 1):
        k = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[k]:
                k = j
        tab[i], tab[k] = tab[k], tab[i]
    return tab

def tri_insertions(tab):
    pass

def tri_bulle(tab):
    pass

def tri_fusion(tab):
    pass