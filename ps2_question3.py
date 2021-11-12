# -*- coding: utf-8 -*-
# # Problem Set 2, Question 3 Stand Alone Script

# # Imports

import pandas as pd
from IPython.core.display import display, Markdown

# # Question 3

# ### a

file_exts = ['https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT',
             'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT',
             'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT',
             'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT']
cohorts = ['2011-2012', '2013-2014', '2015-2016', '2017-2018']
cols_to_keep=['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH3', 'DMDEDUC2',
              'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR',
              'WTINT2YR', 'cohort']
nhanes_demo_df = pd.DataFrame()

for file, cohort in zip(file_exts, cohorts):
    df = pd.read_sas(file)
    df['cohort'] = cohort
    nhanes_demo_df = nhanes_demo_df.append(df[cols_to_keep])

col_renames = {'SEQN':'id',
               'RIDAGEYR':'age',
               'RIAGENDR':'gender',
               'RIDRETH3':'race and ethnicity',
               'DMDEDUC2':'education',
               'DMDMARTL':'marital status',
               'RIDSTATR':'interview/examination status',
               'SDMVPSU':'pseudo-psu variance estimation',
               'SDMVSTRA':'pseudo-stratum variance estimation',
               'WTMEC2YR':'2 year exam weights',
               'WTINT2YR':'2 year interview weights'}

nhanes_demo_df = nhanes_demo_df.rename(columns=col_renames)

nhanes_demo_df['2 year exam weights'] = nhanes_demo_df[
    '2 year exam weights'].apply(lambda x: 0 if x < 2566.1838545 else x)
nhanes_demo_df['2 year interview weights'] = nhanes_demo_df[
    '2 year interview weights'].apply(lambda x: 0 if x < 2571.0687123 else x)

# Convert datatypes, making categorical data ints then categories so category
# names are not floats
col_retypes = {'id':int,
               'age':int,
               'gender':'Int32',
               'race and ethnicity':'Int32',
               'education':'Int32',
               'marital status':'Int32',
               'interview/examination status':'Int32',
               'pseudo-psu variance estimation':'Int32',
               'pseudo-stratum variance estimation':'Int32'}
nhanes_demo_df = nhanes_demo_df.astype(col_retypes)
col_retypes = {'gender':'category',
               'race and ethnicity':'category',
               'education':'category',
               'marital status':'category',
               'interview/examination status':'category',
               'pseudo-psu variance estimation':'category',
               'pseudo-stratum variance estimation':'category'}
nhanes_demo_df = nhanes_demo_df.astype(col_retypes)

display(Markdown(nhanes_demo_df.head().to_markdown(index=False)))
nhanes_demo_df.to_pickle('./nhanes_demographic_dataframe.pkl')

# ### b

file_exts = ['https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT',
             'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT',
             'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT',
             'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT']
cols_to_keep = ['SEQN', 'OHDDESTS']
col_new_names = ['id', 'dentition status code']
col_renames = {'SEQN':'id', 'OHDDESTS':'dentition status code'}
col_retypes = {'id':int, 'dentition status code':'Int32'}
col_retypes2 = {'dentition status code':'category'}
for i in range(32):
    cols_to_keep.append('OHX{:02d}TC'.format(i+1))
    col_new_names.append('tooth count #{:d}'.format(i+1))
    col_renames[cols_to_keep[-1]] = col_new_names[-1]
    col_retypes[col_new_names[-1]] = 'Int32'
    col_retypes2[col_new_names[-1]] = 'category'
for i in range(30):
    if i != 14 and i != 15: # OHX16CTC and OHX17CTC are not columns in the data
        cols_to_keep.append('OHX{:02d}CTC'.format(i+2))
        col_new_names.append('coronal caries: tooth count #{:d}'.format(i+2))
        col_renames[cols_to_keep[-1]] = col_new_names[-1]
        col_retypes[col_new_names[-1]] = 'category'
cols_to_keep.append('cohort')

nhanes_dentition_df = pd.DataFrame()
for file, cohort in zip(file_exts, cohorts):
    df = pd.read_sas(file)
    df['cohort'] = cohort
    nhanes_dentition_df = nhanes_dentition_df.append(df[cols_to_keep])


for i in range(30):
    if i != 14 and i != 15: # OHX16CTC and OHX17CTC are not columns in the data
        col = 'OHX{:02d}CTC'.format(i+2)
        nhanes_dentition_df[col] = nhanes_dentition_df[col].apply(
            lambda x: x.decode('utf-8'))

# Rename columns    
nhanes_dentition_df = nhanes_dentition_df.rename(columns=col_renames)
nhanes_dentition_df = nhanes_dentition_df.astype(col_retypes)

display(Markdown(nhanes_dentition_df.head().to_markdown(index=False)))
nhanes_dentition_df.to_pickle('./nhanes_dentition_dataframe.pkl')

# ### c

demo_size = nhanes_demo_df.shape[0]
dent_size = nhanes_dentition_df.shape[0]

display(Markdown("Demographic dataset has %i cases"%(demo_size)))
display(Markdown("Dentition dataset has %i cases"%(dent_size)))