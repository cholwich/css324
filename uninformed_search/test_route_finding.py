import route_finding as problem
import utils
import ucs

goal_node, n_visits = ucs.uniform_cost_tree_search(problem)
if goal_node is not None:
    print("Solution")
    print("========")
    utils.print_solution(goal_node)
    print("========")
    print("Path cost = %d" % goal_node[3])
    print("Number of Visited States = %d" % n_visits)
else:
    print("No solutions found")
