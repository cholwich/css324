from hillclimbing import *

def random_restart_hill_climbing(succ, f, rnd, n):
    # rnd  = function that randomly generates state
    # n    = number of iterations
    best_value = -float("inf")
    for i in range(n):
        s0 = rnd()
        u = hill_climbing(s0, succ, f)
        if f(u) > best_value:
            best_state = u
            best_value = f(u)
    return best_state
