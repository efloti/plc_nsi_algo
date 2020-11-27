import pytest

from algo.struct.files import File1, File2, File3, File4


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
