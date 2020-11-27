from algo.struct.piles import Pile1, Pile2, Pile3

def test_len():
    assert False # à remplacer...

def test_empiler():
    assert False

def test_depiler():
    assert False

def test_str():
    assert False

def test_pile_trois():
    p = Pile3()
    p.empiler(1)
    p.empiler(2)
    assert len(p) == 2
    assert p.depiler() == 2
    p.depiler()
    assert len(p) == 0
