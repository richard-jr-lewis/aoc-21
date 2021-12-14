from collections import Counter

with open('day_14_input.txt') as file:
    starting_polymer_template = file.readline().strip()
    file.readline()
    lines = file.readlines()

print('starting_polymer_template: {}'.format(starting_polymer_template))

pair_insertions = dict([line.strip().split(' -> ') for line in lines])
print('pairs: {}'.format(pair_insertions))

polymer_template = starting_polymer_template    
print('Template: {}'.format(polymer_template))

for step in range(1, 11):
    new_polymer_template = ''
    for i in range(0, len(polymer_template) - 1, 1):
        pair = polymer_template[i:i + 2]
        # print('step: {}; i: {}; pair: {}; next bond: {}'.format(step, i, pair, pair_insertions[pair]))
        if new_polymer_template == '': new_polymer_template += pair[0]
        new_polymer_template += pair_insertions[pair] + pair[1]
    
    print('After step {}: {}'.format(step, new_polymer_template))
    polymer_template = new_polymer_template

occurrences = dict(Counter(polymer_template))
min_occurence = min(occurrences.values())
max_occurence = max(occurrences.values())

print('length: {}; occurrences: {}; produces {} - {} = {}'.format(len(polymer_template), [(key, occurrences[key]) for key in sorted(occurrences)], max_occurence, min_occurence, max_occurence - min_occurence))