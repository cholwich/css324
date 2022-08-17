import copy


def initial_state():
    return ([[7, 2, 4], [5, 0, 6], [8, 3, 1]], 1, 1)


def is_goal(s):
    return s[0] == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = copy.deepcopy(board)
    new_board[r][c] = new_board[new_r][new_c]
    new_board[new_r][new_c] = 0
    return (new_board, new_r, new_c)
