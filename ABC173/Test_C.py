import pytest
from C import solve


def test_solve():
    assert solve('2 3 2\n..#\n###') == '5'
    assert solve('2 3 4\n..#\n###') == '1'
    assert solve('2 2 3\n##\n##') == '0'
    assert solve('6 6 8\n..##..\n.#..#.\n#....#\n######\n#....#\n#....#') == '208'
