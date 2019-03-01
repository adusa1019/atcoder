import pytest
from B import solve


def test_solve():
    assert solve('4 4\n##.#\n....\n##.#\n.#.#') == '###\n###\n.##'
    assert solve('3 3\n#..\n.#.\n..#') == '#..\n.#.\n..#'
    assert solve('4 5\n.....\n.....\n..#..\n.....') == '#'
    assert solve(
        '7 6\n......\n....#.\n.#....\n..#...\n..#...\n......\n.#..#.') == '..#\n#..\n.#.\n.#.\n#.#'
