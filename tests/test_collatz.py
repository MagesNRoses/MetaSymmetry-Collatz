def test_region_classification():
    assert classify_region(2.0) == 'A'   # x > ε > log2(3)
    assert classify_region(1.2) == 'B'   # ε > x > log2(3)
    assert classify_region(0.5) == 'C'   # log2(3) > x > ε
    assert classify_region(0.05) == 'D'  # log2(3) > ε > x