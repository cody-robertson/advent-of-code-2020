class CountingGame:
    def __init__(self, starting_numbers):
        self.starting_numbers = starting_numbers

    def get_nth_number(self, n: int):
        pass

    def simulate_until_n(self, n: int):
        previous_number = self.starting_numbers[-1]
        spoken_set = {}
        for i in range(len(self.starting_numbers)-1):
            spoken_set[self.starting_numbers[i]] = i+1
        turn_count = len(self.starting_numbers)
        while n > turn_count:
            next_number: int
            if previous_number not in spoken_set:
                next_number = 0
            else:
                next_number = turn_count - spoken_set[previous_number]
            spoken_set[previous_number] = turn_count
            previous_number = next_number
            turn_count += 1
        return previous_number


if __name__ == "__main__":
    input_numbers: list[int]
    with open("input.txt") as input_file:
        input_numbers = list(map(int, input_file.readline().strip().split(",")))
    game = CountingGame(input_numbers)
    print(game.simulate_until_n(30000000))
