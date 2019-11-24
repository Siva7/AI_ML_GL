import numpy as np
import pandas as pd
import os
#Read the csv using pandas
CSV_PATH = os.path.join(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master","artwork_data.csv")

COL_TO_USE = ["id","artist","title","medium","year","acquisitionYear","height","width","units"]

input_df = pd.read_csv(CSV_PATH,usecols=COL_TO_USE,index_col="id")

"""
lables are what is in pandas index object

loc = 
df.loc[1099,'artist']
df.loc[df['artist'] == 'Bacon, Francis',:]

df.iloc[100:300,0,1,4]
"""

input_df.loc[1035,'artist']
"""Blake, Robert"""

input_df.iloc[0,0]
"""Blake, Robert"""
input_df.iloc[0:2,0:2]
"""
             artist                                              title
id                                                                    
1035  Blake, Robert  A Figure Bowing before a Seated Old Man with h...
1036  Blake, Robert  Two Drawings of Frightened Figures, Probably f...
"""

"""Value of highest width """

#this fails as data has strings
input_df['height'].sort_values().head()

#doesnt work as it has string 
pd.to_numeric(input_df['height'])


"""We ask pandas to ignore conversion errors"""
numeric_height_series=pd.to_numeric(input_df['height'],errors='coerce')
numeric_height_series.max()


""" Update our dataframe """
input_df.loc[:,'width'] = pd.to_numeric(input_df['width'],errors='coerce')

input_df.loc[:,'height'] = pd.to_numeric(input_df['height'],errors='coerce')

max_height = input_df['height'].sort_values().head()

max_width = input_df['width'].sort_values().head()

area_series = input_df['height'] * input_df['width']


"""
Add a new column with assign

input_df = input_df.assign(area=area_series)
or as below
"""
input_df['area'] = area_series

max_area=input_df['area'].max()

index_of_max_area = input_df['area'].idxmax()

max_area_record = input_df.loc[index_of_max_area,:]