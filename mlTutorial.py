import pandas as pd
import numpy as np
import matplotlib as ml

"""
Panel:

items − axis 0, each item corresponds to a DataFrame contained inside.
major_axis − axis 1, it is the index (rows) of each of the DataFrames.
minor_axis − axis 2, it is the columns of each of the DataFrames.

Syntax : pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)

A Panel can be created using multiple ways like −

From ndarrays
From dict of DataFrames




"""

data = np.random.rand(2,4,5)
p= pd.Panel(data)
print(p)

data1 = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p1 = pd.Panel(data1)
print (p1['Item1'])