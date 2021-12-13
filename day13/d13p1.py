coords: list[tuple[int, int]] = []
folds: list[tuple[str, int]] = []

with open('day_13_input.txt') as file:
    line = file.readline()
    while line and line != '\n':
        line = line.strip()
        coord = line.split(',')
        coords.append((int(coord[0]), int(coord[1])))
        line = file.readline()
    
    line = file.readline()

    while line:
        line = line.strip('fold along').strip()
        instruction = line.split('=')
        folds.append((instruction[0], int(instruction[1])))
        line = file.readline()

print('coords: {}'.format(coords))

print('folds: {}'.format(folds))

fold = 0

for axis, value in folds:
    fold += 1
    print()
    print('fold: {}; axis: {}; value: {}'.format(fold, axis, value))

    new_coords = []
    for x, y in coords:
        # print('x: {}; y: {}'.format(x, y))
        if axis == 'x':
            # print('x true')
            if x >= value:
                x -= (abs(value - x) * 2)
                # print('x: {}'.format(x))
        elif axis == 'y':
            # print('y true')
            if y >= value:
                y -= (abs(value - y) * 2)
                # print('y: {}'.format(y))
        
        new_coords.append((x, y))
    
    coords = sorted(set(new_coords.copy()))

    print('fold: {}; dots: {}; coords: {}'.format(fold, len(coords), coords))