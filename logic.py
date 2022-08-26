# Heron's Formula

# Heron's formula in geometry gives us a method to find out the area of a triangle with sides a, b, and c.
# The formula is:
# area = sqrt(s(s - a)(s - b)(s - c))
# where s = (a + b + c) / 2

def HeronFormula(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Considering triangle with sides 25,56,76
print(HeronFormula(25, 56, 76))