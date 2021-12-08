from collections import Counter, defaultdict

with open("input.txt") as f:
    lines = f.readlines()
v = Counter([int(x) for x in lines[0].split(",")])
print(v)

def solve(counter, input_size):
    copy = counter
    for counter in range(input_size):
        current = defaultdict(int)
        for value, cnt in copy.items():
            if value == 0:
                current[6] += cnt
                current[8] += cnt
            else:
                current[value - 1] += cnt
        copy = current
        print(copy)
    return sum(copy.values())


print(solve(v, 256))
