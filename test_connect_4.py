"""
Testing Connect_4.py
"""
import sys

import pytest
import unittest

from Connect_4 import find_winner


class TestSuite(unittest.TestCase):
    def test_no_sequence_blue_in_mid(self):
        board = [
            ['None', 'None', 'None', 'R', 'B', 'R', 'R'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ]
        colors = ['R', 'B']
        res = find_winner(board, colors)

        assert not res

    def test_sequence_red_row(self):
        board = [
            ['None', 'None', 'None', 'R', 'R', 'R', 'R'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ]
        colors = ['R', 'B']
        res = find_winner(board, colors)

        assert res

    def test_sequence_red_col(self):
        board = [
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ]
        colors = ['R', 'B']
        res = find_winner(board, colors)

        assert res

    def test_sequence_red_blue_col(self):
        board = [
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['B', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['R', 'None', 'None', 'None', 'None', 'None', 'None'],
            ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ]
        colors = ['R', 'B']
        res = find_winner(board, colors)

        assert not res


def main():
    """
    main for tests
    """
    errcode = pytest.main()
    sys.exit(errcode)


if __name__ == "__main__":
    main()
