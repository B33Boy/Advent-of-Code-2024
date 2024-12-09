import re
from itertools import product, zip_longest


def equals_target(vals, target):
    def dfs(i, prodsum):
        if prodsum == target:
            return True

        if i >= len(vals)-1:
            return False

        return dfs(i+1, prodsum + vals[i+1]) or dfs(i+1, prodsum * vals[i+1])

    return dfs(0, vals[0])


def equals_target2(vals, target):
    # Fails because eval follows BEDMAS and here we want left-to-right

    n = len(vals)

    # n-1 gaps in between n values
    operations = product(["+", "*"], repeat=n-1)
    for ops in operations:
        expression = ''.join((a or '') + (b or '')
                             for a, b in zip_longest(vals, ops,  fillvalue=''))
        print(expression)
        if eval(expression) == target:
            return True

    return False


def equals_target3(vals, target):
    n = len(vals)

    # n-1 gaps in between n values
    operations = product(["+", "*"], repeat=n-1)

    for ops in operations:
        expression = vals[0]
        for val, operator in zip(vals[1:], ops):
            expression = f"({expression}{operator}{val})"
        if eval(expression) == target:
            return True
    return False


res = 0

with open('inp.txt', 'r') as f:
    for line in f:

        tot, vals = line.rstrip().split(':')
        tot = int(tot)

        vals = list(map(int, vals.split()))
        # vals = vals.split()  # For equals_target2

        if equals_target3(vals, tot):
            res += tot

# print(res)


# Part 2
res = 0


def eval_expression(expr):
    if "||" not in expr:
        return eval(expr)

    expr = expr.split("||")
    print(expr)
    tmp = ""
    for count, elem in enumerate(expr):
        if count == 0:
            continue


def equals_target4(vals, target):
    n = len(vals)

    # n-1 gaps in between n values
    operations = product(["+", "*", "||"], repeat=n-1)

    # pattern = r"(\d)\)(\d)"
    pattern = r"\)(?=\d|\))"

    for ops in operations:
        expression = vals[0]

        for val, operator in zip(vals[1:], ops):
            expression = f"({expression}{operator}{val})"

            if operator == '||':
                print("original: ", expression)
                expression = expression.replace("||", "")

                print("before: ", expression)
                num_subs = len(re.findall(pattern, expression))
                expression = re.sub(
                    pattern, r"", expression) + num_subs*')'

            print("after: ", expression, "\n")

            if eval(expression) == target:
                return True

    return False


def equals_target5(vals, target):
    n = len(vals)

    # n-1 gaps in between n values
    operations = product(["+", "*", "||"], repeat=n-1)
    for ops in operations:
        expression = vals[0]
        i = 1

        for operator in ops:
            if operator == "+":
                expression += vals[i]
            elif operator == '*':
                expression *= vals[i]
            elif operator == '||':
                expression = int(str(expression) + str(vals[i]))

            i += 1

        if expression == target:
            return True

    return False


with open('inp.txt', 'r') as f:
    for line in f:

        tot, vals = line.rstrip().split(':')
        tot = int(tot)

        vals = list(map(int, vals.split()))
        # vals = vals.split()  # For equals_target2

        if equals_target5(vals, tot):
            res += tot

print(res)
