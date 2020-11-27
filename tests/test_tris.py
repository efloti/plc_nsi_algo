from algo.tris import tri_selection, tri_insertion, tri_bulle, tri_fusion

def test_tris():
    tab1 = [1,7,6,8,1,3,4]
    tab2 = [10,80,7,5,94,27,54]

    res1 = tri_selection(tab1)
    res2 = tri_selection(tab2)
    res3 = tri_insertion(tab1)
    res4 = tri_insertion(tab2)
    res5 = tri_bulle(tab1)
    res6 = tri_bulle(tab2)

    assert res1 == [1, 1, 3, 4, 6, 7, 8]
    assert res2 == [5, 7, 10, 27, 54, 80, 94]
    assert res3 == [1, 1, 3, 4, 6, 7, 8]
    assert res4 == [5, 7, 10, 27, 54, 80, 94]
    assert res5 == [1, 1, 3, 4, 6, 7, 8]
    assert res6 == [5, 7, 10, 27, 54, 80, 94]
