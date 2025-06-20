import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime as dt

from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
from sklearn.metrics import mean_poisson_deviance, mean_gamma_deviance, accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import learning_curve, train_test_split

from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from tqdm import tqdm

import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")


# ## Load dataset

# In[2]:


df = pd.read_csv('../Dataset/VCB.csv')


# In[3]:


df = df.sort_values(by='date', ascending=True).reset_index(drop=True)


# In[4]:


df.info()


# In[5]:


df.describe()


# ## Data Cleaning

# In[6]:


df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


# In[7]:


df = df.dropna()


# ## Data Visualization

# In[8]:


plt.figure(figsize=(16,6))
plt.title('Close Price History')
plt.plot(df['close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()


# ## Manipulate data

# In[9]:


# Create a new dataframe
data = df.filter(['close'])
# Convert the dataframe to a numpy array
dataset = data.values


# In[10]:


# scaler = MinMaxScaler(feature_range=(0,1))
scaler = StandardScaler()
scaled_data = scaler.fit_transform(dataset)

scaled_data