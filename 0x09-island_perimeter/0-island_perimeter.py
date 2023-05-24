#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Start with the assumption that each land cell contributes 4 to the perimeter

                # Check adjacent cells and subtract the shared sides
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1  # Top cell is land, so subtract one side
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1  # Bottom cell is land, so subtract one side
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1  # Left cell is land, so subtract one side
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1  # Right cell is land, so subtract one side

    return perimeter
