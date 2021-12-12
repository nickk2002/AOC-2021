def solve():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    graph = {}
    for line in lines:
        x, y = line.split('-')
        if not x in graph.keys():
            graph[x] = []
        graph.get(x).append(y)
        if not y in graph.keys():
            graph[y] = []
        graph[y].append(x)
    visited = {}
    path = []
    nr_times = 0

    def dfs(node, visit_twice=False):
        nonlocal nr_times
        path.append(node)
        if 'a' <= node[0] <= 'z':
            visited[node] = True
        if node == 'end':
            nr_times = nr_times + 1
            return
        for neighbour in graph[node]:
            if not visited.get(neighbour):
                dfs(neighbour, visit_twice)
                visited[neighbour] = False
                path.pop()
            if (neighbour != 'start' and neighbour != 'end') and visited.get(neighbour) and visit_twice == False:
                dfs(neighbour, True)
                path.pop()

    dfs('start')
    print(nr_times)


if __name__ == '__main__':
    solve()
