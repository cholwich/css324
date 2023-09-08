import eight_puzzle_tuple as problem
import utils
import informed

goal_node, n_visits = informed.a_star_graph_search(problem, problem.h1)
if goal_node is not None:
    print("Solution")
    print("========")
    utils.print_solution(goal_node)
    print("========")
    print("Path cost = %d" % goal_node[3])
    print("Number of Visited States = %d" % n_visits)
else:
    print("No solutions found")()
