# Importing Libraries
import pandas as pd
import numpy as np
import argparse
#import matplotlib.pyplot as plt
#import seaborn as sns
from IPython.display import display

df = pd.read_csv('owid-covid-data.csv')
#display(df)

# create new month column
df['month'] = pd.DatetimeIndex(df['date']).month
df['year'] = pd.DatetimeIndex(df['date']).year

# extract variables requested (data in year 2020)
variables = ['location','month','total_cases','new_cases','total_deaths','new_deaths']
df_a1 = df.loc[df['year'] == 2020, variables]

# group the data by month and location
df_a1_grouped = df_a1.groupby(['location', 'month'])

# input function to aggregate data
df_a1_sum = df_a1_grouped[['new_cases', 'new_deaths']].sum()
df_a1_max = df_a1_grouped[['total_cases', 'total_deaths']].max()


df_a1_grouped = df_a1_sum.merge(df_a1_max, on=['location', 'month'], how='left')
#display(df_a1_grouped)

# continuing to Question 2 of Task 1
# Calculate case fatality rate from total deaths and total cases
df_a1_grouped['case_fatality_rate'] = df_a1_grouped['new_deaths'] / df_a1_grouped['new_cases']

# reindex and make the dataframe into correct order
df_a1_final = df_a1_grouped.reindex(columns = ['case_fatality_rate', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths'])

print(df_a1_final.head(5))
df_a1_final.to_csv('owid-covid-data-2020-monthly.csv') 