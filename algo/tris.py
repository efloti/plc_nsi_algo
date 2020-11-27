"""Implémentation de différents algorithmes de tris."""

def tri_selection(tab):
    pass

def tri_insertion(tab):
    pass

def tri_bulle(tab):
    for i in range(len(tab)):
        for j in range(len(tab) - 1, i, -1):
            if tab[j-1] > tab[j]:
                tab[j - 1], tab[j] = tab[j], tab[j - 1]

def tri_fusion(tab):
    pass
