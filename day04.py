# --- Day 4: Giant Squid ---
import sys

class Number:
    def __init__(self, number):
        self.number = number
        self.marked = False


class Board:
    def __init__(self, numbers):
        self.numbers = [[Number(n) for n in row] for row in numbers]

    def mark_number(self, number_drawn):
        for row in self.numbers:
            for number in row:
                if number_drawn == number.number:
                    number.marked = True
                    break
        return 0

    def check_winner(self):
        for row in self.numbers:
            row_marked = [n.marked for n in row]
            if all(row_marked):
                return True

        for i in range(5):
            column_marked = []
            for j in range(5):
                column_marked.append(self.numbers[j][i].marked)
            if all(column_marked):
                return True
        return False

    def add_all_unmarked(self):
        total = 0
        for row in self.numbers:
            for number in row:
                if (not number.marked):
                    total += number.number
        return total


input_path = r"day04input.txt"
with open(input_path, "r") as file:
    lines = file.read().split('\n')
    number_calls = [int(x) for x in lines[0].split(',')]
    boards = []
    for i in range(2, len(lines), 6):
        board_numbers = []
        for j in range(5):
            board_numbers.append([int(x) for x in lines[i + j].replace('  ', ' ').strip().split(' ')])
        boards.append(Board(board_numbers)) 


boards_completed = []
for call in number_calls:
    for index, board in enumerate(boards):
        board.mark_number(call)
        has_won = board.check_winner()
        if has_won:
            if (index not in boards_completed):
                boards_completed.append(index) 
            
            if len(boards_completed) == 1:
                print(f"Part one result - First winner board => {board.add_all_unmarked() * call}")
                sys.exit()
                
            #elif len(boards_completed) == len(boards):
                #print(f"Part two result - Last winner board => {board.add_all_unmarked() * call}")
                #sys.exit()
