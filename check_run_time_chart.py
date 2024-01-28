import random
from delaunay_triangulator import DelaunayTriangulator
from vertex import Vertex

import time

import matplotlib.pyplot as plt
import matplotlib.tri as tri

if __name__ == "__main__":
    WIDTH = int(100)
    HEIGHT = int(100)
    ns = range(4, 51)  # n should be greater than 2
    time_list = []

    for n in ns:
        times = []
        for _ in range(5):
            start = time.time()

            xs = [random.randint(1, WIDTH - 1) for _ in range(n)]
            ys = [random.randint(1, HEIGHT - 1) for _ in range(n)]
            zs = [0 for _ in range(n)]

            DT = DelaunayTriangulator(WIDTH, HEIGHT)
            for x, y in zip(xs, ys):
                DT.AddVertex(Vertex(x, y))

            # Remove the super triangle on the outside
            DT.Remove_Super_Triangles()

            XS, YS, TS = DT.export()

            # Creating a Triangulation without specifying the triangles results in the
            # Delaunay triangulation of the points.

            triang = tri.Triangulation(XS, YS)

            end = time.time()
            times.append(end-start)
        print(len(times))
        time_list.append(sum(times)/len(times))

    # Plot the triangulation.
    plt.plot(ns, time_list)
    plt.show()

