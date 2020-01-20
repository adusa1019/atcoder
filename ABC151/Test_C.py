import pytest
from C import solve


def test_solve():
    assert solve('2 5\n1 WA\n1 AC\n2 WA\n2 AC\n2 WA') == '2 2'
    assert solve('100000 3\n7777 AC\n7777 AC\n7777 AC') == '1 0'
    assert solve('6 0') == '0 0'
