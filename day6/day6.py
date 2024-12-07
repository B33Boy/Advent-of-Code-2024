# Part 1

import copy
import time

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
    return px + dx, py + dy


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


def run_simulation3(inp, px, py):
    path = set()

    orientation = inp[px][py]

    while True:
        nx, ny = compute_next_step(px, py, orientation)

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            break

        while inp[nx][ny] == '#':
            path.add((orientation, px, py))
            orientation = next_orientation[orientation]
            nx, ny = compute_next_step(px, py, orientation)

        current_state = (orientation, px, py)
        if current_state in path:
            return True

        path.add((orientation, px, py))

        px, py = nx, ny

    return False


num_inf_loops = 0
origin_x, origin_y = find_initial_start(inp)

start = time.perf_counter()
for i in range(m):
    for j in range(n):
        if inp[i][j] == '#' or inp[i][j] == '^':
            continue

        # Place block
        inp[i][j] = '#'

        if run_simulation3(inp, origin_x, origin_y):
            num_inf_loops += 1
            # print(i, j, num_inf_loops)
        # print_board(inp)

        # Replace original point
        inp[i][j] = '.'

print(num_inf_loops)
print(f"Elapsed TIme: {time.perf_counter() - start} seconds")
