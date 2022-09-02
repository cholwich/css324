import random, math

MUTATION_RATE = 0.30

def genetic_algorithm(population, f, n):
    # population = initial set of individuals
    # f = evaluation function
    # n = number of iterations
    best_state = None
    best_value = -float('inf')
    for i in range(n):
        new_population = []
        print("Round %d/%d" % (i+1, n), end='\r')
        for j in range(len(population)):
            v = evaluate(population, f)
            x = select(population, v)
            y = select(population, v)
            child = cross_over(x, y)
            r = random.uniform(0.0, 1.0)
            if r < MUTATION_RATE:
                child = mutate(child)
            new_population.append(child)
        population = new_population
        s = max(population, key=f)
        v = f(s)
        if v > best_value:
            best_value = v
            best_state = s
    return best_state

def evaluate(population, f):
    return [f(p) for p in population]

def select(population, val):
    m = sum(val)
    r = random.uniform(0, m)
    c = 0
    for p, v in zip(population, val):
        c += v
        if c > r:
            return p

def another_select(population, f):
    r1 = random.randint(0, len(population)-1)
    r2 = random.randint(0, len(population)-1)
    indv1 = population[r1]
    indv2 = population[r2]
    if f(indv1) > f(indv2):
        return indv1
    else:
        return indv2

def cross_over(x, y):
    c = random.randint(0, len(x))
    return x[:c] + y[c:]

def mutate(x):
    c = random.randint(0, len(x)-1)
    x = x[:c] + str(random.randint(0, 1)) + x[c+1:]
    return x
