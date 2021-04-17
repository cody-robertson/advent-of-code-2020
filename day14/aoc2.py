class BitMask:
    def __init__(self, mask: str):
        self.mask = mask

    @staticmethod
    def set_bit(value: int, position: int):
        return value | (1 << position)

    @staticmethod
    def clear_bit(value: int, position: int):
        return value & ~(1 << position)

    def apply_mask(self, value: int) -> list[int]:
        return_values = [value]
        for i in range(len(self.mask)):
            current = self.mask[i]
            next_values = []
            for j in range(len(return_values)):
                if current == "X":
                    next_values.append(self.set_bit(return_values[j], len(self.mask)-1-i))
                    next_values.append(self.clear_bit(return_values[j], len(self.mask) - 1 - i))
                elif current == "1":
                    next_values.append(self.set_bit(return_values[j], len(self.mask)-1-i))
                else:
                    next_values.append(return_values[j])
            return_values = next_values
        return return_values


if __name__ == "__main__":
    program: BitMask
    memory = {}
    with open("input.txt") as input_file:
        for line in input_file:
            first, second = line.strip().split(" = ")
            if first == "mask":
                program = BitMask(second)
            else:
                raw_address = int(first[first.find('[')+1:first.find(']')])
                command_value = int(second)
                command_addresses: list[int] = program.apply_mask(raw_address)
                for address in command_addresses:
                    memory[address] = command_value
    print(memory)
    print("Sum of values:", sum(memory.values()))
