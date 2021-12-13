from collections import defaultdict

# Depth First Search
def dfs(graph: dict[str, list[str]], node: str, target: str, path: list[str]):
    new_path = path + [node]

    if node == target:
        paths.append(new_path)

    for neighbour in graph[node]:
        if neighbour not in new_path or not neighbour.islower():
            dfs(graph, neighbour, target, new_path)

with open('day_12_input.txt') as file:
    inputs = [list(map(str, line.strip().split('-'))) for line in file.readlines()]

# print(inputs)

connections: defaultdict[str, list[str]] = defaultdict(list)

for input in inputs:
    connections[input[0]].append(input[1])
    connections[input[1]].append(input[0])

# print(dict(connections))

paths = []

dfs(connections, 'start', 'end', paths)

[print(path) for path in sorted(paths)]

print('number of paths = {}'.format(len(paths)))