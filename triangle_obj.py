import numpy as np
from vertex import Vertex
from edge import Edge

class TriangleObj(object):
    def __init__(self, a: Vertex, b: Vertex, c: Vertex) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.vertex_list = [a, b, c]
        self.edges = [Edge(a, b),
                      Edge(a, c),
                      Edge(b, c)]
        self.neighbour = [None] * 3

    def hasVertex(self, vertex: Vertex):
        return self.a == vertex or self.b == vertex or self.c == vertex
    
    def __str__(self) -> str:
        return f"Triangle(a:{self.a}, b:{self.b}, c:{self.c})"

    def __repr__(self):
        '''
        return '<%s, [%s, %s, %s]>' % (
                hex(id(s)),
                hex(id(s.neighbour[0])),
                hex(id(s.neighbour[1])),
                hex(id(s.neighbour[2])))
        '''
        return '< ' + str(self.a) + str(self.b) + str(self.c) + ' >'

    def is_in_cricumcircle_check_by_radius(self, other_point: Vertex) -> bool:
        center = self.get_circumcenter()
        radius = self.get_circumradius()
        return center.distance(other_point) < radius

    def get_circumcenter(self) -> Vertex:
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
        d = 2 * ((ax-bx)*(by-cy) - (bx-cx)*(ay-by))
        ux = ((ax**2 + ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
        uy = ((ax**2 + ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
        return Vertex(ux, uy)

    def get_circumradius(self) -> float:
        """
        returns the circumradius of the triangle
        just get the distance from one of the points from the center
        """
        return self.a.distance(self.get_circumcenter())

