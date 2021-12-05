def add_vent(x, y):
    if x not in vents:
        vents[x] = dict()

    if y not in vents[x]:
        vents[x][y] = 0
        
    vents[x][y] += 1
    # print('vents[{}][{}]: {}'.format(x, y, vents[x][y]))

with open('day_5_input.txt') as file:
    lines = file.readlines()

# print('lines: {}'.format(lines))

pairs = [line.strip().split(' -> ') for line in lines]
# print('pairs: {}'.format(pairs))

coord_pairs = [[[int(y) for y in x.split(',')] for x in line.strip().split(' -> ')] for line in lines]
# print('coord_pairs: {}'.format(coord_pairs))

vents = dict()

for coord_pair in coord_pairs:
    # print('coord_pair: {}'.format(coord_pair))
    x1 = coord_pair[0][0]
    x2 = coord_pair[1][0]
    y1 = coord_pair[0][1]
    y2 = coord_pair[1][1]

    if x1 == x2 or y1 == y2:
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        # print('min: [{}, {}]; max: [{}, {}]'.format(min_x, min_y, max_x, max_y))
        for x in range(min_x, max_x + 1):
            # print('x: {}'.format(x))
            for y in range(min_y, max_y + 1):
                # print('y: {}'.format(y))
                add_vent(x, y)
    else:
        dx = x2 - x1
        dy = y2 - y1
        dx_increment = 1 if dx > 0 else -1 if dx < 0 else 0
        dy_increment = 1 if dy > 0 else -1 if dy < 0 else 0
        # print('dx: {}; dy: {}; dx_increment: {}; dy_increment: {}'.format(dx, dy, dx_increment, dy_increment))
        diag_coord = coord_pair[0]

        while diag_coord[0] != coord_pair[1][0] + (1 * dx_increment) or diag_coord[1] != coord_pair[1][1] + (1 * dy_increment):
        # while diag_coord != coord_pair[1]:
            # print('diag_coord: {}; coord_pair[1]: {}'.format(diag_coord, coord_pair[1]))
            add_vent(diag_coord[0], diag_coord[1])
            diag_coord = [diag_coord[0] + (1 * dx_increment), diag_coord[1] + (1 * dy_increment)]

print(vents.items())

number_of_overlaps = 0

for row in vents.values():
    for col in row.values():
        if col > 1: number_of_overlaps += 1

print(number_of_overlaps)