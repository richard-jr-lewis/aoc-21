class School:
    def __init__(self, age: int, count: int):
        self.age = age
        self.count = count

    def __repr__(self) -> str:
        return 'age: {}; count {}'.format(self.age, self.count)

with open('day_6_input.txt') as file:
    inputs = list(map(int, file.readline().rstrip().split(',')))

print(inputs)

schools: list[School] = []

for i in range(0, 9):
    count = sum(input == i for input in inputs)
    if count > 0: schools.append(School(i, count))

print('Initial state: {}'.format(schools))

for i in range(1, 81):
    current_schools = schools.copy()
    for school in current_schools:
        school.age -= 1

        if school.age < 0:
            school.age = 6
            if school.count > 0:
                schools.append(School(8, school.count))

    print('After {} days: {}; Total fish: {}'.format(str(i).rjust(2, ' '), schools, sum(school.count for school in schools)))