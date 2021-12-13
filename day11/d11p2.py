def print_grid():
    [print(' '.join(str(oct.energy_level) for oct in row)) for row in grid]

def reset_flash(x: int, y: int):
    if grid[y][x].has_flashed == True:
        grid[y][x].energy_level = 0
        grid[y][x].has_flashed = False

def add_energy(x: int, y: int):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x].energy_level += 1

def flash(x: int, y: int):
    global total_flashes
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        if grid[y][x].energy_level > 9 and not grid[y][x].has_flashed:
            total_flashes += 1
            grid[y][x].has_flashed = True
            # print('x: {}; y: {}; has flashed set to true'.format(x, y))
            add_energy_to_neighbours(x, y)

def add_energy_to_neighbours(x: int, y: int):
    add_energy(x + 1, y) # East
    add_energy(x + 1, y + 1) # South East
    add_energy(x, y + 1) # South
    add_energy(x - 1, y + 1) # South West
    add_energy(x - 1, y) # West
    add_energy(x - 1, y - 1) # North West
    add_energy(x, y - 1) # North
    add_energy(x + 1, y - 1) # North East

def build_flashes_to_process():
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x].energy_level > 9 and not grid[y][x].has_flashed:
                flashes_to_process.append(grid[y][x])

class Octopus:
    def __init__(self, x: int, y: int, energy_level: int) -> None:
        self.x = x
        self.y = y
        self.energy_level = energy_level
        self.has_flashed = False

    def __repr__(self) -> str:
        return 'x: {}; y: {}; energy_level: {}; has_flashed: {}'.format(self.x, self.y, self.energy_level, self.has_flashed)

with open('day_11_input.txt') as file:
    inputs = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

# [print(input) for input in inputs]

grid: list[list[Octopus]] = []

total_flashes = 0

for y in range(0, len(inputs)):
    row: list[Octopus] = []
    for x in range(0, len(inputs[y])):
        row.append(Octopus(x, y, inputs[y][x]))

    grid.append(row)

print('Before any steps:')
print_grid()

step = 0
number_of_0s = 0

while number_of_0s != 100:
    step += 1
    number_of_0s = 0
    # Increase energy level of each octopus
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            add_energy(x, y)

    # print('{} - after initial energy add:'.format(step))
    # print_grid()
    
    # If energy level > 9, the octopus flashes
    flashes_to_process = []
    build_flashes_to_process()

    while(len(flashes_to_process) > 0):
        for oct in flashes_to_process:
            flash(oct.x, oct.y)

        flashes_to_process = []
        build_flashes_to_process()

    # Reset the flashes
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            reset_flash(x, y)
            if grid[y][x].energy_level == 0:
                number_of_0s += 1

    print('After step {}, number_of_0s = {}:'.format(step, number_of_0s))
    print_grid()

print('total_flashes: {}'.format(total_flashes))
print('final step: {}'.format(step))