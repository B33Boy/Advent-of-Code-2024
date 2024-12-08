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

print(res)
