from algo.struct.piles import Pile1, Pile2, Pile3

def test_pile1():
    pile1 = Pile1()
    pile1.empiler(4)
    pile1.empiler(42)
    pile1.empiler(22)
    pile1.empiler(3)
    pile1.empiler(666)
    assert len(pile1) == 5
    assert str(pile1) == "666 → 3 → 22 → 42 → 4"
    pile1.depiler()
    assert len(pile1) == 4
    assert str(pile1) == "3 → 22 → 42 → 4"

def test_pile2():
    pile2 = Pile2()
    pile2.empiler(1)
    pile2.empiler(5)
    pile2.empiler(3)
    pile2.empiler(2)
    assert len(pile2) == 4
    assert str(pile2) == "1,5,3,2"
    pile2.depiler()
    assert len(pile2) == 3
    assert str(pile2) == "1,5,3"

def test_pile3():
    assert False