import eight_queens as problem

s0 = problem.initial_state()
s0 = [1, 3, 5]
for succ, cost in problem.successors(s0):
    print(succ)