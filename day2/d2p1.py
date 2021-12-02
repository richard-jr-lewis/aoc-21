with open('day_2_input.txt') as file:
    inputs = [line for line in file.readlines()]

position_x = 0
position_y = 0

for input in inputs:
    direction, speed = input.split()
    
    if (direction == 'forward'):
        position_x += int(speed)
        continue

    if (direction == 'down'):
        position_y += int(speed)
        continue

    if (direction == 'up'):
        position_y -= int(speed)

print('position_x: {}; position_y: {}; x * y = {}'.format(position_x, position_y, position_x * position_y))