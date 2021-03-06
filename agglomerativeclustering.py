# -*- coding: utf-8 -*-
"""AgglomerativeClustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yO4YC6kcmw-1yx1TAx_1UtO-4aOZOZgZ

Importing Library
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

"""Inserting Dataset"""

Data = {'x': [32,34,27,26,28,28,27,27,33,27,20,28,25,26,28,28,34,31,33,30],
        'y': [32,30,30,28,25,26,25,24,27,27,32,34,33,32,33,32,33,29,30,27]
       }

df = pd.DataFrame(Data,columns=['x','y'])

"""Converting Data into Dendrogram"""

dendrogram = sch.dendrogram(sch.linkage(df, method='ward'))

"""Converting data into Dendroids"""

plt.scatter(df['x'], df['y'])

"""Commencing Agglomerative Clustering"""

hc = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(df)

"""Showing results"""

plt.scatter(df['x'], df['y'], c=hc.labels_, s= 100)