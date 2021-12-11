def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
    return lines


def solve_part_1(data):
    sum_scores = 0
    error_points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    matching = {
        "(": ')',
        "[": ']',
        "{": '}',
        "<": ">"
    }
    for line in data:
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            elif stack and matching[stack.pop()] != c:
                sum_scores += error_points[c]
                break
    return sum_scores


def solve(part):
    data = read_input()
    if part == 1:
        print("Part1",solve_part_1(data))
    elif part == 2:
        print("Part2",solve_part_2(data))


def solve_part_2(data):
    matching = {
        "(": ')',
        "[": ']',
        "{": '}',
        "<": ">"
    }
    scores_closing = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    list_scores = []
    for line in data:
        stack = []
        broken = False
        for c in line:
            if c in "([{<":
                stack.append(c)
            elif stack and matching[stack.pop()] != c:
                broken = True
                break
        if not broken and len(stack) > 0:
            sum_line = 0
            while len(stack) > 0:
                sum_line = sum_line * 5 + scores_closing[matching[stack.pop()]]
            list_scores.append(sum_line)
    list_scores.sort()
    return list_scores[len(list_scores) // 2]


solve(part=1)
solve(part=2)
