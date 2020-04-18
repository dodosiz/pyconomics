import sys
import numpy as np
from model import BaseGraph

def linear_deprecation(a, m):
    """
    Plots the linear deprecation of a value.
    Attributes:
        a - the starting value (euro)
        m - the total years of use
    """
    d = a / m
    x = np.arange(m + 1)
    y = a - d * x
    graph = BaseGraph(x, y, "years", "value in euro")
    graph.render("bo")

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    linear_deprecation(a, b)
    