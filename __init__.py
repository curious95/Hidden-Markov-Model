import pandas as pd
import numpy as np
from hmmlearn import hmm

'''
data  = pd.read_csv('/home/groot/DevX/soccer/test.csv',delimiter=';')
data = data.loc[:,'Event']
data=data.iloc[:,]
s=list(set(data))
model=hmm.GaussianHMM(n_components=len(s),covariance_type="full",n_iter=100)
model.fit(data)\
'''



X1 = [[0], [1], [2],[1],[2]]


X = np.concatenate([X1])
lengths = [len(X1)]
print(lengths)
print(X)

remodel=hmm.GaussianHMM(algorithm='viterbi',n_components=3).fit(X1, lengths)
m=remodel.transmat_
m=pd.DataFrame(m)
Z2 = remodel.score(X1)


