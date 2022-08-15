def initial_state():
    return []


def is_goal(s):
    return len(s) == 8


def successors(s):
    for new_r in range(1, 9):
        if placable(s, new_r):
            t = s[:]
            t.append(new_r)
            yield t, 1


def attack(r1, c1, r2, c2):
    return r1 == r2 or c1 == c2 or abs(c1-c2) == abs(r1-r2)


def placable(s, new_r):
    new_c = len(s)
    for c in range(len(s)):
        r = s[c]
        if attack(r, c, new_r, new_c):
            return False
    return True
