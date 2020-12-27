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
from sklearn import mixture
from matplotlib import pyplot as plt


# part 1


data = pd.read_csv('aditya-problem-data.csv')
area = (np.array(data['Values of area'])).reshape(-1,1)

# score = [np.nan]
# K_value = 0

# for K in range(1,15):
#     gmm = mixture.GaussianMixture(n_components=K).fit(area)
#     score.append(gmm.score(area))
#     if (score[-1] - score[-2] <= 10**-3):
#         K_value = K-1
#         break
#         # it breaks at 9

K_value = 9
gmm = mixture.GaussianMixture(n_components=K_value, covariance_type='full', random_state = 42)
gmm.fit(area)
label = gmm.predict(area)

final = []
mean_ = []
std_ = []

for k in range(K_value):
    ls = []
    for l in range(len(label)):
        if (label[l] == k):
            ls.append(area[l][0])
    final.append(ls)
    mean_.append(st.mean(ls))
    std_.append(st.stdev(ls))
    ls.clear()
   
print("\nPart 1 - \n")
print("The value of Q is %d" %K_value)
print("\nRespective mean values are ", mean_)  
print("\nRespective Standard deviation's values are ", std_)  

# b part

print("\nPart 2\n")
print("Q represents the number of Gaussian Components.It has significance that Gaussian Mixture Model depends on the value of Q, thus final classification is dependent on Q and hence the accuracy of model.")


# # c part

# print("\nPart 3\n")
# list_3 = []

# for i in area:
#     if ( i <= 99999):
#         list_3.append(i)


# count = 0
# subset_sum = []
# for j in list_3:
#     if (list_3.count(99999-j) > 0):
#         count += 1
#         subset_sum.append([j,99999-j])

# print("Total number of Subsets with two elements and having sum 99999 is %d" %count)
# print("Hence There exists subset whose sum is 99999.")


