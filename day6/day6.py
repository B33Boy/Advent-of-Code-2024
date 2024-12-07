# Part 1

import copy

inp = []

with open('inp.txt', 'r') as f:
    for line in f:
        inp.append(list(line.rstrip()))

m = len(inp)
n = len(inp[0])

orientation_map = {'>': (0, 1),
                   'v': (1, 0),
                   '<': (0, -1),
                   '^': (-1, 0)}

next_orientation = {'>': 'v',
                    'v': '<',
                    '<': '^',
                    '^': '>'}


def find_initial_start(inp):
    # Find cursor position
    px = 0
    py = 0

    for i in range(len(inp)):
        if '^' in inp[i]:
            px = i
            py = inp[i].index('^')
    return px, py


def compute_next_step(px, py, orientation):
    dx, dy = orientation_map[orientation]
    nx = px + dx
    ny = py + dy
    return nx, ny


def run_simulation(inp, px, py):

    while True:
        # Get orientation from board, compute next step
        orientation = inp[px][py]
        nx, ny = compute_next_step(px, py, orientation)

        # Ensure the next step wouldn't be out of bounds
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            break

        # if blocked then calculate next orientation
        if inp[nx][ny] == '#':
            orientation = next_orientation[orientation]
            inp[px][py] = orientation
            nx, ny = compute_next_step(px, py, orientation)

        # mark current as X, then update position
        inp[px][py] = 'X'

        px = nx
        py = ny
        inp[px][py] = orientation


def get_count(inp):
    count = 0
    for i in range(m):
        for j in range(n):
            if inp[i][j] == 'X':
                count += 1
    return count


def print_board(inp):
    for row in inp:
        for col in row:
            print(col, end=" ")
        print()


inp_cpy = copy.deepcopy(inp)
origin_x, origin_y = find_initial_start(inp_cpy)
run_simulation(inp_cpy, origin_x, origin_y)

# print_board(inp_cpy)
print(1 + get_count(inp_cpy))


# Part 2
def run_simulation2(inp, px, py):
    path = []
    foundloop = False

    while True:
        # Get orientation from board, compute next step
        orientation = inp[px][py]
        nx, ny = compute_next_step(px, py, orientation)

        # Ensure the next step wouldn't be out of bounds
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            # If out of bounds, then mark
            # inp[px][py] = 'X'
            path.append((orientation, px, py))
            break

        if (orientation, px, py) in path:
            foundloop = True
            break

        # while blocked then calculate next orientation
        while inp[nx][ny] == '#':
            orientation = next_orientation[orientation]
            inp[px][py] = orientation
            nx, ny = compute_next_step(px, py, orientation)

        path.append((orientation, px, py))

        # mark current as X, then update position
        inp[px][py] = 'X'
        px = nx
        py = ny
        inp[px][py] = orientation

    # Reset board to original
    for _, x, y in path:
        inp[x][y] = '.'
    inp[origin_x][origin_y] = '^'

    return foundloop


num_inf_loops = 0
origin_x, origin_y = find_initial_start(inp)

for i in range(m):
    for j in range(n):
        if inp[i][j] == '#' or inp[i][j] == '^':
            continue

        # Place block
        inp[i][j] = '#'

        if run_simulation2(inp, origin_x, origin_y):
            num_inf_loops += 1

        # Replace original point
        inp[i][j] = '.'

print(num_inf_loops)
