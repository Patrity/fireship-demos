print(0.1 + 0.2 == 0.3)

def are_equal(a, b, ε=1e-10):
    return abs(a - b) < ε

print(are_equal(0.1 + 0.2, 0.3))