class ActualValue:
    digit: int
    value: str

    def __init__(self, digit: int, value: str) -> None:
        self.digit = digit
        self.value = value

    def __repr__(self) -> str:
        return 'digit: {}; value: {}; length: {}'.format(self.digit, self.value.rjust(7, ' '), self.length())

    def length(self) -> int:
        return len(self.value)

actual_values: list[ActualValue] = [ActualValue(0, 'abcefg'), ActualValue(1, 'cf'), ActualValue(2, 'acdeg'), ActualValue(3, 'acdfg'), ActualValue(4, 'bcdf'), ActualValue(5, 'abdfg'), ActualValue(6, 'abdefg'), ActualValue(7, 'acf'), ActualValue(8, 'abcdefg'), ActualValue(9, 'abcdfg')]

# [print(actual_value) for actual_value in actual_values]

unique_actual_value_lengths: list[int] = [actual_value.length() for actual_value in actual_values if actual_value.digit in [1,4,7,8]]
# print(unique_actual_value_lengths)

with open('day_8_input.txt') as file:
    inputs = file.readlines()

# print('inputs: {}'.format(inputs))

entries = [input.strip().split(' | ') for input in inputs]
# print('entries: {}'.format(entries))

unique_actual_value_lengths_appear_total = 0

for entry in entries:
    signal_patterns = entry[0].split()
    output_values = entry[1].split()
    unique_actual_value_lengths_appear = len([len(output_value) for output_value in output_values if len(output_value) in unique_actual_value_lengths])
    print('signal_patterns: {}; output_values: {}; unique_length_entries: {}'.format(signal_patterns, output_values, unique_actual_value_lengths_appear))
    unique_actual_value_lengths_appear_total += unique_actual_value_lengths_appear

print('unique_actual_value_lengths_appear_total: {}'.format(unique_actual_value_lengths_appear_total))