import unittest
from day1.aoc import NumSum


class Day1Test(unittest.TestCase):
    def test_two_sum_sample_output(self):
        program = NumSum([1721, 979, 366, 299, 675, 1456])
        self.assertEqual(program.two_sum(2020), (1721, 299))


if __name__ == '__main__':
    unittest.main()
