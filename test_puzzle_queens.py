import unittest
import sys
sys.path.append('app')
from puzzle_queens import puzzle_queens

class TestPuzzleQueens(unittest.TestCase):
    def test_soluciones(self):
        self.assertAlmostEqual(len(puzzle_queens(1)),1)
        self.assertAlmostEqual(len(puzzle_queens(2)),0)
        self.assertAlmostEqual(len(puzzle_queens(3)),0)
        self.assertAlmostEqual(len(puzzle_queens(4)),2)
        self.assertAlmostEqual(len(puzzle_queens(5)),10)
        self.assertAlmostEqual(len(puzzle_queens(6)),4)
        self.assertAlmostEqual(len(puzzle_queens(7)),40)
        self.assertAlmostEqual(len(puzzle_queens(8)),92)
        self.assertAlmostEqual(len(puzzle_queens(9)),352)
        self.assertAlmostEqual(len(puzzle_queens(10)),724)