import itertools

with open("input.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
v = []
for line in lines:
    part_1 = line.split(" | ")[0].split()
    part_2 = line.split(" | ")[1].split()
    v.append((part_1, part_2))


def compute(perm, list):
    output = ""
    for el in list:
        output += perm[el]
    return "".join(sorted(output))


def sort_string(characters: str):
    return "".join(sorted(characters))


def solve_for_list(input: list, output: list):
    elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    good_dict = {}
    for permutation in itertools.permutations(elements):
        good_dict = {
            compute(permutation, [0, 1, 2]): "7",
            compute(permutation, [1, 2]): "1",
            compute(permutation, [0, 1, 2, 3, 4, 5, 6]): "8",
            compute(permutation, [0, 1, 2, 3, 4, 5]): "0",
            compute(permutation, [0, 2, 3, 4, 5, 6]): "6",
            compute(permutation, [0, 1, 2, 3, 5, 6]): "9",
            compute(permutation, [1, 2, 5, 6]): "4",
            compute(permutation, [0, 1, 3, 4, 6]): "2",
            compute(permutation, [0, 2, 3, 5, 6]): "5",
            compute(permutation, [0, 1, 6, 2, 3]): "3"
        }
        found_dict = True
        for el in input:
            try:
                good_dict[sort_string(el)]
            except KeyError:
                found_dict = False
                break
        if found_dict:
            break
    num = ""
    for el in output:
        num += str(good_dict[sort_string(el)])
    return int(num)


total = sum(solve_for_list(input, output) for input, output in v)
print("SUM", total)
