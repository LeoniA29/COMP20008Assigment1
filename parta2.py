# Importing Libraries
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

# read new csv data
df_scatter = pd.read_csv('owid-covid-data-2020-monthly.csv')

# read old csv data for list of locations in which continents
df_continent = pd.read_csv('owid-covid-data.csv')
df_continent['year'] = pd.DatetimeIndex(df_continent['date']).year

variables = ['continent','location']
df_continent = df_continent.loc[df_continent['year'] == 2020, variables]
df_continent = df_continent.drop_duplicates()

# make a scatter plot of case fatality rate and confirmed new cases by locations in year 2020
# first locate necessary data of each location
df_scatter_a = df_scatter.loc[df_scatter['month'] == 12, ['location','case_fatality_rate', 'new_cases']]
df_scatter_a = df_scatter_a.merge(df_continent, on='location', how='left')    # merge with continent dataframe


# making subplots
fig, ax = plt.subplots()

# colors dictionary to identify which location in continents
colors = {'Asia':'red', 'Europe':'green', 'Africa':'blue', 'North America':'yellow', 
          'South America':'cyan', 'Oceania':'magenta', np.nan:'black'}

grouped = df_scatter_a.groupby('continent') # group dataframe by continents
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='new_cases', y='case_fatality_rate', label=key, color=colors[key])
                
# some arguments for the overall plot readability
#plt.ylim(0,0.08)          # use these ranges for clarity in viewing plot
#plt.xlim(-0.1e7,1.5e7)    # use these ranges for clarity in viewing plot
plt.xlabel("Total Confirmed New Cases")
plt.ylabel("Case Fatality Rate")
plt.title("Confirmed Cases vs Case Fatality Rate \n by Each Location in 2020")
plt.grid(True)
plt.legend()

#plt.show()
plt.savefig('scatter-a.png')

# PLOT B
# same scatter plot as the first question, but the x-axis is changed to a log scale

# Code sourced from : https://www.codegrepper.com/code-examples/python/interquartile+range+pandas
"""def mod_outlier(df):
        df1 = df.copy()
        df = df._get_numeric_data()


        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 -(1.5 * iqr) 
        upper_bound = q3 +(1.5 * iqr)


        for col in col_vals:
            for i in range(0,len(df[col])):
                if df[col][i] < lower_bound[col]:            
                    df[col][i] = lower_bound[col]

                if df[col][i] > upper_bound[col]:            
                    df[col][i] = upper_bound[col]    


        for col in col_vals:
            df1[col] = df[col]

        return(df1)
"""

# copy previous dataframe
df_scatter_b = df_scatter_a.copy()

# plot with new log data
# making subplots
fig, ax = plt.subplots()

#remove outliers
#mod_outlier(grouped_b)
#display(mod_outlier)

grouped_b = df_scatter_b.groupby('continent') # group dataframe by continents
for key, group in grouped_b:
    group.plot(ax=ax, kind='scatter', x='new_cases', y='case_fatality_rate', label=key, color=colors[key])

# apply log to the x-axis (confirmed new cases)
plt.xscale('log') 

# some arguments for the overall plot readability
plt.xlabel("Total Confirmed New Cases")
plt.ylabel("Case Fatality Rate")
plt.title("Confirmed Cases (Log Scale) \n vs Case Fatality Rate by Each Location in 2020")
plt.grid(True)
plt.legend()

#plt.show()
plt.savefig('scatter-b.png')