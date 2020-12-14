from typing import Optional


class XmasDecoder:
    def __init__(self, message_with_preamble: list[int], preamble_length: int):
        self.preamble_length = preamble_length
        self.message = message_with_preamble

    def is_valid_number(self, message_index: int) -> bool:
        if message_index < self.preamble_length:
            return True
        preamble = self.message[message_index-self.preamble_length:message_index]
        preamble_set = set(preamble)
        number = self.message[message_index]
        max_preamble = max(preamble)
        min_preamble = min(preamble)
        if number - max_preamble > max_preamble or number - min_preamble < min_preamble:
            return False
        for first in preamble:
            second = number - first
            if second != first and second in preamble_set:
                return True
        return False

    def get_invalid_numbers_in_message(self) -> list[int]:
        for i in range(len(self.message)):
            if not self.is_valid_number(i):
                yield self.message[i]

    def contiguous_sum(self, target_sum: int) -> Optional[tuple[int, int]]:
        for i in range(len(self.message)):
            for j in range(i, len(self.message)):
                subset = self.message[i:j]
                if sum(subset) == target_sum:
                    return min(subset), max(subset)


if __name__ == "__main__":
    preamble_size = 25  # Hard-coded for each example for now
    input_list: list[int]
    with open("input.txt") as input_file:
        input_list = list(map(int, input_file.readlines()))
    decoder = XmasDecoder(input_list, preamble_size)
    invalid_number = list(decoder.get_invalid_numbers_in_message())[0]
    print(invalid_number)
    result = decoder.contiguous_sum(invalid_number)
    print(result[0], result[1])
    print(result[0] + result[1])
