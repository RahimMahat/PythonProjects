import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets._samples_generator import  make_blobs

# K-Means:

X,y_true = make_blobs(n_samples=700,centers=5,cluster_std=0.45,random_state=0)

plt.scatter(X[:,0],X[:,1],s=30)

func = KMeans(n_clusters=5)
func.fit(X)
y_func = func.predict(X)

plt.scatter(X[:,0],X[:,1],c=y_func, s= 15)
centers = func.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='black',s=70,alpha=1)
plt.show()