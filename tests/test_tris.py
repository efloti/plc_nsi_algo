from algo.tris import tri_selection, tri_insertion, tri_bulle, tri_fusion

def test_tris():
    t = [5, 7, 4, 6]
    assert tri_selection(t) == [4, 5, 6, 7 ]

