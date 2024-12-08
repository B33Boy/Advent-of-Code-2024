
def equals_target(vals, target):
    def dfs(i, prodsum):
        if prodsum == target:
            return True

        if i >= len(vals)-1:
            return False

        return dfs(i+1, prodsum + vals[i+1]) or dfs(i+1, prodsum * vals[i+1])

    return dfs(0, vals[0])


res = 0

with open('inp.txt', 'r') as f:
    for line in f:

        tot, vals = line.rstrip().split(':')
        tot = int(tot)

        vals = list(map(int, vals.split()))

        if equals_target(vals, tot):
            res += tot

print(res)
