import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x, dtype=float)
    mode = Counter(x).most_common(1)[0][0]
    median = np.median(x)
    return (mean, float(median), float(mode))
