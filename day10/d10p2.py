import statistics

def calculate_line_completion_score(line: list[str]) -> int:
    total_score = 0

    for char in line:
        total_score = (total_score * 5) + completion_character_scores[char]

    return total_score

with open('day_10_input.txt') as file:
    inputs = [line.rstrip() for line in file.readlines()]

# print(inputs)

valid_pairs: list[tuple[str, str]] = [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]
# print(valid_pairs)

valid_pairs_dict: dict[str, str] = {'(': ')', '[': ']', '{': '}', '<': '>'}
# print(valid_pairs_dict)

completion_character_scores: dict[str, int] = {')': 1, ']': 2, '}': 3, '>': 4}
# print(illegal_character_scores)

opening_characters = [opening for opening, closing in valid_pairs]

incomplete_lines = []

for input in inputs:
    chunk_openings = []
    line_is_corrupted = False
    for opening_char in input:
        # print('chunk_openings: {}'.format(chunk_openings))
        if opening_char in opening_characters:
            chunk_openings.append(opening_char)
            # print('add: {}'.format(char))
        elif len([closing for opening, closing in valid_pairs if opening == chunk_openings[len(chunk_openings) - 1] and opening_char == closing]) == 1:
            chunk_openings.pop()
            # print('remove: {}'.format(char))
        else:
            line_is_corrupted = True
            break
    
    if not line_is_corrupted:
        incomplete_lines.append(chunk_openings)

print('incomplete lines:')
[print(''.join(x)) for x in incomplete_lines]

line_completions = []

for incomplete_line in incomplete_lines:
    closing_chars =[]
    while len(incomplete_line) > 0:
        opening_char = incomplete_line.pop()
        
        closing_char = valid_pairs_dict[opening_char]
        closing_chars.append(closing_char)
    
    line_completions.append(closing_chars)

# print(line_completions)

line_completion_scores = [calculate_line_completion_score(line_completion) for line_completion in line_completions]

print(line_completion_scores)

print('median: {}'.format(statistics.median(line_completion_scores)))