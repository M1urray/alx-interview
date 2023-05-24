#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    if not grid:
        return 0
    rows = len(grid)
    perimeter = 0
    for row in range(rows):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                row == 0 or (len(grid[row - 1]) > j and grid[row - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                row == rows - 1 or (len(grid[row + 1]) >
                                 j and grid[row + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
