from algo.struct.files import File1, File2, File3, File4
import pytest

def test_len():
    assert False # à remplacer...

def test_enfiler():
    assert False

def test_defiler():
    assert False

def test_str():
    assert False

def test_file_quatre():
    f = File4(5)
    f.enfiler(1)
    f.enfiler(2)
    f.enfiler(3)
    assert not f.est_vide()
    assert str(f) == "1 -> 2 -> 3"
    assert f.defiler() == 1
    f.enfiler(4)
    f.enfiler(5)
    f.enfiler(6)
    assert len(f) == 5
    assert f.defiler() == 2
    assert str(f) == "3 -> 4 -> 5 -> 6"
