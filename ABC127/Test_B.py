import pytest
from B import solve


def test_solve():
    assert solve('2 10 20') == '30\n50\n90\n170\n330\n650\n1290\n2570\n5130\n10250'
    assert solve('4 40 60') == '200\n760\n3000\n11960\n47800\n191160\n764600\n3058360\n12233400\n48933560'
