import heapq
import os

def read_file(filename):
    with open(os.path.dirname(__file__) + '\\' + filename) as file:
        return [[int(i) for i in line.strip("\n")] for line in file.readlines()]

def dijkstra(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    neighbour_relative_positions: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)] # E, S, W, N

    shortest: list[list[int]] = [[-1] * max_x for _ in range(max_y)]
    shortest[start[1]][start[0]] = 0

    queue: list[tuple[int, int, int]] = []
    heapq.heappush(queue, (0, *start))

    visited: set[tuple[int, int]] = set()

    while queue:
        _, x, y = heapq.heappop(queue)
        visited.add((x, y))

        for neighbour_relative_position in neighbour_relative_positions:
            n_x, n_y = (x + neighbour_relative_position[0], y + neighbour_relative_position[1])
            if 0 <= n_x < max_x and 0 <= n_y < max_y:
                n_cost = grid[n_y][n_x]

                if  (n_x, n_y) not in visited:
                    new_cost = shortest[y][x] + n_cost

                    if new_cost < shortest[n_y][n_x] or shortest[n_y][n_x] == -1:
                        shortest[n_y][n_x] = new_cost
                        heapq.heappush(queue, (new_cost, n_x, n_y))

                        # print('shortest updated for ({}, {}) -> ({}, {}). new_cost = {}'.format(x, y, n_x, n_y, new_cost))
                        # [print(' '.join(str(pos).rjust(3, ' ') for pos in row)) for row in shortest]
                        # print()

    return shortest

inputs = read_file('day_15_input.txt')
# print(inputs)

max_y = len(inputs)
max_x = len(inputs[0])

start = (0, 0)
end = (max_x - 1, max_y - 1)

result = dijkstra(inputs, start, end)
# [print(' '.join(str(pos).rjust(3, ' ') for pos in row)) for row in result]
print('shortest path: {}'.format(result[end[1]][end[0]]))