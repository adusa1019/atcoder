import pytest
from B import solve


def test_solve():
    assert solve('4\nhoge\nenglish\nhoge\nenigma') == 'No'
    assert solve('9\nbasic\nc\ncpp\nphp\npython\nnadesico\nocaml\nlua\nassembly') == 'Yes'
    assert solve('8\na\naa\naaa\naaaa\naaaaa\naaaaaa\naaa\naaaaaaa') == 'No'
    assert solve('3\nabc\narc\nagc') == 'No'
