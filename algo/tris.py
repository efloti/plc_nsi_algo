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
    new = tri_fusion_separation(tab)
    for i in range(len(tab)):
        tab[i] = new[i]


def tri_fusion_separation(tab):
    n = len(tab)
    if n == 1:
        return tab
    m = n // 2
    return tri_fusion_melange(
        tri_fusion_separation(tab[:m]),
        tri_fusion_separation(tab[m:]))


def tri_fusion_melange(tab1, tab2):
    tab = []
    i, j, n1, n2 = 0, 0, len(tab1), len(tab2)
    while i < n1 and j < n2:
        nb1, nb2 = tab1[i], tab2[j]
        if nb1 < nb2:
            tab.append(nb1)
            i += 1
        else:
            tab.append(nb2)
            j += 1
    if i == n1:
        tab.extend(tab2[j:])
    else:
        tab.extend(tab1[i:])
    return tab
