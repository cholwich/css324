def initial_state():
    return (0, 0)

def is_goal(s):
    return s[1] == 4

def successors(s):
    x, y = s
    # Try to empty one bottle
    if x > 0:
        yield ((0, y), x)
    if y > 0:
        yield ((x, 0), y)
    # Try to fill up one bottle
    if x < 3:
        yield ((3, y), 3-x)
    if y < 5:
        yield ((x, 5), 5-y)
    # Try to pour from one to another
    t = 5-y
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t, 5), t)
        else:
            yield ((0, y+x), x)
    t = 3-x
    if y > 0 and t > 0:
        if y > t:
            yield ((3, y-t), t)
        else:
            yield ((x+y, 0), y)
