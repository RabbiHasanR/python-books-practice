weird_bord = [['_'] * 3] * 3
print(weird_bord)

weird_bord[1][2] = 0
print(weird_bord)

# The outer list is made of three references to the same inner list. While it is
# unchanged, all seems right.
# Placing a mark in row 1, column 2 reveals that all rows are aliases referring to
# the same object.

# The problem with Example 2-13 is that, in essence, it behaves like this code:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

print(board)
board[1][2] = 1
print(board)


# On the other hand, the list comprehension from Example 2-12 is equivalent to this code:
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)

board[1][2] = 'Y'
print(board)

# Each iteration builds a new row and appends it to board .
# Only row 2 is changed, as expected.