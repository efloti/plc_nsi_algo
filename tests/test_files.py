from algo.struct.files import File1, File2, File3, File4
import pytest

def test_file1():
    file = File1()
    assert len(file) == 0
    file.enfiler(1)
    file.enfiler(2)
    assert len(file) == 2
    assert file[0] == 1
    assert file[1] == 2
    file.defiler()
    assert len(file) == 1
    assert file[0] == 2
    file.defiler()
    file.enfiler(1)
    file.enfiler(2)
    assert str(file) == '2 → 1'

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
