# """
# This function, gridChallenge, sorts each row alphabetically and then checks if the columns are sorted alphabetically as well.
# If all columns are sorted, it returns "YES"; otherwise, it returns "NO".
# """
def gridChallenge(grid):
    sorted_rows = []
    for row in grid:
        sorted_row = sorted(row)
        sorted_rows.append(sorted_row)

    transposed_grid = []
    for i in range(len(grid[0])):
        column = []
        for j in range(len(grid)):
            column.append(sorted_rows[j][i])
        transposed_grid.append(column)

    for col in transposed_grid:
        if col != sorted(col):
            return "NO"
    
    return "YES"
 
print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
