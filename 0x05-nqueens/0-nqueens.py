#!/usr/bin/python3
import sys


def nqueens(n):
    """
    doc
    """
    def printBoard(board):
        res = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "Q":
                    res.append([i, j])
        print(res)

    col = set()
    pd = set()
    nd = set()
    result = []
    board = [["_"] * n for i in range(n)]

    def backtrack(row):
        if row == n:
            printBoard(board)
        for cl in range(n):
            if cl in col or row+cl in pd or row-cl in nd:
                continue
            board[row][cl] = "Q"
            col.add(cl)
            pd.add(row+cl)
            nd.add(row-cl)
            backtrack(row + 1)
            col.remove(cl)
            pd.remove(row+cl)
            nd.remove(row-cl)
            board[row][cl] = "_"

    backtrack(0)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except TypeError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be a numberi")
        sys.exit(1)
    nqueens(n)
