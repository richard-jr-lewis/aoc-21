from collections import Counter

def add_count_to_dict(new_schools: dict[int, int], new_age: int, count: int):
    if new_age in new_schools:
        new_schools[new_age] += count
    else:
        new_schools[new_age] = count

with open('day_6_input.txt') as file:
    inputs = list(map(int, file.readline().rstrip().split(',')))

print(inputs)

schools: dict[int, int] = dict(Counter(inputs).items())

print('Initial state: {}'.format(schools))

for i in range(1, 257):
    new_schools: dict[int, int] = dict()
    for age in schools.keys():
        new_age = age - 1

        if new_age < 0:
            new_age = 6
            add_count_to_dict(new_schools, 8, schools[age])

        add_count_to_dict(new_schools, new_age, schools[age])

    schools = new_schools.copy()

    print('After {} days: {}; Total fish: {}'.format(str(i).rjust(2, ' '), schools, sum(count for count in schools.values())))