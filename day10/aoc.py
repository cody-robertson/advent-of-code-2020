class JoltAdapter:
    def __init__(self, adapter_array: list[int]):
        self.adapters = sorted(adapter_array)
        self.adapters.append(self.adapters[-1] + 3)

    def jolt_differential(self):
        differentials = {0: 0, 1: 0, 2: 0, 3: 0}
        previous = 0  # account for differential from outlet
        for adapter in self.adapters:
            differentials[adapter - previous] += 1
            previous = adapter
        differentials[3] += 1  # account for differential to device
        return differentials

    def valid_configurations(self):
        memo: dict[int, int] = {0: 1}
        for adapter in self.adapters:
            memo[adapter] = 0
        for adapter_first in [0] + self.adapters:
            for adapter_second in self.adapters:
                if 1 <= adapter_second - adapter_first <= 3:
                    memo[adapter_second] += memo[adapter_first]
        return memo[self.adapters[-1]]

        # for i in range(max(self.adapters)+1):
        #     memo[i] = 0
        # for i in range(len(self.adapters)):
        #     for adapter in self.adapters:
        #         for adapter_2 in self.adapters:
        #             difference = adapter - adapter_2
        #             if 1 <= difference <= 3:
        #                 memo[adapter].add(adapter_2)
        #                 memo[adapter].union(memo[adapter_2])

    # def add_configurations_to_last(self, memo: dict[int, set[int]]):
    #     reachable: list[int] = list(memo[max(memo.keys())])
    #     total = len(reachable)
    #     while len(reachable) > 0:
    #         next_reachable = []
    #         for i in range(len(reachable)):
    #             current = reachable.pop()
    #             next_reachable += list(memo[current])
    #         total += total * len(next_reachable)
    #         reachable.extend(next_reachable)


if __name__ == "__main__":
    adapters: list[int]
    with open("input.txt") as input_file:
        adapters = list(map(int, input_file.readlines()))
    program = JoltAdapter(adapters)
    results = program.jolt_differential()
    print(results[1] * results[3])
    print(program.valid_configurations())
