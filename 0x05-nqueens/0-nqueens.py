#!/usr/bin/python3

import sys


def solve_nqueens(N):
    """
    Solve the N Queens problem using backtracking.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Returns:
        List[List[int]]: List of solutions where each solution is represented
        as a list of queen positions.
    """
    # Initialize solutions with an empty list
    solutions = [[]]

    # Iterate over each row
    for row in range(N):
        solutions = place_queen(row, N, solutions)

    return solutions


def place_queen(row, N, prev_solutions):
    """
    Place a queen in the current row if it is safe to do so.

    Args:
        row (int): The current row.
        N (int): The size of the chessboard and the number of queens.
        prev_solutions (List[List[int]]): Previous solutions.

    Returns:
        List[List[int]]: Updated solutions
        after placing a queen in the current row.
    """
    new_solutions = []
    for solution in prev_solutions:
        for col in range(N):
            if is_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_safe(row, col, solution):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        row (int): Current row.
        col (int): Column position to check.
        solution (List[int]): Current solution configuration.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for r, c in enumerate(solution):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def main():
    """
    Main function to solve and print N Queens solutions.
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

    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, col] for i, col in enumerate(solution)])


if __name__ == '__main__':
    main()
