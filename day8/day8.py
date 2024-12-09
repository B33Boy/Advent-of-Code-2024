
from collections import defaultdict
from itertools import combinations

# Part 1

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

# Part 2


def point_out_of_bounds(point: tuple[int, int], m: int, n: int) -> bool:
    if point[0] < 0 or point[0] >= m or point[1] < 0 or point[1] >= n:
        return True
    return False


def get_all_antinodes(p1: tuple[int, int], p2: tuple[int, int]) -> list[tuple[int, int]]:
    diff_x = p2[0] - p1[0]
    diff_y = p2[1] - p1[1]

    all_antinodes: list[tuple[int, int]] = [p1, p2]
    k = 1

    while True:
        antinode = (p1[0] - k*diff_x, p1[1] - k*diff_y)
        if point_out_of_bounds(antinode, m, n):
            break
        all_antinodes.append(antinode)
        k += 1

    k = 1
    while True:
        antinode = (p2[0] + k*diff_x, p2[1] + k*diff_y)
        if point_out_of_bounds(antinode, m, n):
            break
        all_antinodes.append(antinode)
        k += 1

    return all_antinodes


locs: set[tuple[int, int]] = set()

for char, points in char_map.items():

    perms = list(combinations(points, 2))

    for p1, p2 in perms:
        antinodes: list[tuple[int, int]] = get_all_antinodes(p1, p2)
        for node in antinodes:
            locs.add(node)

print(len(locs))
