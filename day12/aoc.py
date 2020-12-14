from math import radians, sin, cos


class Position:
    def __init__(self, x, y, theta):
        self.x: float = x
        self.y: float = y
        self.theta: float = theta

    def __repr__(self):
        return "x:{}, y:{}, theta:{}".format(self.x, self.y, self.theta)

    def __str__(self):
        return "x:{}, y:{}, theta:{}".format(self.x, self.y, self.theta)

    def manhattan(self):
        return abs(self.x) + abs(self.y)


class NavigationComputer:
    def __init__(self, instructions: list[tuple[chr, int]]):
        self.instructions = instructions
        self.ship_position = Position(0, 0, 90)
        self.waypoint_offset = Position(10, 1, 0)

    def distance_after_instructions(self, use_waypoint=False):
        self.ship_position = Position(0, 0, 90)
        self.waypoint_offset = Position(10, 1, 0)
        for instruction, amount in self.instructions:
            self.follow_instruction(instruction, amount, use_waypoint)
        return self.ship_position.manhattan()

    def follow_instruction(self, instruction: chr, amount: int, use_waypoint=False):
        if instruction == 'N':
            self.change_position(delta_y=amount, use_waypoint=use_waypoint)
        elif instruction == 'S':
            self.change_position(delta_y=-amount, use_waypoint=use_waypoint)
        elif instruction == 'E':
            self.change_position(delta_x=amount, use_waypoint=use_waypoint)
        elif instruction == 'W':
            self.change_position(delta_x=-amount, use_waypoint=use_waypoint)
        elif instruction == 'L':
            self.change_position(delta_theta=-amount, use_waypoint=use_waypoint)
        elif instruction == 'R':
            self.change_position(delta_theta=amount, use_waypoint=use_waypoint)
        elif instruction == 'F':
            self.follow_forward_instruction(amount, use_waypoint)
        else:
            raise ValueError("Unknown instruction received: {}".format(instruction))

    def follow_forward_instruction(self, amount: int, use_waypoint=False):
        angle: float
        if use_waypoint:
            self.move_ship_to_waypoint(amount)
        else:
            angle = self.ship_position.theta
            self.move_ship_at_angle(amount, angle)

    def move_ship_at_angle(self, amount: int, angle: float):
        if angle == 0:
            self.change_ship_position(delta_y=amount)
        elif angle == 90:
            self.change_ship_position(delta_x=amount)
        elif angle == 180:
            self.change_ship_position(delta_y=-amount)
        elif angle == 270:
            self.change_ship_position(delta_x=-amount)
        else:
            x_change = sin(radians(angle % 90)) * amount
            y_change = cos(radians(angle % 90)) * amount
            if 0 < angle < 90:
                self.change_ship_position(x_change, y_change)
            elif 90 < angle < 180:
                self.change_ship_position(x_change, -y_change)
            elif 180 < angle < 270:
                self.change_ship_position(-x_change, -y_change)
            elif 270 < angle < 360:
                self.change_ship_position(-x_change, y_change)

    def move_ship_to_waypoint(self, number_of_times: int):
        self.change_ship_position(self.waypoint_offset.x * number_of_times, self.waypoint_offset.y * number_of_times)

    def change_position(self, delta_x=0, delta_y=0, delta_theta=0, use_waypoint=False):
        if use_waypoint:
            self.move_waypoint(delta_x, delta_y, delta_theta)
        else:
            self.change_ship_position(delta_x, delta_y, delta_theta)

    def change_ship_position(self, delta_x: float = 0, delta_y: float = 0, delta_theta: float = 0):
        self.ship_position.x += delta_x
        self.ship_position.y += delta_y
        self.ship_position.theta = (self.ship_position.theta + delta_theta) % 360

    def move_waypoint(self, delta_x: float = 0, delta_y: float = 0, delta_r: float = 0):
        self.waypoint_offset.x += delta_x
        self.waypoint_offset.y += delta_y
        # calculate new position based on rotation around point
        x1 = self.waypoint_offset.x
        y1 = self.waypoint_offset.y
        # apparently, these equations expect your rotations to be counter-clockwise
        # because of this, we need to flip the sign of our angle
        rotation_angle = delta_r * -1
        self.waypoint_offset.x = round((x1 * cos(radians(rotation_angle))) - (y1 * sin(radians(rotation_angle))))
        self.waypoint_offset.y = round((y1 * cos(radians(rotation_angle))) + (x1 * sin(radians(rotation_angle))))


if __name__ == "__main__":
    input_list: list[tuple[chr, int]] = []
    with open("input.txt") as input_file:
        for line in input_file:
            character: chr = line[0]
            integer: int = int(line[1:])
            input_list.append((character, integer))
    computer = NavigationComputer(input_list)
    print(computer.distance_after_instructions(use_waypoint=False))
    print(computer.distance_after_instructions(use_waypoint=True))
