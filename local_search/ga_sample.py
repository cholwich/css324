import ga
import random

MIN = -5
MAX = +5
NBITS = 16 

def to_chromosome(x, y):
     cx = int((x - MIN) / (MAX - MIN) * (2**NBITS - 1))
     cy = int((y - MIN) / (MAX - MIN) * (2**NBITS - 1))
     return format(cx, 'b').zfill(NBITS) \
             + format(cy, 'b').zfill(NBITS)

def from_chromosome(c):
    r = MAX - MIN
    cx = c[:NBITS]
    cy = c[NBITS:]
    x = int(cx, 2) / (2**NBITS - 1) * r
    y = int(cy, 2) / (2**NBITS - 1) * r
    return x, y

def f(c):
    x, y = from_chromosome(c)
    return 100 - (x-1)**2 - (y-1)**2

random.seed(7876)
initial_population = []
for i in range(10):
    x = random.uniform(MIN, MAX)
    y = random.uniform(MIN, MAX)
    initial_population.append(to_chromosome(x, y))

best_c = ga.genetic_algorithm(initial_population, f, 20000)
print('Best state =', from_chromosome(best_c))
