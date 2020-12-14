class BinaryBoarding:
    @staticmethod
    def get_set_number(location_string: str) -> int:
        if len(location_string) != 10:
            raise ValueError("Input is not the correct length!")
        start = 0
        end = 127
        for char in location_string[:7]:
            if char == "F":
                end = ((end - start) // 2) + start
            elif char == "B":
                start = ((end - start) // 2) + 1 + start
        if start != end:
            raise ArithmeticError("Start and end are not the same!  Start: {}, End: {}".format(start, end))
        row = start
        start = 0
        end = 7
        for char in location_string[7:]:
            if char == "L":
                end = ((end - start) // 2) + start
            elif char == "R":
                start = ((end - start) // 2) + 1 + start
        if start != end:
            raise ArithmeticError("Start and end are not the same!  Start: {}, End: {}".format(start, end))
        column = start
        return BinaryBoarding.convert_to_seat_number(row, column)

    @staticmethod
    def convert_to_seat_number(row: int, column: int) -> int:
        return (row * 8) + column


if __name__ == "__main__":
    filled_seats = []
    with open("input.txt") as input_file:
        for line in input_file:
            filled_seats.append(BinaryBoarding.get_set_number(line.strip()))  # [BinaryBoarding.get_set_number(line.strip()) for line in input_file]
    print("Max Seat", max(filled_seats))
    missing_seat = list(set(range(min(filled_seats), max(filled_seats)+1)) - set(filled_seats))[0]
    print("Seat found:", missing_seat)
