with open('day_10_input.txt') as file:
    inputs = [line.rstrip() for line in file.readlines()]

# print(inputs)

valid_pairs: list[tuple[str, str]] = [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]
# print(valid_pairs)

illegal_character_scores: dict[str, int] = {')': 3, ']': 57, '}': 1197, '>': 25137}
# print(illegal_character_scores)

opening_characters = [opening for opening, closing in valid_pairs]

first_illegal_characters = []

for input in inputs:
    chunk_openings = []
    for char in input:
        # print('chunk_openings: {}'.format(chunk_openings))
        if char in opening_characters:
            chunk_openings.append(char)
            # print('add: {}'.format(char))
        elif len([closing for opening, closing in valid_pairs if opening == chunk_openings[len(chunk_openings) - 1] and char == closing]) == 1:
            chunk_openings.pop()
            # print('remove: {}'.format(char))
        else:
            first_illegal_characters.append(char)
            break

print(first_illegal_characters)

print('first_illegal_characters score: {}'.format(sum([illegal_character_scores[x] for x in first_illegal_characters])))