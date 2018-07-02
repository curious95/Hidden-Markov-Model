#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:36:41 2018
"""


import pandas as pd
import numpy as np

data=pd.read_csv('/home/groot/Downloads/formattedFile.csv',delimiter=';')
from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
data.iloc[:,1]=le1.fit_transform(data.iloc[:,1])
le=LabelEncoder()
data.iloc[:,4]=le.fit_transform(data.iloc[:,4])
x=data.iloc[:,4].tolist()

m=np.zeros(max(x)+1)
for i in x:
    m[i]+=1
m=m/len(x)
tran=np.zeros((max(x)+1)*(max(x)+1))
tran=np.reshape(tran,((max(x)+1),(max(x)+1)))
prev=data.iloc[:,1][0]
for i in range(len(data)-1):
    if(prev==data.iloc[:,1][i]):
        k=i+1
        tran[data.iloc[:,4][i]][data.iloc[:,4][k]]+=1
    else:
        prev=data.iloc[:,1][i]

tran=pd.DataFrame(tran)
m=pd.DataFrame(m)
#m.to_csv('/home/aptus_user/Start_Probability.csv')
#tran.to_csv('/home/aptus_user/Transition_matrix.csv')
ind=[]
for i in tran.index:
    ind.append(le.inverse_transform(i))
newtran=pd.DataFrame(tran.values,index=ind,columns=ind)
newtran.to_csv('/home/groot/Transition_matrix.csv')
data=pd.read_csv('/home/groot/Transition_matrix.csv')
i=11
m=[]
m.append(data.iloc[:,i].nlargest(n=2))
c=0
ind=m[0].index.tolist()
for j in range(len(ind)):
    data.iloc[:,i+1][ind[j]]=0
c=0
while(c<10):
    for i in ind:
        tmp=data.iloc[:,i+1].nlargest(n=2)
        tmpind=tmp.index.tolist()
        m.append(tmp)
        ind=tmpind
        for j in range(len(ind)):
            data.iloc[:,i+1][ind[j]]=0
        c+=1
c=len(m)-1
while(c>=0):
    for i in m[c].index:
        print(data.iloc[:,0][i]+'->',end='')
    c-=1
print('Shot',end='')