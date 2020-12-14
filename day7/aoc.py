class ShinyGold:
    def __init__(self, bag_mappings: dict[str, dict[str, int]]):
        self.bag_mappings = bag_mappings
        self.bags_containing_shiny_gold = set()
        self.bags_not_containing_shiny_gold = set()

    def find_bags_that_contain_shiny_gold(self) -> list[str]:
        if len(self.bags_containing_shiny_gold) > 0:
            return list(self.bags_containing_shiny_gold)
        else:
            for bag_name in self.bag_mappings.keys():
                self.dfs(bag_name)
            return list(self.bags_containing_shiny_gold)

    def dfs(self, bag_name: str) -> bool:
        if bag_name in self.bags_containing_shiny_gold or bag_name == "shiny gold":
            return True
        elif bag_name in self.bags_not_containing_shiny_gold:
            return False
        elif len(self.bag_mappings[bag_name]) == 0:
            self.bags_not_containing_shiny_gold.add(bag_name)
            return False
        else:
            for name in self.bag_mappings[bag_name].keys():
                if self.dfs(name):
                    self.bags_containing_shiny_gold.add(bag_name)
                    return True
            self.bags_not_containing_shiny_gold.add(bag_name)
            return False

    def find_total_bags_in_bag(self, bag_name: str) -> int:
        return self.bfs(bag_name)

    def bfs(self, bag_name: str) -> int:
        current_bags: dict[str, int] = {bag_name: 1}
        next_bags: dict[str, int] = {}
        total = 0
        while len(current_bags) > 0:
            for current_bag_name, current_bag_count in current_bags.items():
                bags_in_current_bag = self.bags_in_bag(current_bag_name)
                total += bags_in_current_bag * current_bag_count
                if bags_in_current_bag > 0:
                    for new_bag_name, new_bag_count in self.bag_mappings[current_bag_name].items():
                        if new_bag_name in next_bags:
                            next_bags[new_bag_name] += new_bag_count * current_bag_count
                        else:
                            next_bags[new_bag_name] = new_bag_count * current_bag_count
            current_bags = next_bags
            next_bags = {}
        return total

    def bags_in_bag(self, bag_name) -> int:
        return sum(self.bag_mappings[bag_name].values())


class InputFormatter:
    @staticmethod
    def format_file_input(file_name: str) -> dict[str, dict[str, int]]:
        input_mappings: dict[str, dict[str, int]] = {}
        with open(file_name) as input_file:
            for line in input_file:
                source_mapping, dest_string = line.strip().split(" bags contain ")
                destination_strings = dest_string.split(", ")
                destination_mappings: dict[str, int] = {}
                for i in range(len(destination_strings)):
                    if "no other bags" in destination_strings[i]:
                        pass
                    elif destination_strings[i][-1] == ".":
                        temp_split = destination_strings[i][:-5].strip().split(" ")
                        count_mapping = int(temp_split[0])
                        name_mapping = " ".join(temp_split[1:])
                        destination_mappings[name_mapping] = count_mapping
                    else:
                        temp_split = destination_strings[i][:-4].strip().split(" ")
                        count_mapping = int(temp_split[0])
                        name_mapping = " ".join(temp_split[1:])
                        destination_mappings[name_mapping] = count_mapping
                input_mappings[source_mapping] = destination_mappings
        return input_mappings


if __name__ == "__main__":
    mappings = InputFormatter.format_file_input("input.txt")
    program = ShinyGold(mappings)
    print("Bags containing shiny gold:", len(program.find_bags_that_contain_shiny_gold()))
    print("Total bags in a shiny gold:", program.find_total_bags_in_bag("shiny gold"))
