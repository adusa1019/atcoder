import pytest
from C import solve


def test_solve():
    assert solve('3 4 3\n1 3 3 100\n1 2 2 10\n2 3 2 10') == '110'
    assert solve('4 6 10\n2 4 1 86568\n1 4 0 90629\n2 3 0 90310\n3 4 1 29211\n3 4 3 78537\n3 4 2 8580\n1 2 1 96263\n1 4 2 2156\n1 2 0 94325\n1 4 3 94328') == '357500'
    assert solve('10 10 1\n1 10 9 1') == '1'
