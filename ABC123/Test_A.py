import pytest
from A import solve


def test_solve():
    assert solve('1\n2\n4\n8\n9\n15') == 'Yay!'
    assert solve('15\n18\n26\n35\n36\n18') == ':('
