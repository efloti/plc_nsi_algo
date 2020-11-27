from algo.tris import tri_selection, tri_insertion, tri_bulle, tri_fusion

def test_tris():
    # doit tester que les différents algorithmes de tris tries effectivement
    # les tableaux qu'on leur soumet
    tableau = [7, 8, 4, 0, -3]
    tableau_bis = [9, 8, 7, 6]
    tableau_ter = [1, 2, 3, 4, 5]
    tableau_vide = []
    tri_bulle(tableau)
    tri_bulle(tableau_bis)
    tri_bulle(tableau_ter)
    tri_bulle(tableau_vide)
    assert tableau == [-3, 0, 4, 7, 8]
    assert tableau_bis == [6, 7, 8, 9]
    assert tableau_ter == [1, 2, 3, 4, 5]
    assert tableau_vide == []

