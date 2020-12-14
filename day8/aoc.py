from typing import Optional


class Instruction:
    def __init__(self, command, value):
        self.command: str = command
        self.value: int = value

    def __repr__(self):
        return "{}: {}".format(self.command, self.value)


class IntCode2020:
    def __init__(self, program: list[Instruction]):
        self.program: list[Instruction] = program
        self.instruction_pointer: int = 0
        self.accumulator: int = 0

    def detect_loop(self) -> bool:
        self.accumulator = 0
        self.instruction_pointer = 0
        instructions_executed = set()

        while self.instruction_pointer < len(self.program):
            if self.instruction_pointer in instructions_executed:
                return True
            else:
                instructions_executed.add(self.instruction_pointer)
            instruction = self.program[self.instruction_pointer]
            command = instruction.command
            command_value = instruction.value
            if command == "acc":
                self.add(command_value)
                self.instruction_pointer += 1
            elif command == "nop":
                self.instruction_pointer += 1
            elif command == "jmp":
                self.jump(command_value)
            else:
                raise ValueError("Operation not supported!")
        return False

    def add(self, amount: int):
        self.accumulator += amount

    def jump(self, amount: int):
        self.instruction_pointer += amount


if __name__ == "__main__":
    instructions: list[Instruction] = []
    with open("input.txt") as input_file:
        for line in input_file:
            op, num = line.split(" ")
            instructions.append(Instruction(op, int(num)))
    int_code = IntCode2020(instructions)
    print("Accumulator before loop:", int_code.detect_loop())

    for i in range(len(instructions)):
        if instructions[i].command == "nop":
            instructions[i].command = "jmp"
            int_code = IntCode2020(instructions)
            if not int_code.detect_loop():
                print("Accumulator without loop:", int_code.accumulator)
                break
            else:
                instructions[i].command = "nop"
        elif instructions[i].command == "jmp":
            instructions[i].command = "nop"
            int_code = IntCode2020(instructions)
            if not int_code.detect_loop():
                print("Accumulator without loop:", int_code.accumulator)
                break
            else:
                instructions[i].command = "jmp"
