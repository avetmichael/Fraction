class Fraction():
    def __init__(self, numerator, denominator):
        self.a = numerator
        self.b = denominator
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False
    def __ne__(self, other):
        if self.a != other.a and self.b != other.b:
            return True
        return False
    def __gt__(self, other):
        if self.a > other.a and self.b > other.b:
            return True
        return False
    def __add__(self, other):
        return Fraction((self.a * other.b) + (other.a * self.b), (self.b * other.b))
    def __mul__(self, other):
        return Fraction((self.a * other.a), (self.b * other.b))
    def __truediv__(self, other):
        return Fraction((self.a * other.b), (self.b * other.a))
    def __sub__(self, other):
        return Fraction((self.a * other.b) - (other.a * self.b), (self.b * other.b))
    def print(self):
        print(self.a, end='')
        print('/', end='')
        print(self.b)

p1 = Fraction(5, 4)
p2 = Fraction(3, 2)
print(p1 == p2)
print(p1 != p2)
print(p1 > p2)
r = p1 + p2
q = p1 - p2
g = p1 * p2
k = p1 / p2
r.print()
q.print()
g.print()
k.print()