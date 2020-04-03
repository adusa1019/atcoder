import pytest
from B import solve


def test_solve():
    assert solve('84 97 66\n79 89 11\n61 59 7\n7\n89\n7\n87\n79\n24\n84\n30') == 'Yes'
    assert solve('41 7 46\n26 89 2\n78 92 8\n5\n6\n45\n16\n57\n17') == 'No'
    assert solve('60 88 34\n92 41 43\n65 73 48\n10\n60\n43\n88\n11\n48\n73\n65\n41\n92\n34') == 'Yes'
