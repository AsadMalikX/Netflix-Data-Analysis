#!/usr/bin/env python
# coding: utf-8

# # Data Exploration

# In[271]:


# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings. filterwarnings('ignore')


# In[272]:


df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
df.head()


# In[273]:


# Printing the number of rows and coloumns
df.shape


# In[274]:


# Informtion about data
df.info()


# In[275]:


# Exploring Grnre coloumn
df['Genre'].head()


# In[276]:


# Checking the duplicated rows
df.duplicated().sum()


# In[277]:


# Getting the statistical measures about data
df.describe()


# # • Exploration Summary
# 
# • we have a dataframe consisting of 9827 rows and 9 columns.
# 
# • our dataset looks a bit tidy with no NaNs nor duplicated values.
# 
# • Release_Date column needs to be casted into date time and to extract only the year value.
# 
# • Overview, Original_Languege and Poster-Url wouldn't be so useful during analys, so we'll drop them.
# 
# • there is noticable outliers in Popularity column.
# 
# • Vote_Average bettter be categorised for proper analysis.
# 
# • Genre column has comma saperated values and white spaces that needs to be handled and casted into category.

# # Data Cleaning

# In[278]:


df.head()


# In[279]:


# Casting the coloumns
df['Release_Date'] = pd.to_datetime(df['Release_Date'])

# Confirming changes
print(df['Release_Date'].dtypes)


# In[280]:


df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes


# In[281]:


df.info()


# In[282]:


df.head()


# In[283]:


# Droping the irrelevant coloumns
cols = ['Overview', 'Original_Language', 'Poster_Url']


# In[284]:


df.drop(cols, axis = 1, inplace=True)
df.columns


# In[285]:


df.head()


# # categorizing Vote_Average column
# We would cut the Vote_Average values and make 4 categories: popular average
# below_avg not_popular to describe it more using catigorize_col() function
# provided above.

# In[286]:


def catigorize_col (df, col, labels):
 
 # setting the edges to cut the column accordingly
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates='drop')
    return df


# In[287]:


# define labels for edges
labels = ['not_popular', 'below_avg', 'average', 'popular']
# categorize column based on labels and edges
catigorize_col(df, 'Vote_Average', labels)
# confirming changes
df['Vote_Average'].unique()


# In[288]:


# exploring column
df['Vote_Average'].value_counts()


# In[289]:


# dropping NaNs
df.dropna(inplace = True)
# confirming
df.isna().sum()


# In[290]:


df.head()


# In[291]:


# split the strings into lists
df['Genre'] = df['Genre'].str.split(', ')
# explode the lists
df = df.explode('Genre').reset_index(drop=True)
df.head()


# In[292]:


# casting column into category
df['Genre'] = df['Genre'].astype('category')
# confirming changes
df['Genre'].dtypes


# In[293]:


df.info()


# In[294]:


df.nunique()


# # Data Visualization
# 
# here, we'd use Matplotlib and seaborn for making some informative visuals to gain
# insights abut our data.

# In[295]:


# setting up seaborn configurations
sns.set_style('whitegrid')


# # Q1: What is the most frequent genre in the dataset?

# In[296]:


# showing stats. on genre column
df['Genre'].describe()


# In[297]:


# visualizing genre column
sns.catplot(y = 'Genre', data = df, kind = 'count',
 order = df['Genre'].value_counts().index,
 color = '#4287f5')
plt.title('genre column distribution')
plt.show()


# we can notice from the above visual that Drama genre is the most frequent genre
# in our dataset and has appeared more than 14% of the times among 19 other
# genres.

# # Q2: What genres has highest votes ?

# In[298]:


# visualizing vote_average column
sns.catplot(y = 'Vote_Average', data = df, kind = 'count',
 order = df['Vote_Average'].value_counts().index,
 color = '#4287f5')
plt.title('votes destribution')
plt.show() 


# # Q3: What movie got the highest popularity ? what's its genre ?

# In[299]:


# checking max popularity in dataset
df[df['Popularity'] == df['Popularity'].max()]


# # Q4: What movie got the lowest popularity? what's its genre?

# In[300]:


# checking max popularity in dataset
df[df['Popularity'] == df['Popularity'].min()]


# # Q5: Which year has the most filmmed movies?

# In[301]:


df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()


# # Conclusion

# Q1: What is the most frequent genre in the dataset?
# 
# Drama genre is the most frequent genre in our dataset and has appeared more than 14% of the times among 19 other genres.
# 
# Q2: What genres has highest votes ?
# 
# We have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the highest popularity among fans by being having more than 18.5% of movies popularities.
# 
# Q3: What movie got the highest popularity ? what's its genre ?
# 
# Spider-Man: No Way Home has the highest popularity rate in our dataset and it has genres of Action , Adventure and Sience Fiction.
# 
# Q4: What movie got the lowest popularity ? what's its genre ?
# 
# The united states, thread' has the highest lowest rate in our dataset and it has genres of music , drama , 'war', 'sci-fi' and history.
# 
# Q4: Which year has the most filmmed movies?
# 
# Year 2020 has the highest filmming rate in our dataset

# In[ ]:





# In[ ]:




