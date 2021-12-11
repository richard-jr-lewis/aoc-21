from collections import Counter

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

def set_digit(digit: int): # requires complete knowledge of segment mappings
    pattern = set([segment_mappings[key] for key in [actual_value.value.upper() for actual_value in actual_values if actual_value.digit == digit][0]])
    signal_mappings[digit] = [signal_pattern for signal_pattern in signal_patterns if set(signal_pattern) == pattern][0]

def decode_output_values() -> int:
    actual_output_value: list[str] = []
    for output_value in output_values:
        actual_output_value.append([str(k) for k, v in signal_mappings.items() if set(v) == set(output_value)][0])

    return int(''.join(actual_output_value))

actual_values: list[ActualValue] = [ActualValue(0, 'abcefg'), ActualValue(1, 'cf'), ActualValue(2, 'acdeg'), ActualValue(3, 'acdfg'), ActualValue(4, 'bcdf'), ActualValue(5, 'abdfg'), ActualValue(6, 'abdefg'), ActualValue(7, 'acf'), ActualValue(8, 'abcdefg'), ActualValue(9, 'abcdfg')]

# [print(actual_value) for actual_value in actual_values]

with open('day_8_input.txt') as file:
    inputs = file.readlines()

# print('inputs: {}'.format(inputs))

entries = [input.strip().split(' | ') for input in inputs]
# print('entries: {}'.format(entries))

output_values_sum = 0

for entry in entries:
    signal_mappings: dict[int, str] = dict()
    segment_mappings: dict[str, str] = dict()
    signal_patterns = entry[0].split()
    output_values = entry[1].split()

    # Identify 1
    signal_mappings[1] = [signal_pattern for signal_pattern in signal_patterns if len(signal_pattern) == 2][0]
    # print('1: {}'.format(signal_mappings[1]))

    # Identify 4
    signal_mappings[4] = [signal_pattern for signal_pattern in signal_patterns if len(signal_pattern) == 4][0]
    # print('4: {}'.format(signal_mappings[4]))

    # Identify 7
    signal_mappings[7] = [signal_pattern for signal_pattern in signal_patterns if len(signal_pattern) == 3][0]
    # print('7: {}'.format(signal_mappings[7]))

    # Identify 8
    signal_mappings[8] = [signal_pattern for signal_pattern in signal_patterns if len(signal_pattern) == 7][0]
    # print('8: {}'.format(signal_mappings[8]))

    # Identify segment A
    segment_mappings['A'] = list(set(signal_mappings[7]).difference(set(signal_mappings[1])))[0]
    # print('segment_mappings: {}'.format(segment_mappings))

    # Identify possible CF
    possible_CF = list(set(signal_mappings[1]) & set(signal_mappings[7]))
    # print('possible_CF: {}'.format(possible_CF))

    # Identify possible BD
    possible_BD = list(set(signal_mappings[4]).difference(set(signal_mappings[1])))
    # print('possible_BD: {}'.format(possible_BD))

    # Work with length 6 signals
    len_6_signals = [signal_pattern for signal_pattern in signal_patterns if len(signal_pattern) == 6]
    # print('len_6_signals: {}'.format(len_6_signals))

    len_6_signals_stripped_of_known_segments = [(len_6_segment, list(((set(len_6_segment).difference(set(possible_CF)).difference(set(possible_BD)))).difference(set(segment_mappings.values())))) for len_6_segment in len_6_signals]
    # print('len_6_signals_stripped_of_known_segments: {}'.format(len_6_signals_stripped_of_known_segments))

    unknown_segments_in_len_6_signals = [list(((set(len_6_segment).difference(set(possible_CF)).difference(set(possible_BD)))).difference(set(segment_mappings.values()))) for len_6_segment in len_6_signals]
    # print('unknown_segments_in_len_6_signals: {}'.format(unknown_segments_in_len_6_signals))
    freq_of_segments = dict(Counter([item for sublist in unknown_segments_in_len_6_signals for item in sublist]).items())
    # print(freq_of_segments)
    
    # Identify segment E
    segment_mappings['E'] = [k for k, v in freq_of_segments.items() if v == 2][0]

    # Identify segment G
    segment_mappings['G'] = [k for k, v in freq_of_segments.items() if v == 3][0]

    # Identify 9
    signal_mappings[9] = [signal_pattern for signal_pattern, unknown_segments in len_6_signals_stripped_of_known_segments if len(unknown_segments) == 1 and unknown_segments[0] == segment_mappings['G']][0]
    # print('9: {}'.format(signal_mappings[9]))

    # Work with length 5 signals
    len_5_signals = [signal_pattern for signal_pattern in signal_patterns if len(signal_pattern) == 5]
    # print('len_5_signals: {}'.format(len_5_signals))

    len_5_signals_stripped_of_known_segments = [(len_5_segment, list(set(len_5_segment).difference(set(segment_mappings.values())))) for len_5_segment in len_5_signals]
    # print('len_5_signals_stripped_of_known_segments: {}'.format(len_5_signals_stripped_of_known_segments))

    unknown_segments_in_len_5_signals = [list((set(len_5_segment).difference(set(segment_mappings.values())))) for len_5_segment in len_5_signals]
    # print('unknown_segments_in_len_5_signals: {}'.format(unknown_segments_in_len_5_signals))
    freq_of_segments = dict(Counter([item for sublist in unknown_segments_in_len_5_signals for item in sublist]).items())
    # print(freq_of_segments)

    # Identify segment B
    segment_mappings['B'] = [k for k, v in freq_of_segments.items() if v == 1][0]

    # Identify segment D
    segment_mappings['D'] = [k for k, v in freq_of_segments.items() if v == 3][0]

    # Work with length 6 signals - take 2
    len_6_signals_stripped_of_known_segments = [(len_6_segment, list((set(len_6_segment)).difference(set(segment_mappings.values())))) for len_6_segment in len_6_signals]
    # print('len_6_signals_stripped_of_known_segments: {}'.format(len_6_signals_stripped_of_known_segments))

    # Identify segment F
    outstanding_item = [(signal, segments[0]) for signal, segments in len_6_signals_stripped_of_known_segments if len(segments) == 1][0]
    segment_mappings['F'] = outstanding_item[1]

    # Identify 6
    signal_mappings[6] = outstanding_item[0]
    # print('6: {}'.format(signal_mappings[6]))

    # Identify segment C
    segment_mappings['C'] = list(set('abcdefg').difference(set(segment_mappings.values())))[0]

    print('segment_mappings: {}'.format(['{}: {}'.format(key, segment_mappings[key]) for key in sorted(segment_mappings)]))

    # Identify 2
    set_digit(2)

    # Identify 3
    set_digit(3)

    # Identify 5
    set_digit(5)

    # Identify 0
    set_digit(0)

    print('signal_mappings: {}'.format(signal_mappings))

    output_value = decode_output_values()
    print('output_value: {}'.format(output_value))

    output_values_sum += output_value

print('output_values_sum: {}'.format(output_values_sum))