from collections import Counter

with open('day_7_input.txt') as file:
    inputs = list(map(int, file.readline().strip().split(',')))
# print(inputs)

crab_positions: dict[int, int] = dict(Counter(inputs).items())
print('Initial state: {}'.format(crab_positions))

total_fuel_for_positions: dict[int, int] = dict()

for possible_position in range(0, max(crab_positions.keys()) + 1):
    total_fuel_for_position = sum([(abs(crab_position - possible_position) * crab_positions[crab_position]) for crab_position in crab_positions.keys()])
    # print('total_fuel_for_position {}: {}'.format(possible_position, total_fuel_for_position))
    total_fuel_for_positions[possible_position] = total_fuel_for_position

min_fuel_position = min(total_fuel_for_positions, key = total_fuel_for_positions.get)
print('lowest fuel usage is at position {} ({} fuel)'.format(min_fuel_position, total_fuel_for_positions[min_fuel_position]))