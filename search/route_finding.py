edges = [
    ["oradea", "zerind", 71], ["oradea", "sibiu", 151], 
    ["zerind", "arad", 75], ["arad", "timisoara", 118], 
    ["arad", "sibiu", 140], ["timisoara", "lugoj", 111],
    ["lugoj", "mehadia", 70], ["mehadia", "dobreta", 75], 
    ["dobreta", "craiova", 120], ["craiova", "rimnicu vilcea", 146], 
    ["craiova", "pitesti", 138], ["pitesti", "rimnicu vilcea", 97],
    ["pitesti", "bucharest", 101], ["rimnicu vilcea", "sibiu", 80], 
    ["sibiu", "fagaras", 99], ["fagaras", "bucharest", 211], 
    ["bucharest", "giurgiu", 90], ["bucharest", "urziceni", 85],
    ["urziceni", "hirsova", 98], ["urziceni", "vaslui", 142], 
    ["hirsova", "eforie", 86], ["vaslui", "lasi", 92], 
    ["lasi", "neamt", 87]
]

def initial_state():
    return "arad"

def is_goal(s):
    return s == "bucharest"

def successors(s):
    for e in edges:
        if e[0] == s:
            yield e[1], e[2]
        elif e[1] == s:
            yield e[0], e[2]
