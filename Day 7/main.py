with open("input.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
v = [int(x) for x in lines[0].split(",")]
sum = sum(v)
min_value = 2e9
for el in range(1200):
    value = 0
    for el2 in v:
        n = abs(el2 - el)
        value += n * (n + 1) / 2
    min_value = min(min_value,value)
print(min_value)