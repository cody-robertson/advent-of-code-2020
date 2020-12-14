from enum import Enum


class Seat(Enum):
    Empty = 'L'
    Floor = '.'
    Occupied = '#'


class SeatingSystem:
    def __init__(self, seating: list[list[Seat]]):
        self.seating: list[list[Seat]] = seating
        self.original_state = self.copy_seating_list()
        self.search_space: list[tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def stabilize_seating(self):
        self.seating = self.original_state
        next_state = self.get_next_state()
        while not self.is_equivalent_to_current_seating(next_state):
            self.seating = next_state[:]
            next_state = self.get_next_state()

    def stabilize_seating_more_tolerant(self):
        self.seating = self.original_state
        next_state = self.get_next_state_more_tolerant()
        while not self.is_equivalent_to_current_seating(next_state):
            self.seating = next_state[:]
            next_state = self.get_next_state_more_tolerant()

    def get_next_state(self) -> list[list[Seat]]:
        next_state = self.copy_seating_list()
        for i in range(len(self.seating)):
            for j in range(len(self.seating[i])):
                occupied = self.number_occupied_adjacent_to_seat(i, j)
                if self.seating[i][j] == Seat.Empty and occupied == 0:
                    next_state[i][j] = Seat.Occupied
                elif self.seating[i][j] == Seat.Occupied and occupied >= 4:
                    next_state[i][j] = Seat.Empty
        return next_state

    def get_next_state_more_tolerant(self) -> list[list[Seat]]:
        next_state = self.copy_seating_list()
        for i in range(len(self.seating)):
            for j in range(len(self.seating[i])):
                occupied = self.number_occupied_adjacent_to_seat_keep_looking(i, j)
                if self.seating[i][j] == Seat.Empty and occupied == 0:
                    next_state[i][j] = Seat.Occupied
                elif self.seating[i][j] == Seat.Occupied and occupied >= 5:
                    next_state[i][j] = Seat.Empty
        return next_state

    def number_occupied_adjacent_to_seat(self, row: int, column: int):
        return len(self.occupied_adjacent_to_seat(row, column))

    def number_occupied_adjacent_to_seat_keep_looking(self, row: int, column: int):
        return len(self.occupied_adjacent_to_seat_keep_looking(row, column))

    def occupied_adjacent_to_seat(self, row: int, column: int) -> list[tuple[int, int]]:
        return [(r, c) for r, c in self.search_space if self.is_occupied(row, column, r, c, keep_looking=False)]

    def occupied_adjacent_to_seat_keep_looking(self, row: int, column: int) -> list[tuple[int, int]]:
        return [(r, c) for r, c in self.search_space if self.is_occupied(row, column, r, c, keep_looking=True)]

    def is_occupied(self, row: int, column: int, row_add: int, column_add: int, keep_looking: bool = False) -> bool:
        if 0 <= row+row_add < len(self.seating):
            if 0 <= column+column_add < len(self.seating[row]):
                seat = self.seating[row+row_add][column+column_add]
                if not keep_looking or seat != Seat.Floor:
                    return seat == Seat.Occupied
                else:
                    return self.is_occupied(row+row_add, column+column_add, row_add, column_add, keep_looking)
        return False

    def copy_seating_list(self) -> list[list[Seat]]:
        copy = []
        for row in self.seating:
            copy.append(row[:])
        return copy

    def is_equivalent_to_current_seating(self, new_seating: list[list[Seat]]):
        if len(self.seating) != len(new_seating):
            return False
        for i in range(len(self.seating)):
            if len(self.seating[i]) != len(new_seating[i]):
                return False
            for j in range(len(self.seating[i])):
                if self.seating[i][j] != new_seating[i][j]:
                    return False
        return True

    def count_seat_types(self):
        result = {Seat.Occupied: 0, Seat.Empty: 0, Seat.Floor: 0}
        for row in self.seating:
            for seat in row:
                result[seat] += 1
        return result


if __name__ == "__main__":
    ferry_seating: list[list[Seat]] = []
    with open("input.txt") as input_file:
        for line in input_file:
            row_input = []
            for character in list(line.strip()):
                if character == 'L':
                    row_input.append(Seat.Empty)
                elif character == '.':
                    row_input.append(Seat.Floor)
                elif character == '#':
                    row_input.append(Seat.Occupied)
                else:
                    raise ValueError("Invalid character in input: '{}'".format(character))
            ferry_seating.append(row_input)
    system = SeatingSystem(ferry_seating)
    system.stabilize_seating()
    print(system.count_seat_types())
    system.stabilize_seating_more_tolerant()
    print(system.count_seat_types())
