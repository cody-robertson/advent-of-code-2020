class NumSum:
    def __init__(self, num_array: list[int]):
        self.num_array = num_array
        self.two_sums = {}
        self.three_sums = {}
        self.sum_values()

    def sum_values(self):
        self.two_sums = {}
        self.three_sums = {}
        for i in range(len(self.num_array) - 1):
            for j in range(i + 1, len(self.num_array)):
                self.two_sums[self.num_array[i] + self.num_array[j]] = (self.num_array[i], self.num_array[j])
        for i in range(len(self.num_array) - 2):
            for j in range(i + 1, len(self.num_array) - 1):
                for k in range(j + 1, len(self.num_array)):
                    self.three_sums[self.num_array[i] + self.num_array[j] + self.num_array[k]] = (self.num_array[i], self.num_array[j], self.num_array[k])

    def two_sum(self, num):
        return self.two_sums.get(num)

    def three_sum(self, num):
        return self.three_sums.get(num)


if __name__ == "__main__":
    num_list = []
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            num_list.append(int(line.strip()))
    # program = NumSum(num_list)
    # items = program.two_sum(2020)
    # print(items[0] * items[1])
    # items = program.three_sum(2020)
    # print(items[0] * items[1] * items[2])

    print([(x, y, z) for x, y, z in [[x for x in num_list], [y for y in num_list], [z for z in num_list]] if x + y + z == 2020])
