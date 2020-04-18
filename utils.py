import sys
import numpy as np
from model import SingleGraph, DualGraph

def create_linear_deprecation(a, m):
    """
    Creates the single graph plot for the linear deprecation of a value.
    Attributes:
        a - the starting value (euro)
        m - the total years of use
    """
    d = a / m
    x = np.arange(m + 1)
    y = a - d * x
    return SingleGraph(x, y, "linear deprecation")
    
def create_geometrical_deprecation(a, m, q):
    """
    Creates the single graph plot for the geometrical deprecation of a value.
    Attributes:
        a - the starting value (euro)
        m - the total years of use
        q - the deprecation quote
    """
    x = np.arange(m + 1)
    y = a * (1 - q) ** x
    return SingleGraph(x, y, "geometrical deprecation")

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = float(sys.argv[3])
    ld = create_linear_deprecation(a, b)
    gd = create_geometrical_deprecation(a, b, c)
    dg = DualGraph(ld, gd, "linear and geometrical deprecation")
    dg.render("years", "euro")
    