from collections import deque

# a node = a tuple of 5 members
def create_node(state, parent, action, path_cost, depth):
    return (state, parent, action, path_cost, depth)

# Trace back from a goal node, n, to the initial node
# to generate a solution
def print_solution(n):
    r = deque() # double-end queue
    while n is not None:
        r.appendleft(n[0])
        n = n[1]
    for s in r:
        print(s)
