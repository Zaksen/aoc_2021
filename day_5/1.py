import re

with open('input.txt', 'r') as f:
    coordinates = [l.rstrip().split(' -> ') for l in f.readlines()]


coord = [[l[0].split(','), l[1].split(',')] for l in coordinates if l[0][0] == l[1][0] or l[0][1] == l[1][1]]

grid = [[0 for i in range(999)] for j in range(999)]

for c in coord:
    x1 = int(c[0][0])
    y1 = int(c[0][1])

    x2 = int(c[1][0])
    y2 = int(c[1][1])

    if x1 == x2:
        inf = min(y1, y2)
        sup = max(y1, y2)
        for i in range(inf, sup+1):
            grid[i][x1] += 1
    else:
        inf = min(x1, x2)
        sup = max(x1, x2)
        for i in range(inf, sup+1):
            grid[y1][i] += 1        

count = 0
for l in grid:
    for x in l:
        if x >= 2:
            count += 1

print(count) 

