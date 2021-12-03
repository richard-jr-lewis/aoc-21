def get_most_common_bit(inputs, col):
    number_of_0s = 0
    number_of_1s = 0

    for row in inputs:
        if row[col] == 0: number_of_0s += 1
        if row[col] == 1: number_of_1s += 1

    most_common_bit = 0 if number_of_0s > number_of_1s else 1

    return most_common_bit

def get_most_common_bit_binary(most_common_bits_start, col):
    most_common_bits = []

    most_common_bit = get_most_common_bit(most_common_bits_start, col)

    for row in most_common_bits_start:
        if row[col] == most_common_bit:
            most_common_bits.append(row)

    print('col: {}; most_common_bit: {}; most_common_bits length: {}'.format(col, most_common_bit, len(most_common_bits)))

    if len(most_common_bits) > 1: return get_most_common_bit_binary(most_common_bits, col + 1)
    
    return ''.join([str(i) for i in most_common_bits[0]])

def get_least_common_bit_binary(least_common_bits_start, col):
    least_common_bits = []

    least_common_bit = 0 if get_most_common_bit(least_common_bits_start, col) == 1 else 1
    
    for row in least_common_bits_start:
        if row[col] == least_common_bit:
            least_common_bits.append(row)

    print('col: {}; least_common_bit: {}; least_common_bits length: {}'.format(col, least_common_bit, len(least_common_bits)))

    if len(least_common_bits) > 1: return get_least_common_bit_binary(least_common_bits, col + 1)
    
    return ''.join([str(i) for i in least_common_bits[0]])


with open('day_3_input.txt') as file:
    inputs = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

most_common_bit_binary = get_most_common_bit_binary(inputs, 0)
print('most_common_bit_binary: {}'.format(most_common_bit_binary))

least_common_bit_binary = get_least_common_bit_binary(inputs, 0)
print('least_common_bit_binary: {}'.format(least_common_bit_binary))

oxygen_generator_rating = int(most_common_bit_binary, 2)
co2_scrubber_rating = int(least_common_bit_binary, 2)

print('oxygen_generator_rating: {}; co2_scrubber_rating: {}'.format(oxygen_generator_rating, co2_scrubber_rating))

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print('life_support_rating: {}'.format(life_support_rating))