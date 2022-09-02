def hill_climbing(s0, succ, f):
    # s0   = initial state
    # succ = successor function
    # f    = evaluation function
    u = s0                  # the current state
    while True:
        s = list(succ(u))
        v = max(s, key=f)   # candidate of the next state
        if f(v) > f(u):
            u = v
        else:
            return u
