# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Sean Kelly, seankell@umich.edu

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
#
# + [Pandas Idiom: Splitting](#Pandas-Idiom:-Splitting) 
# + [Splitting to analyze data](#Splitting-to-analyze-data)
# + [Splitting to create new Series](#Splitting-to-create-new-Series)
# + [Takeaways](#Takeaways)

# # Imports

import numpy as np
import pandas as pd

# ## Pandas Idiom: Splitting

# - A useful way to utilize data is by accessing individual rows or groups of 
# rows and operating only on those rows or groups.  
# - A common way to access rows is indexing using the `loc` or `iloc` methods 
# of the dataframe. This is useful when you know what row indices you'd like to
# access.  
# - However, it is often required to subset a given data set based on some 
# criteria that we want each row of the subset to meet.  
# - We will look at selecting subsets of rows by splitting data based on row 
# values and performing analysis or calculations after splitting.

# ## Splitting to analyze data

# - Using data splitting makes it simple to create new dataframes representing 
# subsets of the initial dataframes
# - Find the average of one column of a group defined by another column

t_df = pd.DataFrame(
    {"col0":np.random.normal(size=10),
     "col1":np.random.normal(loc=10,scale=100,size=10),
     "col2":np.random.uniform(size=10)}
    )
t_below_average_col1 = t_df[t_df["col1"] < 10]
t_above_average_col1 = t_df[t_df["col1"] >= 10]
print([np.round(t_above_average_col1["col0"].mean(),4),
      np.round(t_below_average_col1["col0"].mean(),4)])

# ## Splitting to create new Series

# - We can use this splitting method to convert columns to booleans based on 
# a criterion we want that column to meet, such as converting a continuous 
# random variable to a bernoulli outcome with some probability p.

p = 0.4
t_df["col0_below_p"] = t_df["col2"] < p
t_df

# ## Takeaways

# - Splitting is a powerful but simple idiom that allows easy grouping of data
# for analysis and further calculations.  
# - There are many ways to access specific rows of your data, but it is
# important to use the right tool for the job.  
# - More information on splitting can be found [here][splitting].  
#
# [splitting]: https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#splitting

