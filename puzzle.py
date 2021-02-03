"""Python module for validating a board of symbols.

    Functions
    ---------
        add_cell - add cell to a set of visited set
        validate_corner - check if a given corner is valid
        validate_column - check if a given column is valid
        validate_row - check if a given row is valid
        validate_board - check if a given board is valid
"""

from typing import List, Set

SAMPLE_BOARD = [
    "**** ****",
    "***1 ****",
    "**2 2****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   2  **",
    "  8  2***",
    "  4  ****"
]


def add_cell(cell: str, visited: Set[str]) -> bool:
    """
    Add cell to a set of visited set if it is not equal to '*' or ' '.
    If the same cell is already in the visited set, return False.
    Otherwise, return True.

    >>> add_cell('5', {'1', '2', '3'})
    True
    >>> add_cell('5', {'1', '2', '5'})
    False
    >>> add_cell('*', {'1', '2', '3'})
    True
    >>> add_cell(' ', {'1', '2', '3'})
    True
    """
    if cell in ('*', ' '):
        return True

    if cell in visited:
        return False

    visited.add(cell)

    return True


def validate_corner(board: List[str], diagonal: int) -> bool:
    """
    Check if a given corner is valid. A corner is considered to be valid
    if it does not contain repeated symbols except for '*' and ' '.

    >>> validate_corner(SAMPLE_BOARD, 1)
    True
    >>> validate_corner(SAMPLE_BOARD, 2)
    False
    """
    visited = set()

    # Check horizontal part of the corner
    horizontal = board[len(board) - diagonal - 1][diagonal:]

    for cell in horizontal:
        if not add_cell(cell, visited):
            return False

    # Check vertical part of the corner except for
    # the diagonal cell to avoid its duplication
    for idx in range(len(board) - diagonal - 1):
        cell = board[idx][diagonal]

        if not add_cell(cell, visited):
            return False

    return True


def validate_column(board: List[str], col: int) -> bool:
    """
    Check if a given column is valid. A column is considered to be valid
    if it does not contain repeated symbols except for '*' and ' '.

    >>> validate_column(SAMPLE_BOARD, 1)
    True
    >>> validate_column(SAMPLE_BOARD, 2)
    False
    """
    visited = set()

    for row, _ in enumerate(board):
        if not add_cell(board[row][col], visited):
            return False

    return True


def validate_row(board: List[str], row: int) -> bool:
    """
    Check if a given row is valid. A row is considered to be valid
    if it does not contain repeated symbols except for '*' and ' '.

    >>> validate_row(SAMPLE_BOARD, 1)
    True
    >>> validate_row(SAMPLE_BOARD, 2)
    False
    """
    visited = set()

    for col, _ in enumerate(board):
        if not add_cell(board[row][col], visited):
            return False

    return True


def validate_board(board: List[str]) -> bool:
    """
    Check if a given board is valid. A board is considered to be valid if each of its
    rows, columns and corners does not contain repeated symbols except for '*' and ' '.

    >>> validate_board(SAMPLE_BOARD)
    False
    """
    # Iterate through each row, column and corner
    for idx in range(9):
        is_valid_corner = validate_corner(board, idx)
        is_valid_column = validate_column(board, idx)
        is_valid_row = validate_row(board, idx)

        # If at least one item is not valid, the board is not valid
        if is_valid_corner and is_valid_column and is_valid_row:
            continue

        return False

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
