# print("Hello World")

# Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

#     Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#     Any live cell with two or three live neighbors lives on to the next generation.
#     Any live cell with more than three live neighbors dies, as if by overpopulation.
#     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
import time
import os
# grid = [[0]*30 for _ in range(30)]

def print_grid(grid):
    # global grid
    for _ in grid:
        g = ['1' if i == 1 else '.' for i in _]
        print(*g)
# print_grid()

# 10 11 12 13 14 15 16 17 18
# 0 0 0 1 1 1 0 0 0... [9]
# 1 1 0 0 0 1 1 0 0... [10]
# 0 1 1 0 1 0 0 1 1... [11]
# 0 0 0 1 1 1 1 0 0... [12]
# 1 0 0 1 1 0 0 1 1... [13]
# 1 1 0 0 0 1 1 0 0... [14]

# initial_config = [
#     (5, 1), (5, 2), (6, 1), (6, 2),  (7, 11),
#     (4, 12), (8, 12), (3, 13), (9, 13), (3, 14), 
#     (20, 20), (21, 20), (22, 20), (23, 20),
#     (23, 22), (19, 23), (22, 23),
#     (25, 25), (26, 25), (25, 26)]
initial_config = [
(12, 11), (13, 11), (14, 10), (14, 12), (15, 11),
(16, 11), (17, 11), (18, 11), (19, 10), (19, 12), (20, 11), (21, 11)
]
def initialize_grid(rows, cols, initial_config):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for (x, y) in initial_config:
        grid[x][y] = 1
    return grid

# Example usage:
rows, cols = 40, 60
grid = initialize_grid(rows, cols, initial_config)

# grid[9][13], grid[9][14] = 1, 1
# grid[10][10], grid[10][15], grid[10][16] = 1, 1, 1
# grid[11][11], grid[11][12], grid[11][18] =  1, 1, 1
# grid[12][13], grid[12][15], grid[12][16] = 1, 1, 1
# grid[13][10], grid[13][13] , grid[13][17] =  1, 1, 1
# grid[14][10], grid[14][11], grid[14][16] = 1, 1, 1

# print_grid(grid)

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, 1, -1]

turns = 1000

def get_count(i, j, grid):
    global dx, dy
    count = 0
    for _ in range(8):
        r = i + dx[_]
        c = j + dy[_]
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1:
            count += 1
    return count

# how many moves can computer make
for _ in range(turns):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count = get_count(i, j, grid)
            # print(f"{count=} | {i=} | {j=}")
            if grid[i][j] == 1:
                if count < 2 or count > 3:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1
            else:
                if count == 3:
                    grid[i][j] = 1
            # if count < 2:
            #     grid[i][j] = 0
            # elif count == 2 or count == 3:
            #     grid[i][j] = 1
            # elif count > 3:
            #     grid[i][j] = 1
    
    os.system("clear")
    print_grid(grid)
    time.sleep(0.1)
