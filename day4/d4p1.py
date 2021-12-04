class BingoCardNumber:
    def __init__(self, number, marked):
        self.number = number
        self.marked = marked

    def __repr__(self):
        return str(self.number)

bingo_numbers = []
bingo_cards = []
current_bingo_card = []

def read_file():
    global bingo_numbers
    global current_bingo_card

    with open('day_4_input.txt') as file:
        bingo_numbers = list(map(int, file.readline().rstrip().split(',')))

        while line := file.readline():
            if line == '\n':
                if current_bingo_card:
                    bingo_cards.append(current_bingo_card)
                    current_bingo_card = []
                continue

            bingo_row = [BingoCardNumber(int(n), False) for n in line.rstrip().split(' ') if n]
            
            current_bingo_card.append(bingo_row)
        
        bingo_cards.append(current_bingo_card)
        current_bingo_card = []

def is_col_a_winner(bingo_card):
    for col in range(0, len(bingo_card), 1):
        marked_numbers = 0

        for row in bingo_card:
            if row[col].marked: marked_numbers += 1

        # print('col: {}; marked_numbers: {}'.format([row[col] for row in bingo_card], marked_numbers))
        if marked_numbers == len(bingo_card[0]): return True
        marked_numbers = 0

    return False

def is_row_a_winner(bingo_card):
    for row in bingo_card:
        marked_numbers = 0

        for col in row:
            if col.marked: marked_numbers += 1
    
        # print('row: {}; marked_numbers: {}'.format(row, marked_numbers))
        if marked_numbers == len(bingo_card[0]): return True
        marked_numbers = 0

    return False

def calculate_score(bingo_card, last_number_called):
    sum_unmarked_numbers = 0

    for row in bingo_card:
        for col in row:
            if not col.marked: sum_unmarked_numbers += col.number

    print('sum_unmarked_numbers: {}; last_number_called: {}; final_score: {}'.format(sum_unmarked_numbers, last_number_called, sum_unmarked_numbers * last_number_called))

read_file()

print(bingo_numbers)
print()
print(bingo_cards)

for bingo_number in bingo_numbers:
    for bingo_card in bingo_cards:
        for row in bingo_card:
            for bingo_card_number in row:
                if bingo_card_number.number == bingo_number: bingo_card_number.marked = True

        if is_row_a_winner(bingo_card) or is_col_a_winner(bingo_card):
            calculate_score(bingo_card, bingo_number)
            quit()