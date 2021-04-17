class Rule:
    def __init__(self, name: str, valid_ranges: list[range]):
        self.name: str = name
        self.valid_ranges: list[range] = valid_ranges

    def is_valid_value(self, value: int) -> bool:
        for valid_range in self.valid_ranges:
            if value in valid_range:
                return True
        return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class TicketValidator:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def get_invalid_fields(self, ticket: list[int]) -> list[int]:
        invalid_fields = []
        for field in ticket:
            is_valid: bool = False
            for rule in self.rules:
                if not is_valid and rule.is_valid_value(field):
                    is_valid = True
            if not is_valid:
                invalid_fields.append(field)
        return invalid_fields

    def get_valid_rules_for_field(self, tickets: list[list[int]], field_index: int) -> list[str]:
        valid_rules = self.rules[:]
        for ticket in tickets:
            for rule in valid_rules[:]:
                if not rule.is_valid_value(ticket[field_index]):
                    valid_rules.remove(rule)
        return list(map(lambda y: y.name, valid_rules))

    def get_valid_rules_for_each_field(self, tickets: list[list[int]]) -> dict[str, int]:
        valid_field_rules: list[list[str]] = []
        number_of_fields = len(tickets[0])
        for i in range(number_of_fields):
            valid_field_rules.append(self.get_valid_rules_for_field(tickets, i))
        result_list = {}
        while len(result_list) < number_of_fields:
            for i in range(number_of_fields):
                if len(valid_field_rules[i]) == 1:
                    result_list[valid_field_rules[i][0]] = i
            for i in range(number_of_fields):
                for name in result_list:
                    if name in valid_field_rules[i]:
                        valid_field_rules[i].remove(name)
        return result_list


if __name__ == "__main__":
    input_rules: list[Rule] = []
    your_ticket: list[int]
    nearby_tickets: list[list[int]] = []
    section = "rules"
    with open("input.txt") as input_file:
        for line in input_file.readlines():
            if line.strip() == "your ticket:":
                section = "your ticket"
            elif line.strip() == "nearby tickets:":
                section = "nearby tickets"
            elif line.strip() != "" and section == "rules":
                input_name, input_ranges_raw = line.strip().split(": ")
                input_ranges_parsed: list[range] = []
                for input_range_raw in input_ranges_raw.split(" or "):
                    start, end = list(map(int, input_range_raw.split("-")))
                    input_ranges_parsed.append(range(start, end+1))
                input_rules.append(Rule(input_name, input_ranges_parsed))
            elif line.strip() != "":
                input_ticket_values = list(map(int, line.split(",")))
                if section == "your ticket":
                    your_ticket = input_ticket_values
                else:
                    nearby_tickets.append(input_ticket_values)
    validator = TicketValidator(input_rules)
    error_rate = 0
    for nearby_ticket in nearby_tickets:
        error_rate += sum(validator.get_invalid_fields(nearby_ticket))
    print(error_rate)
    valid_tickets = [nearby_ticket for nearby_ticket in nearby_tickets if validator.get_invalid_fields(nearby_ticket) == []]
    results = validator.get_valid_rules_for_each_field(valid_tickets)
    product = 1
    print(results)
    for key, value in results.items():
        if key.startswith("departure"):
            product *= your_ticket[value]
    print(product)
