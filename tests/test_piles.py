from algo.struct.piles import Pile1, Pile2, Pile3
pile2 = Pile2()

def test_len():
    pile2.empiler(1)
    pile2.empiler(5)
    pile2.empiler(3)
    pile2.empiler(2)
    assert len(pile2) == 4

def test_empiler():
    pile2.empiler(1)
    pile2.empiler(5)
    pile2.empiler(3)
    pile2.empiler(2)
    assert str(pile2) == "1,5,3,2" \
           and len(pile2) == 4


def test_depiler():
    pile2.empiler(1)
    pile2.empiler(5)
    pile2.empiler(3)
    pile2.empiler(2)
    pile2.depiler()
    assert str(pile2) == "1,5,3" \
           and len(pile2) == 3

def test_str():
    pile2.empiler(1)
    pile2.empiler(5)
    pile2.empiler(3)
    pile2.empiler(2)
    assert str(pile2) == "1,5,3,2"