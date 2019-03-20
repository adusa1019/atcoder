import pytest
from C import solve


def test_solve():
    assert solve('3 3\n.#.\n###\n.#.') == 'Yes'
    assert solve('5 5\n#.#.#\n.#.#.\n#.#.#\n.#.#.\n#.#.#') == 'No'
    assert solve(
        '11 11\n...#####...\n.##.....##.\n#..##.##..#\n#..##.##..#\n#.........#\n#...###...#\n.#########.\n.#.#.#.#.#.\n##.#.#.#.##\n..##.#.##..\n.##..#..##.'
    ) == 'Yes'
