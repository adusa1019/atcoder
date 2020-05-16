import pytest
from D import solve


def test_solve():
    assert solve('4\nRRGB') == '1'
    assert solve('39\nRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB') == '1800'
    assert solve('4000\n' + "R" * 1300 + "G" * 1300 + "B" * 1400) == '2365092500'
