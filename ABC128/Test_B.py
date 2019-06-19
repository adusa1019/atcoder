import pytest
from B import solve


def test_solve():
    assert solve('6\nkhabarovsk 20\nmoscow 10\nkazan 50\nkazan 35\nmoscow 60\nkhabarovsk 40') == '3\n4\n6\n1\n5\n2'
    assert solve('10\nyakutsk 10\nyakutsk 20\nyakutsk 30\nyakutsk 40\nyakutsk 50\nyakutsk 60\nyakutsk 70\nyakutsk 80\nyakutsk 90\nyakutsk 100') == '10\n9\n8\n7\n6\n5\n4\n3\n2\n1'
