ifile = "example.txt"

with open(ifile, mode="r") as f:
    lines = [line.strip() for line in f]

random_numbers = list(map(int, lines[0].split(",")))

boards = list()
board = list()

for i in range(2, len(lines)):
    line = lines[i]
    if len(line) > 0:
        board.append([(int(n), False) for n in line.split()])
    else:
        boards.append(board)
        board = list()

boards.append(board)

def winner(board):
    # check rows
    for row in board:
        marks = [mark for _, mark in row]
        if all(marks):
            return True

    # check cols
    for col in range(len(board[0])):
        marks = [board[row][col][1] for row in range(len(board))]
        if all(marks):
            return True

    return False


winner_found = False
for number in random_numbers:
    if winner_found:
        break

    boards = [[[(val, True) if number == val else (val, mark)
                for val, mark in row]
                for row in board]
                for board in boards]

    for board in boards:
        if winner(board):
            winner_found = True
            summe = sum([val for row in board for val, mark in row if not mark])
            print(f"part1: {number * summe}")
            break
