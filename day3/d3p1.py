with open('day_3_input.txt') as file:
    inputs = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

number_of_0s = 0
number_of_1s = 0
most_common_bits = []
least_common_bits = []

for col in range(0, len(inputs[0]), 1):
    for row in inputs:
        if row[col] == 0: number_of_0s += 1
        if row[col] == 1: number_of_1s += 1

    print('number_of_0s: {}; number_of_1s: {}; most commmon bit: {}'.format(number_of_0s, number_of_1s, '0' if number_of_0s >= number_of_1s else '1'))
    most_common_bits.append(0 if number_of_0s >= number_of_1s else 1)
    least_common_bits.append(0 if number_of_0s < number_of_1s else 1)
    number_of_0s = 0
    number_of_1s = 0

print('most_common_bits: {}'.format(most_common_bits))
print('least_common_bits: {}'.format(least_common_bits))

gamma = int(''.join([str(i) for i in most_common_bits]), 2)
print('gamma: {}'.format(gamma))

epsilon = int(''.join([str(i) for i in least_common_bits]), 2)
print('epsilon: {}'.format(epsilon))

power_consumption = gamma * epsilon
print('power_consumption: {}'.format(power_consumption))