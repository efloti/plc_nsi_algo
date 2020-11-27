import pytest

from algo.struct.files import File1, File2, File3, File4
import pytest

def test_len_file3():
    file = File3()
    assert len(file) == 0
    file.enfiler(1)
    assert len(file) == 1
    file.enfiler(2)
    assert len(file) == 2
    file.enfiler(3)
    file.enfiler(4)
    file.enfiler(12)
    file.enfiler("bonjour")
    assert len(file) == 6


def test_enfiler_file3():
    file = File3()
    assert str(file) == "None"
    file.enfiler(1)
    assert str(file._entree) == "1"
    file.enfiler(3)
    assert str(file._entree) == "3 → 1"


def test_defiler_file3():
    file = File3()
    with pytest.raises(IndexError):
        file.defiler()
    file.enfiler(1)
    assert file.defiler() == 1
    file.enfiler(1)
    file.enfiler(2)
    file.enfiler(3)
    file.enfiler(4)
    assert file.defiler() == 1
    assert str(file._entree) == "None"
    assert str(file._sortie) == "2 → 3 → 4"
    assert file.defiler() == 2
    assert str(file._sortie) == "3 → 4"


def test_str_file3():
    file = File3()
    assert str(file) == "None"
    file.enfiler(4)
    assert str(file) == "4"
    file.enfiler(5)
    assert str(file) == "5 → 4"
    file.enfiler("abc")
    assert str(file) == "abc → 5 → 4"
    file.defiler()
    assert str(file) == "abc → 5"


def test_eq_file3():
    file1 = File3()
    file1.enfiler(2)
    file1.enfiler(3)
    file2 = File3()
    file2.enfiler(1)
    file2.enfiler(2)
    file2.enfiler(3)
    assert file1 != file2
    file2.defiler()
    assert file1 == file2


def test_copy_file3():
    file1 = File3()
    file1.enfiler(2)
    file1.enfiler(3)
    file2 = file1.copy()
    assert file1 == file2
    file2.defiler()
    assert file1 != file2

def test_len():
    file1 = File1()
    assert len(file1) == 0

def test_enfiler():
    file = File1()
    file.enfiler(1)
    file.enfiler(2)
    assert len(file) == 2
    assert file[0] == 1
    assert file[1] == 2

def test_defiler():
    file = File1()
    file.enfiler(1)
    file.enfiler(2)
    file.defiler()
    assert len(file) == 1
    assert file[0] == 2

def test_str():
    file = File1()
    file.enfiler(1)
    file.enfiler(2)
    assert str(file) == '1 → 2'

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
