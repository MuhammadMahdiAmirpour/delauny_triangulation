from delaunay_triangulator import DelaunayTriangulator
from vertex import Vertex

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

if __name__ == "__main__":
    radius = 100
    data = np.loadtxt("test_dir/test.txt", dtype=np.float64)
    xs = data[:, 0] * radius
    ys = data[:, 1] * radius
    WIDTH = int(100)
    HEIGHT = int(100)

    DT = DelaunayTriangulator(WIDTH, HEIGHT)
    for x, y in zip(xs, ys):
        DT.AddVertex(Vertex(x, y))

    # Remove the super triangle on the outside
    DT.Remove_Super_Triangles()

    XS, YS, TS = DT.export()

    # Creating a Triangulation without specifying the triangles results in the
    # Delaunay triangulation of the points.

    triang = tri.Triangulation(XS, YS)

    # Plot the triangulation.
    fig, ax = plt.subplots()
    ax.margins(0.1)
    ax.set_aspect('equal')

    ax.triplot(triang, 'bo-')

    # print(XS)
    # print(YS)
    # print(TS)

    # ax.triplot(tri.Triangulation(XS, YS, TS), 'bo--')
    ax.set_title('Plot of Delaunay triangulation')

    plt.show()

