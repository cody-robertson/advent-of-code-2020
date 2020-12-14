import unittest
from day12.aoc import NavigationComputer, Position


class NavigationComputerTests(unittest.TestCase):
    def setUp(self):
        self.navigationComputer = NavigationComputer([])
        self.navigationComputer.ship_position = Position(0, 0, 0)

    def test_angle_to_waypoint(self):
        test_cases = [(Position(0, 1, 0), 0), (Position(1, 1, 0), 45), (Position(-1, 1, 0), 270+45)]
        for position, output in test_cases:
            with self.subTest(position=position):
                self.navigationComputer.waypoint_position = position
                angle = self.navigationComputer.get_angle_to_waypoint()
                self.assertEqual(angle, output)

    def test_moves_to_correct_waypoint_position(self):
        self.navigationComputer.follow_instruction('F', 10, use_waypoint=True)
        self.assertEqual(self.navigationComputer.ship_position.x, 100)
        self.assertEqual(self.navigationComputer.ship_position.y, 10)


if __name__ == '__main__':
    unittest.main()
