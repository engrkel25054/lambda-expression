# Program specification
"""
Write a lambda expression that has two numeric parameters. If the second argument equals zero, it should return
None. Otherwise, it should return the value of dividing the first argument by the second argument.
Hint: use a conditional expression.
"""

def my_map(my_func, x, y):
    if y == 0:
        return None
    else:
        return my_func(x, y)


a = int(input("a: "))
b = int(input("b: "))
print(my_map(lambda x, y: x / y, a, b))