import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    if len(x) == len(y):
        return float(np.sum(np.array(x, dtype=float) * np.array(y, dtype=float)))
    raise ValueError("Vectors mismatched!")
