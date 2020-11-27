import pytest
import time
from algo.tris import tri_selection, tri_insertion, tri_bulle, tri_fusion

liste_fonctions = [tri_selection, tri_insertion, tri_bulle, tri_fusion]


def grandes_listes():
    import random
    aleatoire = [random.randint(1, 2000) for _ in range(5000)]
    tri_fait = grande_liste.copy()
    tri_fait.sort()
    return aleatoire, tri_fait


grande_liste, grande_l_attendue = grandes_listes()


@pytest.mark.parametrize("tab,attendu", [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([12, 53, 27, 2, 6], [2, 6, 12, 27, 53]),
        (grande_liste, grande_l_attendue),

    ])
def test_tous_tris_basile(tab, attendu):
    # doit tester que les différents algorithmes de tris tries effectivement
    # les tableaux qu'on leur soumet
    for i in range(len(liste_fonctions)):
        test_tab = tab.copy()
        t1 = time.time()
        liste_fonctions[i](test_tab)
        print("\n"+str(time.time()-t1))
        assert test_tab == attendu
