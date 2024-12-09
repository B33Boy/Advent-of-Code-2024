
from collections import defaultdict
from itertools import combinations

locs: set[tuple[int, int]] = set()
inp: list[list[str]] = []
char_map: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

with open('inp.txt', 'r') as f:
    for line in f:
        inp.append(list(line.rstrip()))

for row_idx, row in enumerate(inp):
    for col_idx, elem in enumerate(row):

        if elem != '.':
            char_map[elem].append((row_idx, col_idx))


def get_antinodes(p1: tuple[int, int], p2: tuple[int, int]) -> list[tuple[int, int]]:
    diff_x = p2[0] - p1[0]
    diff_y = p2[1] - p1[1]

    return (p1[0] - diff_x, p1[1] - diff_y), (p2[0] + diff_x, p2[1] + diff_y)


m = len(inp)
n = len(inp[0])

# Generate antinodes for each point pair
for char, points in char_map.items():
    # print(char, points)
    perms = list(combinations(points, 2))

    for p1, p2 in perms:
        # print(p1, p2, end=' ')
        antinodes: list[tuple[int, int]] = get_antinodes(p1, p2)
        # print(antinodes)
        for node in antinodes:
            if node[0] >= 0 and node[0] < m and node[1] >= 0 and node[1] < n:
                locs.add(node)

print(len(locs))
