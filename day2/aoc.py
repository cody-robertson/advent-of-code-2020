class PasswordValidator:
    @staticmethod
    def is_valid_password_first_policy(rule: tuple[chr, tuple[int, int]], password_string: str):
        char_match: chr = rule[0]
        char_range: range = range(rule[1][0], rule[1][1] + 1)
        return len([x for x in password_string if x == char_match]) in char_range

    @staticmethod
    def is_valid_password_second_policy(rule: tuple[chr, tuple[int, int]], password_string: str):
        first_location = rule[1][0] - 1
        second_location = rule[1][1] - 1
        char_match = rule[0]
        return (password_string[first_location] == char_match and password_string[second_location] != char_match) \
               or (password_string[first_location] != char_match and password_string[second_location] == char_match)


if __name__ == "__main__":
    input_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            line = line.strip().split(' ')
            rule_split = list(map(int, line[0].split('-')))[0:2]
            rule_char: chr = line[1][0]
            password_rule = (rule_char, (rule_split[0], rule_split[1]))
            password: str = line[2]
            input_list.append((password_rule, password))
    validator = PasswordValidator()
    valid_count_first_policy = len([x for x in input_list if validator.is_valid_password_first_policy(x[0], x[1])])
    valid_count_second_policy = len([x for x in input_list if validator.is_valid_password_second_policy(x[0], x[1])])
    print("First policy:", valid_count_first_policy)
    print("Second policy:", valid_count_second_policy)
