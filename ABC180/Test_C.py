import pytest
from C import solve


def test_solve():
    assert solve('6') == '1\n2\n3\n6'
    assert solve('9') == '1\n3\n9'
    assert solve('720') == '1\n2\n3\n4\n5\n6\n8\n9\n10\n12\n15\n16\n18\n20\n24\n30\n36\n40\n45\n48\n60\n72\n80\n90\n120\n144\n180\n240\n360\n720'
    assert solve('1000000007') == '1\n1000000007'
