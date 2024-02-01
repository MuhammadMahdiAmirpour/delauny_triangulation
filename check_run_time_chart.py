from delaunay_triangulator import DelaunayTriangulator
from vertex import Vertex

import time

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.tri as tri

if __name__ == "__main__":
    WIDTH = int(100)
    HEIGHT = int(100)
    ns = range(3, 50)  # n should be greater than 2
    time_list = []
    data = np.loadtxt("test_dir/test.txt", dtype=np.float64) * HEIGHT

    for n in ns:
        times = []
        for _ in range(10):
            start = time.time()

            DT = DelaunayTriangulator(WIDTH, HEIGHT)
            for x, y in data[:n]:
                DT.AddVertex(Vertex(x, y))

            # Remove the super triangle on the outside
            DT.Remove_Super_Triangles()

            XS, YS, TS = DT.export()

            # Creating a Triangulation without specifying the triangles results in the
            # Delaunay triangulation of the points.

            triang = tri.Triangulation(XS, YS)

            end = time.time()
            times.append(end-start)
        time_list.append(sum(times)/len(times))

    # Plot the triangulation.
    plt.plot(ns, time_list)
    plt.show()

