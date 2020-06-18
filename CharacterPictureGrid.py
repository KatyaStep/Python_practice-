grid = [['.', '.', '.', '.', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['.', 'O', 'O', 'O', 'O', 'O'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]

# grid = [
#     [1,2], 
#     [4,5],
#     [7,8],
#     ]

#print (len(grid))

#g = grid[0]

# for i in range(len(g)):
#     print (g[i])

rows = len(grid[0])

for x in range(rows):
    for y in range (len(grid)):
        print(grid[y][x], end='') # Print the # or space.
    print() # Print a newline at the end of the row.
