# Part 1

import collections

a = []
b = []


with open("inp.txt", 'r') as f:
    for line in f:
        line = line.split()
        a.append(int(line[0]))
        b.append(int(line[1]))


a = sorted(a)
b = sorted(b)
s = 0

for i in range(len(a)):
    s += abs(a[i] - b[i])

print(s)

# Part 2

counter = collections.Counter(b)
b_freq = dict(counter)

sim = 0
# print(sorted(b_freq))

for a_val in a:
    sim += a_val * b_freq.get(a_val, 0)


print(sim)
