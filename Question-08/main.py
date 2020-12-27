# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:16:48 2020

@author: Mr. Aman Saini
"""

# for installing modules , use command in cmd  - pip install module_name
# e.g   pip install sklearn


import pandas as pd
import numpy as np
import statistics as st
from sklearn.cluster import KMeans
from sklearn import mixture


# part 1


data = pd.read_csv('aditya-problem-data.csv')

area = list(data['Values of area'])
index = list(range(0,len(area)))
area_1 = (np.array(area)).reshape(-1,1)


kmeans = KMeans().fit(area_1)
mu_k = kmeans.cluster_centers_
Q = len(mu_k)



gmm = mixture.GaussianMixture(n_components=Q, covariance_type='full', random_state = 42)
gmm.fit(area_1)
label = gmm.predict(area_1)


final = []
mean_ = []
std_ = []

for k in range(8):
    list_1 = []
    for l in range(len(label)):
        if (label[l] == k):
            list_1.append(area[l])
    final.append(list_1)
    mean_.append(st.mean(list_1))
    std_.append(st.stdev(list_1))
    list_1.clear()
    
print("\nPart 1 - \n")
print("The value of Q is %d" %Q)
print("Respective mean values are ", mean_)  
print("Respective Standard deviation's values are ", std_)  
    






# b part

print("\nPart 2\n")
print("Q represents the number of Gaussian Components.It has significance that Gaussian Mixture Model depends on the value of Q, thus final classification is dependent on Q.")




# c part


print("\nPart 3\n")
list_3 = []

for i in area:
    if ( i <= 99999):
        list_3.append(i)


count = 0
subset_sum = []
for j in list_3:
    if (list_3.count(99999-j) > 0):
        count += 1
        subset_sum.append([j,99999-j])

print("Total number of Subsets with two elements and having sum 99999 is %d" %count)
print("Hence There exists subset whose sum is 99999.")

