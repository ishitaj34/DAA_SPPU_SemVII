def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

def isSafe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solveNQueens(board, row, n):
    # Base condition: all queens are placed
    if row == n:
        printBoard(board, n)
        return

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solveNQueens(board, row + 1, n)  
            board[row][col] = 0  # Backtrack

def NQueens(n):
    board = [[0]*n for _ in range(n)]
    solveNQueens(board, 0, n)

NQueens(4)
