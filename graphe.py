# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:06:26 2022

@author: Josué
"""
import numpy
import matplotlib.pyplot as plt
from jyquickhelper import RenderJsDot


def plot_network(mat):
    # Dessine un graph à l'aide du language DOT
    # https://graphviz.org/doc/info/lang.html
    rows = ["digraph{ ", '  rankdir="LR";', '  size="4,4";']
    for i in range(max(mat.shape)):
        rows.append("  %d;" % i)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i, j] > 0:
                rows.append("  %d -> %d;" % (i, j))
    rows.append("}")
    dot = "\n".join(rows)
    # print(dot)  # décommenter cette ligne pour voir le résultat
    return RenderJsDot(dot)

mat = numpy.array([[6, 3, 10, 14, 5,9,7,11,2,3],
                   [1, 5, 4, 6, 10,9,8,6,1],
                   [5, 8, 1, 3, 10,12,9,6,7]])
plot_network(mat)

