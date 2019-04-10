import pytest
from D import solve


def test_solve():
    assert solve('4 5\n1 2\n3 4\n1 3\n2 3\n1 4') == '0\n0\n4\n5\n6'
    assert solve('6 5\n2 3\n1 2\n5 6\n3 4\n4 5') == '8\n9\n12\n14\n15'
    assert solve('2 1\n1 2') == '1'
    assert solve('10000 5000\n' +
                 '\n'.join(["{} {}".format(2 * i, 2 * i + 1) for i in range(5000)])) == "\n".join(
                     [str(49990001 + i) for i in range(5000)])
