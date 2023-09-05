#!/usr/bin/python3
"""Solves the N queens puzzle"""

import sys

def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen on the board at a specific
    position(row, column)
    """
    for i in range(row):
        if board[i][col]:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j]:
            return False
    
    for i, j in zip(range(row, -1, -1), 
                    range(col, len(board), 1)):
        if board[i][j]:
            return False

    return True

def print_board(board):
    """Prints the coordinates of the queens on the board"""
    coordinates = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:
                coordinates.append([r, c])
    print(coordinates)

def solve_nqueens(N):
    """Solves for the nqueens using the value of N given in the input"""
    board = [[False]*N for _ in range(N)]

    def backtrack(row):
    """Recursive backtracking algorithm"""
        if row == N:
            print_board(board)
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = True
                backtrack(row + 1)
                board[row][col] = False

    backtrack(0)


if __name__ == "__main__":
    """
    Check if script is run as main program and
    parse command line arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
