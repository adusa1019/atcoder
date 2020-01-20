import pytest
from D import solve


def test_solve():
    assert solve('3 3\n...\n...\n...') == '4'
    assert solve('3 5\n...#.\n.#.#.\n.#...') == '10'
