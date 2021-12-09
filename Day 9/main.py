with open("input.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
v = [[int(x) for x in l] for l in lines]
visited_matrix = [[False for x in l] for l in lines]


def ok(x, y):
    if 0 <= x < len(v) and 0 <= y < len(v[0]):
        return v[x][y]
    return 12


def dfs(x, y):
    if ok(x, y) == 12 or visited_matrix[x][y] or v[x][y] == 9:
        return 0
    visited_matrix[x][y] = True
    return 1 + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x + 1, y) + dfs(x, y + 1)


basins = []
for i in range(len(v)):
    for j in range(len(v[i])):
        if v[i][j] < ok(i - 1, j) and v[i][j] < ok(i, j - 1) and v[i][j] < ok(i + 1, j) and v[i][j] < ok(i, j + 1):
            print(v[i][j], i, j)
            basins.append(dfs(i, j))
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
