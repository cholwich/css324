import random
import math


def simulated_annealing(s0, succ, f, schedule):
    best_value = -float("inf")
    u = s0
    i = 1
    while True:
        T = schedule(i)
        if T == 0:
            break
        s = list(succ(u))
        v = random.choice(s)
        dE = f(v) - f(u)
        if dE > 0:
            u = v
        else:
            p = math.exp(dE/T)
            r = random.uniform(0.0, 1.0)
            if r < p:
                u = v
        i += 1
        if f(u) > best_value:
            best_state = u
            best_value = f(u)
    return best_state
