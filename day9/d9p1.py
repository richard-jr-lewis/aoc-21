def neighbour_is_larger(cell: tuple[int, int], neighbour: tuple[int, int]) -> bool:
    neighbour_x = neighbour[0]
    neighbour_y = neighbour[1]

    if 0 <= neighbour_y < len(inputs) and 0 <= neighbour_x < len(inputs[neighbour_y]):
        # print('cell {} has neighbour: {}'.format(cell, neighbour))
        return inputs[neighbour_y][neighbour_x] > inputs[cell[1]][cell[0]]

    return True


with open('day_9_input.txt') as file:
    inputs = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

# print(inputs)

low_points: list[int] = []

for y in range(0, len(inputs)):
    for x in range(0, len(inputs[y])):
        if (neighbour_is_larger((x, y), (x + 1, y))
            and neighbour_is_larger((x, y), (x, y + 1))
            and neighbour_is_larger((x, y), (x - 1, y))
            and neighbour_is_larger((x, y), (x, y - 1))):
            # print('append {}'.format(inputs[y][x]))
            low_points.append(inputs[y][x])

print(low_points)

total_risk_level = sum([low_point + 1 for low_point in low_points])
print('total_risk_level: {}'.format(total_risk_level))