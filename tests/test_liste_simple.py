import pytest

from algo.struct.liste_simple import Cellule, Liste


def test_cellule():
    c1 = Cellule(0)
    assert c1.valeur == 0
    assert str(c1) == "0"
    assert c1.suivante is None
    c2 = Cellule(1, c1)
    assert c2.suivante is c1
    assert str(c2) == "1 → 0"

def test_liste_str():
    assert str(Liste()) == "None"

def test_inserer_apres():
    l = Liste()
    l._inserer_apres(5)
    assert len(l) == 1
    assert l.tete.valeur == 5 and l.queue.valeur == 5
    assert str(l) == "5"
    l._inserer_apres(2, l.queue)
    assert l.tete.valeur == 5 and l.queue.valeur == 2
    assert len(l) == 2
    assert str(l) == "5 → 2"
    l._inserer_apres(3, l.tete)
    assert len(l) == 3
    assert l.tete.valeur == 5 and l.queue.valeur == 2
    assert str(l) == "5 → 3 → 2"

def test_supprimer_apres():
    l = Liste()
    l._inserer_apres(5)
    l._inserer_apres(2, l.queue)
    l._inserer_apres(3, l.tete)
    v = l._supprimer_apres()
    assert v == 5 and l.tete.valeur == 3 and l.queue.valeur == 2
    assert len(l) == 2 and str(l) == "3 → 2"
    v = l._supprimer_apres(l.tete)
    assert v == 2 and l.tete is l.queue and l.tete.valeur == 3
    assert len(l) == 1 and str(l) == "3"
    v = l._supprimer_apres()
    assert v == 3 and l.tete is None and l.queue is None
    assert len(l) == 0 and str(l) == "None"

def test_in():
    l = Liste()
    l._inserer_apres(5)
    l._inserer_apres(2, l.queue)
    l._inserer_apres(3, l.tete)
    assert 2 in l and 5 in l and 3 in l and 10 not in l

def test_crochet():
    l = Liste()
    l._inserer_apres(5)
    l._inserer_apres(2, l.queue)
    l._inserer_apres(3, l.tete)
    assert l[0] == 5 and l[1] == 3 and l[2] == 2
    with pytest.raises(IndexError):
        assert l[-1]
        assert l[20]
        assert l["truc"]

def test_inserer_tete():
    l = Liste()
    for v in range(5):
        l.inserer_tete(v)
    assert len(l) == 5 and l.tete.valeur == 4 and l.queue.valeur == 0
    assert str(l) == "4 → 3 → 2 → 1 → 0"

def test_inserer_queue():
    l = Liste()
    for v in range(5):
        l.inserer_queue(v)
    assert len(l) == 5 and l.tete.valeur == 0 and l.queue.valeur == 4
    assert str(l) == "0 → 1 → 2 → 3 → 4"

def test_supprimer_tete():
    l = Liste()
    l._inserer_apres(5)
    l._inserer_apres(2, l.queue)
    l._inserer_apres(3, l.tete)
    v = l.supprimer_tete()
    assert v == 5 and len(l) == 2 and l.tete.valeur == 3 and l.queue.valeur == 2
    assert str(l) == "3 → 2"

def test_iteration_avec_for():
    l = Liste()
    for v in range(10):
        l.inserer_queue(v)
    i = 0
    for v in l:
        # fonctionne du fait de la définition de
        # __getitem__; pas efficace!!!!
        # semble traduit en
        # i = 0
        # while True:
        #   try:
        #     v = l[i] # est O(i) (la liste est reparcourue à chaque accès)
        #   except IndexError:
        #      break
        #   i += 1
        #   <corps de boucle>
        #
        assert v == i
        i += 1

def test_setitem():
    l = Liste()
    for _ in range(5):
        l.inserer_queue(0)
    l[2] = 10 
    assert l[2] == 10 and str(l) == "0 → 0 → 10 → 0 → 0"
    with pytest.raises(IndexError):
        assert l[-1]
        assert l[20]
        assert l["truc"]
