
# coding: utf-8

# # Clustering using the Mean Shift algorithm
# ##### Using MeanShift to find clusters in the Titanic data set and examine each cluster

# In[3]:

import pandas as pd


# ### Titanic data set
# 
# <b>Download link: </b>https://www.kaggle.com/c/3136/download/train.csv
# 
# <b>Summary: </b>Information about passengers who were on the Titanic including whether they survived

# In[4]:

titanic_data = pd.read_csv('../data/titanic.csv', quotechar='"')
titanic_data.head()


# #### Drop columns which are meaningless when attempting to find patterns

# In[5]:

titanic_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], 'columns', inplace=True)
titanic_data.head()


# #### Convert the gender values to numbers

# In[6]:

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
titanic_data['Sex'] = le.fit_transform(titanic_data['Sex'].astype(str))
titanic_data.head()


# #### Apply one-hot encoding for the port of Embarkation

# In[7]:

titanic_data = pd.get_dummies(titanic_data, columns=['Embarked'])
titanic_data.head()


# #### Check how many rows in the data frame contain null values

# In[8]:

titanic_data[titanic_data.isnull().any(axis=1)]


# #### Rather than clean up all the missing NaN values, we drop them all

# In[9]:

titanic_data = titanic_data.dropna()


# #### Use Mean Shift in order to find clusters in the data
# * The bandwidth parameter specifies the "radius" of each cluster
# * Higher bandwidths will produce fewer clusters

# In[10]:

from sklearn.cluster import MeanShift

analyzer = MeanShift(bandwidth=30)
analyzer.fit(titanic_data)


# #### Default bandwidth for a data set is calculated using the estimate_bandwidth function

# In[11]:

# Getting the size of the bandwidth which MeanShift will have used by default
from sklearn.cluster import estimate_bandwidth
estimate_bandwidth(titanic_data)


# #### Fetch the labels generated by MeanShift for the Titanic data 

# In[12]:

labels = analyzer.labels_


# #### How many clusters do we have?

# In[13]:

import numpy as np

np.unique(labels)


# #### Create a new cluster_group column in the data frame for these labels 

# In[14]:

import numpy as np

titanic_data['cluster_group'] = np.nan
data_length = len(titanic_data)
for i in range(data_length):
    titanic_data.iloc[i, titanic_data.columns.get_loc('cluster_group')] = labels[i]


# In[15]:

titanic_data.head()


# #### Examine the overall data in the data set

# In[16]:

titanic_data.describe()


# #### Examine average data for each cluster

# In[17]:

titanic_cluster_data = titanic_data.groupby(['cluster_group']).mean()
titanic_cluster_data


# #### Add the counts for each cluster

# In[18]:

titanic_cluster_data['Counts'] = pd.Series(titanic_data.groupby(['cluster_group']).size())
titanic_cluster_data


# #### Examine the data in one of the clusters

# In[19]:

titanic_data[ titanic_data['cluster_group'] == 1 ].describe()


# #### View all the rows of one cluster

# In[20]:

titanic_data[ titanic_data['cluster_group'] == 0]


# In[ ]:



