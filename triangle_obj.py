import numpy as np
import math
from point import Point

class TriangleObj(object):
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self) -> str:
        return f"Triangle(a:{self.a}, b:{self.b}, c:{self.c})"

    def is_in_cricumcircle(self, other_point: Point) -> bool:
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

    def is_in_cricumcircle_check_by_radius(self, other_point: Point) -> bool:
        center = self.get_circumcenter()
        radius = self.get_circumradius()
        return center.distance(other_point) > radius

    def get_circumcenter(self) -> Point:
        """
        find the coordinates of circumcenter of the triangle object
        got the idea from the link below:
        https://stackoverflow.com/questions/56224824/how-do-i-find-the-circumcenter-of-the-triangle-using-python-without-external-lib
        """
        ax = self.a.x
        bx = self.b.x
        cx = self.c.x
        ay = self.a.y
        by = self.b.y
        cy = self.c.y
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
        uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
        return (ux, uy)

    def get_circumradius(self) -> float:
        """
        returns the circumradius of the triangle
        just get the distance from one of the points from the center
        """
        return self.a.distance(self.get_circumcenter())

