import random
from delaunay_triangulator import DelaunayTriangulator
from vertex import Vertex

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    WIDTH = int(100)
    HEIGHT = int(100)
    n =  21 # n should be greater than 2

    xs = [random.randint(1, WIDTH-1) for _ in range(n)]
    ys = [random.randint(1, HEIGHT-1) for _ in range(n)]

    # data = np.loadtxt("test_dir/test.txt", dtype=np.float64) * HEIGHT

    DT = DelaunayTriangulator(WIDTH, HEIGHT)
    for x, y in zip(xs, ys):
        DT.AddVertex(Vertex(x, y))

    # Remove the super triangle on the outside
    DT.Remove_Super_Triangles()

    XS, YS, TS = DT.export()

    fig, ax = plt.subplots()
    ax.margins(0.1)
    ax.set_aspect('equal')

    ax.set_title('Plot of Delaunay triangulation')

    for idx1, idx2, idx3 in TS:
        xs = [XS[idx1],XS[idx2],XS[idx3]]
        ys = [YS[idx1],YS[idx2],YS[idx3]]
        plt.scatter(xs, ys, color="red")
        plt.plot(xs + [XS[idx1]], ys + [YS[idx1]], linestyle="-", color="blue")

    plt.show()

