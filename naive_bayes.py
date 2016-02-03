
# coding: utf-8

# In[1]:

import csv
import datetime
import pandas as pd
import numpy as np

demographic_data = {}
with open('demographic.csv', 'rbU') as csvfile:
    demo_fields = []
    demographic_read = csv.reader(csvfile, delimiter=';')
    for row in demographic_read:
        if len(demo_fields) == 0:
            demo_fields = row[2:] #row[2:] are actual data
        else:
            demographic_data[row[1]] = row[2:] #row[1] is PdDistrict, used as index
            
df_demographic = pd.DataFrame(demographic_data).transpose()
df_demographic.columns = demo_fields


# In[4]:

df_train = pd.read_csv('../sf/train.csv', parse_dates=['Dates'])
df_train.drop(['Descript', 'Resolution'], axis=1, inplace=True)
df_train = df_train.join(df_demographic, on='PdDistrict')
for column_name in ['Category', 'DayOfWeek', 'PdDistrict']:
    df_train[column_name] = pd.Categorical.from_array(df_train[column_name]).labels


# In[5]:

df_test = pd.read_csv('../sf/test.csv', parse_dates=['Dates'])
df_test = df_test.join(df_demographic, on='PdDistrict')
for column_name in ['DayOfWeek', 'PdDistrict']:
    df_train[column_name] = pd.Categorical.from_array(df_train[column_name]).labels


# In[6]:

'''
from sklearn.feature_extraction.text import CountVectorizer
cvec = CountVectorizer()
bows_train = cvec.fit_transform(df_train['Address'][:100000,].values)
'''
inds = np.arange(df_train.shape[0])
np.random.shuffle(inds)
'''
from sklearn.cross_validation import KFold
kf = KFold(df_train.shape[0], n_folds = 10)
for train, test in kf:
    #print("%s %s" % (train, test))
    print df_train.loc[train,:].shape, df_train.loc[test,:].shape
'''


# In[7]:

df_train, df_val = df_train[:int(0.8*len(inds))], df_train[int(0.8*len(inds)):]


# In[8]:

from patsy import dmatrices, dmatrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

y_train, X_train = dmatrices('Category ~ X + Y + DayOfWeek + PdDistrict', df_train)
y_val, X_val = dmatrices('Category ~ X + Y + DayOfWeek + PdDistrict', df_val)


# In[13]:

logistic = LogisticRegression(max_iter=10)
logistic.fit(X_train, y_train.ravel())


# In[14]:

print('Mean accuracy (Logistic): {:.4f}'.format(logistic.score(X_val, y_val.ravel())))


# In[ ]:



