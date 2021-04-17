import unittest
from day15.aoc import CountingGame


class CountingGameTests(unittest.TestCase):
    def test_part_1_scenarios(self):
        scenarios = [
            ([0, 3, 6], 436),
            ([1, 3, 2], 1),
            ([2, 1, 3], 10),
            ([1, 2, 3], 27),
            ([2, 3, 1], 78),
            ([3, 2, 1], 438),
            ([3, 1, 2], 1836)
        ]
        for starting_numbers, expected_output in scenarios:
            with self.subTest(starting_numbers=starting_numbers):
                game = CountingGame(starting_numbers)
                self.assertEqual(game.simulate_until_n(2020), expected_output)

    def test_part_2_scenarios(self):
        scenarios = [
            ([0, 3, 6], 175594),
            ([1, 3, 2], 2578),
            ([2, 1, 3], 3544142),
            ([1, 2, 3], 261214),
            ([2, 3, 1], 6895259),
            ([3, 2, 1], 18),
            ([3, 1, 2], 362)
        ]
        for starting_numbers, expected_output in scenarios:
            with self.subTest(starting_numbers=starting_numbers):
                game = CountingGame(starting_numbers)
                self.assertEqual(game.simulate_until_n(30000000), expected_output)


if __name__ == '__main__':
    unittest.main()
