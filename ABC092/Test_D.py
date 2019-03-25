import pytest
from D import solve


def test_solve():
    assert solve('2 3') == '3 3\n##.\n..#\n#.#'
    assert solve('7 8') == '3 5\n#.#.#\n.#.#.\n#.#.#'
    assert solve('1 1') == '4 2\n..\n#.\n##\n##'
    assert solve('3 14') == '8 18\n..................\n..................\n....##.......####.\n....#.#.....#.....\n...#...#....#.....\n..#.###.#...#.....\n.#.......#..#.....\n#.........#..####.'
