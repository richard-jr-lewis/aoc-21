from collections import Counter
from collections import defaultdict

with open('day_14_input.txt') as file:
    starting_polymer_template = file.readline().strip()
    file.readline()
    lines = file.readlines()

print('starting_polymer_template: {}'.format(starting_polymer_template))

pair_insertions = dict([line.strip().split(' -> ') for line in lines])
print('pairs: {}'.format(pair_insertions))

starting_pairs: defaultdict[str, int] = defaultdict(int)

for i in range(0, len(starting_polymer_template) - 1, 1):
    pair = starting_polymer_template[i:i + 2]
    starting_pairs[pair] += 1

# print(dict(starting_pairs))

polymer_pairs = starting_pairs.copy()

for step in range(1, 41):
    new_polymer_pairs: defaultdict[str, int] = defaultdict(int)
    for pair in polymer_pairs.keys():
        new_bond = pair_insertions[pair]
        new_polymer_pairs[pair[0] + new_bond] += polymer_pairs[pair]
        new_polymer_pairs[new_bond + pair[1]] += polymer_pairs[pair]

    # print('After step {}: {}'.format(step, dict(new_polymer_pairs)))

    polymer_pairs = new_polymer_pairs.copy()

# For some reason, there is a difference in number of times an instance appears depending on where in the pair it is
# I don't know why this is the case - too lazy to determine :D
occurrences1: defaultdict[str, int] = defaultdict(int) # alleged instances of character 1 of a pair. e.g. if pair = AB, then instances of A
occurrences2: defaultdict[str, int] = defaultdict(int) # alleged instances of character 1 of a pair. e.g. if pair = AB, then instances of B
occurrences: defaultdict[str, int] = defaultdict(int)

for pair in polymer_pairs.keys():
    occurrences1[pair[0]] += polymer_pairs[pair]
    occurrences2[pair[1]] += polymer_pairs[pair]

for key in occurrences1:
    occurrences[key] = max(occurrences1[key], occurrences2[key])

min_occurence = min(occurrences.values())
max_occurence = max(occurrences.values())

print('length: {}; occurrences: {}; produces {} - {} = {}'.format(sum(occurrences.values()), [(key, occurrences[key]) for key in sorted(occurrences)], max_occurence, min_occurence, max_occurence - min_occurence))