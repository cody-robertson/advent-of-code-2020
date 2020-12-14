import string

if __name__ == "__main__":
    # Part 1
    total = 0
    with open("input.txt") as input_file:
        group_answers = set()
        for line in input_file:
            line = line.strip()
            if line == "":
                total += len(group_answers)
                group_answers = set()
            else:
                for answer in line:
                    group_answers.add(answer)
        total += len(group_answers)
    print("Anyone said yes:", total)

    # Part 2
    total = 0
    with open("input.txt") as input_file:
        group_answers = {}
        group_size = 0
        for line in input_file:
            line = line.strip()
            if line == "":
                for char in string.ascii_lowercase:
                    answer = group_answers.get(char)
                    if answer is not None and answer == group_size:
                        total += 1
                group_answers = {}
                group_size = 0
            else:
                group_size += 1
                for answer in line:
                    if answer in group_answers.keys():
                        group_answers[answer] += 1
                    else:
                        group_answers[answer] = 1
        for char in string.ascii_lowercase:
            answer = group_answers.get(char)
            if answer is not None and answer == group_size:
                total += 1
    print("Everyone said yes:", total)
