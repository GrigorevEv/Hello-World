class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ')'


a = Vector(1, 2)
b = Vector(3, 4)
c = a + b
d = a - b
e = a * b
f = b * a

print(c.__str__())
print(d.__str__())
print(e.__str__())
print(f.__str__())
print(d.__neg__())
