import re

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
biggest = 1000
matrix = [[0 for j in range(biggest)]
          for i in range(biggest)]
for line in lines:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r"\d+", line)]

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            matrix[y][x1] = matrix[y][x1] + 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            matrix[y1][x] = matrix[y1][x] + 1
    else:
        x = x1
        y = y1
        while not (x == x2 and y == y2):
            matrix[y][x] = matrix[y][x] + 1
            if x < x2:
                x = x + 1
            else:
                x = x - 1
            if y < y2:
                y = y + 1
            else:
                y = y - 1
        matrix[y][x] = matrix[y][x] + 1
count = 0
for i in range(biggest):
    for j in range(biggest):
        if matrix[i][j] >= 2:
            count = count + 1
print("FINAL: " + str(count))
