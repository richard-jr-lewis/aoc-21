def neighbour_is_larger(cell: tuple[int, int], neighbour: tuple[int, int]) -> bool:
    neighbour_x = neighbour[0]
    neighbour_y = neighbour[1]

    if 0 <= neighbour_y < len(inputs) and 0 <= neighbour_x < len(inputs[neighbour_y]):
        # print('cell {} has neighbour: {}'.format(cell, neighbour))
        return inputs[neighbour_y][neighbour_x] > inputs[cell[1]][cell[0]]

    return True

def flood_fill(node: tuple[int, int]):
    queue: list[tuple[int, int]] = [node]
    basin: list[tuple[int, int]] = []
    while len(queue) > 0:
        # print('queue length: {}; queue: {}'.format(len(queue), queue))
        n = queue.pop(0)
        x = n[0]
        y = n[1]
        # print('n: {}; value: {}'.format(n, inputs[y][x]))
        # print('basin: {}'.format(basin))
        # print(inputs[y][x])
        if 0 <= y < len(inputs) and 0 <= x < len(inputs[y]) and inputs[y][x] < 9 and n not in basin:
            basin.append(n)
            queue.append((x + 1, y))
            queue.append((x, y + 1))
            queue.append((x - 1, y))
            queue.append((x, y - 1))

    return basin


with open('day_9_input.txt') as file:
    inputs = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

# print(inputs)

low_points: list[tuple[int, int]] = []

for y in range(0, len(inputs)):
    for x in range(0, len(inputs[y])):
        if (neighbour_is_larger((x, y), (x + 1, y))
            and neighbour_is_larger((x, y), (x, y + 1))
            and neighbour_is_larger((x, y), (x - 1, y))
            and neighbour_is_larger((x, y), (x, y - 1))):
            # print('append {}'.format((x,y)))
            low_points.append((x,y))

print('low_points: {}'.format(low_points))

basin_sizes = sorted([len(flood_fill(low_point)) for low_point in low_points], key=int, reverse=True)
print('basin_sizes: {}'.format(basin_sizes))

largest_basins_value = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print('largest_basins_value: {}'.format(largest_basins_value))