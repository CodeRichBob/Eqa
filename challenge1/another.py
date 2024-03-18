import math

#define a function f(x)
def f(x):
    return math.sin(x) + (3/4)*x - 1

#define the derivative of the function f(x)

def df(x):
    return math.cos(x) + 3/4

# Function to find the root using Newton raphson method

def find_root(x0, threshhold=1e-6, max_iterations=100):
    for i in range(max_iterations):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < threshhold:
            return x1
        x0 = x1
    return None

# Initial values
initial_values = [1.0, 2.0, 4.0]

# Solve for each initial value
for x0 in initial_values:
    root = find_root(x0)
    if root is not None and 0 < root < 6:
        print(f"Initial guess: {x0}, Root: {root}")
    else:
        print(f"Initial guess: {x0}, No root found within the domain (0.0, 6.0)")
