from algo.struct.files import File1, File2, File3, File4

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