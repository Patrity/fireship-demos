square = lambda x: x**2
double = lambda x: x * 2
add = lambda x, y: x + y

numbers = [1, 2, 3, 4]
squared = list(map(square, numbers))
doubled = list(map(double, numbers))

print(squared)
print(doubled)

numbers_two = [4, 3, 2, 1]
added = list(map(add, numbers, numbers_two))

print(added)