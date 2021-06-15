'''
Implement the function find_roots to find the roots of the quadratic equation: ax^2 + bx + c = 0.
The function should return a tuple containing roots in any order.
If the equation has only one solution, the function should return that solution as both elements of the tuple.
The equation will always have at least one solution.

The roots of the quadratic equation can be found with the following formula: X(1,2) = [-b +/- sqrt(b^2-4ac] / 2a
A quadratic equation.

For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1)
as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.
'''
import math
def find_roots(a, b, c):
    d = math. sqrt(b**2 - 4*a*c)
    plus = -b + d
    minus = -b - d
    x1 = (plus/(2*a))
    x2 = (minus/(2*a))
    res = (x1, x2)
    return res

print(find_roots(2, 10, 8));
