import numpy as np
from point import Point

class TriangleObj(object):
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self) -> str:
        return f"Triangle(a:{self.a}, b:{self.b}, c:{self.c})"

    def is_in_cricumcircle(self, other_point: Point):
        """
        checks if the other_point is in the circumcircle of the triangle object
        I got the idea from this link:
        https://stackoverflow.com/questions/39984709/how-can-i-check-wether-a-point-is-inside-the-circumcircle-of-3-points
        """
        adx = self.a.x - other_point.x
        ady = self.a.y - other_point.y
        adxy = adx ** 2 + ady ** 2
        bdx = self.b.x - self.d.x
        bdy = self.b.y - self.d.y
        bdxy = bdx ** 2 + bdy ** 2
        cdx = self.c.x - other_point.x
        cdy = self.c.y - other_point.y
        cdxy = adx ** 2 + ady ** 2
        matrice = np.array([[adx, ady, adxy],
                            [bdx, bdy, bdxy],
                            [cdx, cdy, cdxy]])
        return np.linalg.det(matrice) > 0

