import numpy as np
if __name__ == "__main__":
    radius = 100
    seeds = radius * np.loadtxt("test_dir/test.txt", dtype=np.float64)
    print(seeds)
    pass

