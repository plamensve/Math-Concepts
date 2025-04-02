import numpy as np


def solve_phistomefel_ring(sudoku_grid, red_cells, blue_cells):
    """
    Prove that the set (list in python) of red cells contains the same numbers as the set (list in python) of blue cells.
    """
    red_nums = [sudoku_grid[row, col] for row, col in red_cells]
    blue_nums = [sudoku_grid[row, col] for row, col in blue_cells]

    return sorted(red_nums) == sorted(blue_nums)


sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

red_cells = [(0, 0), (0, 1), (1, 0), (1, 1), (7, 0), (7, 1), (8, 0), (8, 1), (0, 7), (0, 8), (1, 7), (1, 8), (7, 7),
             (7, 8), (8, 7), (8, 8)]
blue_cells = [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6),
              (2, 5), (2, 4), (2, 3)]

areEqual = solve_phistomefel_ring(sudoku, red_cells, blue_cells)
print(areEqual)
