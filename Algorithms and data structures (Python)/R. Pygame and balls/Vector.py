class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ')'

a = Vector(1, 2)
b = Vector(3, 4)
c = a + b
print(c.__str__())