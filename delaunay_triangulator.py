import numpy as np
from vertex import Vertex
from triangle_obj import TriangleObj

class DelaunayTriangulator(object):
    def __init__(self, WIDTH, HEIGHT):
        self.triangulation = []

        # Declaring the super triangle coordinate information
        self.SuperPointA = Vertex(-100, -100)
        self.SuperPointB = Vertex(2 * WIDTH + 100, -100)
        self.SuperPointC = Vertex(-100, 2 * HEIGHT + 100)

        superTriangle = TriangleObj(self.SuperPointA, self.SuperPointB, self.SuperPointC)

        self.triangulation.append(superTriangle)

    def AddVertex(self, p):

        bad_triangles = []

        for triangle in self.triangulation:
            # Check if the given point is inside the circumcircle of triangle
            if triangle.is_in_cricumcircle(p):
                # If it is then add the triangle to bad triangles
                bad_triangles.append(triangle)

        polygon = []

        # Routine is to find the convex hull of bad triangles
        # This involves a naive search method, which increases the time complexity
        for triangle in bad_triangles:
            for edge in triangle.edges:
                if edge not in polygon:
                    polygon.append(edge)
                elif edge in polygon:
                    polygon.remove(edge)
#         for current_triangle in bad_triangles:
#             for this_edge in current_triangle.edges:
#                 isNeighbour = False
#                 for other_triangle in bad_triangles:
#                     if current_triangle == other_triangle:
#                         continue
#                     for that_edge in other_triangle.edges:
#                         if this_edge == that_edge:
#                             # Check if the Edge is shared between two triangles
#                             # If the edge is shared it won't be included into the convex hull
#                             isNeighbour = True
#                 if not isNeighbour:
#                     polygon.append(this_edge)

        # Delete the bad triangles
        for each_triangle in bad_triangles:
            self.triangulation.remove(each_triangle)

        # Re-triangle the convex hull using the given point
        for each_edge in polygon:
            newTriangle = TriangleObj(each_edge.v0, each_edge.v1, p)
            self.triangulation.append(newTriangle)

    def Remove_Super_Triangles(self):
        # Removing the super triangle using Lamba function
        onSuper = lambda triangle: triangle.hasVertex(self.SuperPointA) or triangle.hasVertex(
            self.SuperPointB) or triangle.hasVertex(self.SuperPointC)

        for triangle_new in self.triangulation[:]:
            if onSuper(triangle_new):
                self.triangulation.remove(triangle_new)

    def export(self):

        ps = [p for t in self.triangulation for p in t.vertex_list]

        x_s = [p.x for p in ps]
        y_s = [p.y for p in ps]

        ts = [(ps.index(t.a), ps.index(t.b), ps.index(t.c)) for t in self.triangulation]

        return x_s, y_s, ts

