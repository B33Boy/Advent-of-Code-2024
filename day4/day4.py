# part 1
inp = []

with open('inp.txt', 'r') as f:
    for line in f:
        inp.append(list(line.rstrip()))


def find_word_count_in_arr(board, word):
    rows = len(board)
    cols = len(board[0])

    count = 0

    directions = [(0, 1),  # right
                  (0, -1),  # left
                  (1, 0),  # down
                  (-1, 0),  # up
                  (-1, 1),  # up-right
                  (-1, -1),  # up-left
                  (1, 1),  # down-right
                  (1, -1)  # down-left
                  ]

    def check_dir(x, y, dx, dy):
        for k in range(len(word)):
            nx = x + k*dx
            ny = y + k*dy

            # Check nx, ny bounds
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                return False

            if board[nx][ny] != word[k]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_dir(i, j, dx, dy):
                    count += 1

    return count


count = find_word_count_in_arr(inp, "XMAS")
print(count)

# Part 2


def find_word_count_in_arr(board):
    rows = len(board)
    cols = len(board[0])

    count = 0

    def check_x(x, y):
        if x-1 < 0 or x+1 >= rows or y-1 < 0 or y+1 >= cols:
            return False

        ur = (x-1, y+1)
        ul = (x-1, y-1)
        dr = (x+1, y+1)
        dl = (x+1, y-1)

        if (board[ul[0]][ul[1]] == "M" and board[dl[0]][dl[1]] == "M" and board[ur[0]][ur[1]] == "S" and board[dr[0]][dr[1]] == "S"):
            return True

        if (board[ul[0]][ul[1]] == "S" and board[dl[0]][dl[1]] == "S" and board[ur[0]][ur[1]] == "M" and board[dr[0]][dr[1]] == "M"):
            return True

        if (board[ul[0]][ul[1]] == "M" and board[dl[0]][dl[1]] == "S" and board[ur[0]][ur[1]] == "M" and board[dr[0]][dr[1]] == "S"):
            return True

        if (board[ul[0]][ul[1]] == "S" and board[dl[0]][dl[1]] == "M" and board[ur[0]][ur[1]] == "S" and board[dr[0]][dr[1]] == "M"):
            return True

        return False

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "A":
                if check_x(i, j):
                    count += 1

    return count


count = find_word_count_in_arr(inp)
print(count)
