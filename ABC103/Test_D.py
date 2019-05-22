import pytest
from D import solve


def test_solve():
    # assert solve('5 2\n1 4\n2 5') == '1'
    # assert solve('9 5\n1 8\n2 7\n3 5\n4 6\n7 9') == '2'
    # assert solve('5 10\n1 2\n1 3\n1 4\n1 5\n2 3\n2 4\n2 5\n3 4\n3 5\n4 5') == '4'
    assert solve('5 99999\n' + '\n'.join(["{} 100000".format(i + 1) for i in range(99999)])) == '1'
