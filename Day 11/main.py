from collections import deque


def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        matrix = [[int(x) for x in line] for line in lines]
    return matrix


def in_matrix(x, y):
    return 0 <= x < 10 and 0 <= y < 10


def solve(data):
    sum_flashes = 0
    for _ in range(10000):
        ok = True
        for i in range(10):
            for j in range(10):
                if data[i][j] != 0:
                    ok = False
        if ok:
            print("DAY:", _)
            return

        queue = deque()
        for i in range(10):
            for j in range(10):
                data[i][j] = data[i][j] + 1
                if data[i][j] == 10:
                    data[i][j] = 0
                    queue.append((i, j))
        dirx = [-1, -1, 0, 1, 1, 1, 0, -1]
        diry = [0, 1, 1, 1, 0, - 1, -1, -1]
        while len(queue) > 0:
            i, j = queue.popleft()
            sum_flashes = sum_flashes + 1
            for dx, dy in zip(dirx, diry):
                if in_matrix(i + dx, j + dy):
                    if data[i + dx][j + dy] > 0:
                        data[i + dx][j + dy] = data[i + dx][j + dy] + 1
                        if data[i + dx][j + dy] == 10:
                            data[i + dx][j + dy] = 0
                            queue.append((i + dx, j + dy))

    print("Flashes", sum_flashes)


if __name__ == '__main__':
    data = read_input()
    solve(data)
