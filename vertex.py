import math
class Vertex(object):
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    __rmul__ = __mul__

    def __str__(self) -> str:
        return "Vertex(%s, %s)"%(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vertex(self.x + other.x, self.y + other.y)

    def distance(self, other):
        dist_obj = self - other
        return math.sqrt(dist_obj[0]**2 + dist_obj[1]**2)

