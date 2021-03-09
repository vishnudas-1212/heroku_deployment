import numpy as np
import pandas as pd
import pickle

df=pd.read_csv('candidate.csv',index_col=0)
X = np.array(df.iloc[:,:-1])
y = np.array(df.iloc[:,-1])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.svm import SVC
sv = SVC(kernel='linear').fit(X_train,y_train)


pickle.dump(sv, open('iri.pkl', 'wb'))
