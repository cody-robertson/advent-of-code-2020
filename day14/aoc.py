class BitMask:
    def __init__(self, mask: str):
        self.mask = mask

    @staticmethod
    def set_bit(value: int, position: int):
        return value | (1 << position)

    @staticmethod
    def clear_bit(value: int, position: int):
        return value & ~(1 << position)

    def apply_mask(self, value: int) -> int:
        return_value = value
        for i in range(len(self.mask)):
            current = self.mask[i]
            if current == "0":
                return_value = self.clear_bit(return_value, len(self.mask)-1-i)
            elif current == "1":
                return_value = self.set_bit(return_value, len(self.mask)-1-i)
        print("{:36b}".format(value))
        print(self.mask)
        print("{:36b}".format(return_value))
        print()
        return return_value


if __name__ == "__main__":
    program: BitMask
    memory = {}
    with open("input.txt") as input_file:
        for line in input_file:
            first, second = line.strip().split(" = ")
            if first == "mask":
                program = BitMask(second)
            else:
                command_address = int(first[first.find('[')+1:first.find(']')])
                command_value = program.apply_mask(int(second))
                memory[command_address] = command_value
    print(memory)
    print("Sum of values:", sum(memory.values()))
