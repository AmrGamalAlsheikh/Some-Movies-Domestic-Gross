
# coding: utf-8

# ### Movie-Domestic-Gross 

# Import the packages needed to perform the analysis

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
get_ipython().magic('matplotlib inline')


# In[2]:

# Import the data
mov = pd.read_csv('Movie-Domestic-Gross.csv', encoding = 'latin1')


# In[3]:

# Explore the dataset
mov.head()


# In[4]:

# Check the summary of the dataframe
mov.describe()


# In[5]:

# Check the structure of the dataframe
mov.info()


# In[6]:

# Explore the categorical variable Studio
print(mov.Studio.unique())
print(len(mov.Studio.unique()))


# In[7]:

# Explore the categorical variable Genre
print(mov.Genre.unique())
print(len(mov.Genre.unique()))


# In[8]:

# Filter the dataframe by genre
mov2 = mov[(mov.Genre == 'action') | (mov.Genre == 'adventure') | (mov.Genre == 'animation') | 
           (mov.Genre == 'comedy') | (mov.Genre == 'drama')]
mov2.Genre.unique()
#len( mov2[mov2.Genre == 'action'])
#len( mov2[mov2.Genre == 'adventure'])
#len( mov2[mov2.Genre == 'animation'])
#len( mov2[mov2.Genre == 'comedy'])
#len( mov2[mov2.Genre == 'drama'])


# In[9]:

# Filter the dataframe by studio
mov3 = mov2[(mov2.Studio == 'Buena Vista Studios') | (mov2.Studio == 'Fox') | (mov2.Studio == 'Paramount Pictures') | 
            (mov2.Studio == 'Sony') | (mov2.Studio == 'Universal') | (mov2.Studio == 'WB')]
mov3.Studio.unique()


# In[10]:

# Check how the filters worked
print (mov3.Genre.unique())
print (mov3.Studio.unique())
print (len(mov3))


# In[11]:

mov3.columns=['DayofWeek', 'Director', 'Genre', 'MovieTitle', 'ReleaseDate',
       'Studio', 'AdjustedGross$mill', 'BudgetDollarmill', 'GrossMillions',
       'IMDbRating', 'MovieLensRating', 'Overseas$mill', 'Overseas%',
       'Profit$mill', 'Profit%', 'RuntimeMin', 'US$mill',
       'Gross%US']


# In[12]:

mov3.Genre  = mov3.Genre.astype('category')


# In[13]:

mov3.info()


# In[14]:

mov3.columns


# In[15]:

# Define the style
sns.set(style="darkgrid", palette="muted", color_codes=True)
# Plot the boxsplots

ax = sns.boxplot(data=mov3, x='Genre', y='Gross%US', orient='v',color='lightgray',showfliers=False)
plt.setp(ax.artists, alpha=0.5)

# Add in points to show each observation
sns.stripplot(x='Genre', y='Gross%US', data=mov3, jitter=True, size=6, linewidth=0, hue = 'Studio', alpha=0.7)

ax.axes.set_title('Domestic Gross % by Genre',fontsize=30)
ax.set_xlabel('Genre',fontsize=20)
ax.set_ylabel('Gross % US',fontsize=20)

# Define where to place the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:



