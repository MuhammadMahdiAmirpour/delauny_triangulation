import random
from delaunay_triangulator import DelaunayTriangulator
from vertex import Vertex

import time

import matplotlib.pyplot as plt
import matplotlib.tri as tri

if __name__ == "__main__":
    WIDTH = int(100)
    HEIGHT = int(100)
    ns = range(10, 80, 10)  # n should be greater than 2
    time_list = []

    for n in ns:
        start = time.time()

        xs = [random.randint(1, WIDTH - 1) for _ in range(n)]
        ys = [random.randint(1, HEIGHT - 1) for _ in range(n)]
        zs = [0 for _ in range(n)]

        DT = DelaunayTriangulator(WIDTH, HEIGHT)
        for x, y in zip(xs, ys):
            DT.AddVertex(Vertex(x, y))

        # Remove the super triangle on the outside
        DT.Remove_Super_Triangles()

        # Helps in determining the neighbours of triangles. I felt it might help in the future
        # Remove this to speed up triangle generation
        DT.Find_Neighbours()

        XS, YS, TS = DT.export()

        # Creating a Triangulation without specifying the triangles results in the
        # Delaunay triangulation of the points.

        # Create the Triangulation; no triangles so Delaunay triangulation created.
        # triang = tri.Triangulation(xs, ys)

        triang = tri.Triangulation(XS, YS)

        end = time.time()
        time_list.append(end-start)

    # Plot the triangulation.
    plt.plot(ns, time_list)
    plt.show()

