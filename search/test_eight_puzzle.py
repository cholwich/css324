import eight_puzzle as problem

s0 = problem.initial_state()
for succ, cost in problem.successors(s0):
    print(succ)
