import numpy as np
import pandas as pd
import os
#Read the csv using pandas
CSV_PATH = os.path.join(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master","artwork_data.csv")

COL_TO_USE = ["id","artist","title","medium","year","acquisitionYear","height","width","units"]

input_df = pd.read_csv(CSV_PATH,usecols=COL_TO_USE,index_col="id")

"""
The below are applied on SeriesGroupBy
Aggregration => regular summirazatoin
Transformation (window) => its like a map with grouped info available
Filtering
"""


"""DataFrameGroupBy object"""

input_df.groupby('artist')
"""
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000226DE6CEA48>
"""
grouped_df=input_df.groupby('artist')

small_df = input_df.iloc[49980:50019,:].copy()
small_group_df = small_df.groupby('artist')

"""
DataFrameGroupBy is a collection of the unique values inthe grouped column to the 
dataframe records that contain that value
""" 

for name,group_df in small_group_df:
    print(name)
    print(group_df)
    break

"""
Find min aqusition year per artist
"""

min_acq_per_artist = small_group_df['acquisitionYear'].min()

"""
fillna functions is used to fill in for nan in data
pd.concat
"""



seriesgroupby=small_df.groupby('artist')['medium']
type(seriesgroupby)
"""
<pandas.core.groupby.generic.SeriesGroupBy object at 0x00000226DEA2B848>
"""

for x,y in seriesgroupby:
    print(x)
    print(y)
    break

"""
small_df.groupby('artist')['medium','title']
would return a DataFrameGroupBy
"""
 
"""
Get min acquisitiondate per artist
"""
seriesgroupby_of_acqYear_grouped_by_artist = small_df.groupby('artist')['acquisitionYear']

series_min_year_per_artist = seriesgroupby_of_acqYear_grouped_by_artist.min()


series_min_year_per_artist = seriesgroupby_of_acqYear_grouped_by_artist.agg(np.min)


"""
Transformation

Append a column "deficite_height" which is max_height_in_group - self_height
grouped on artist

"""
seriesGroupBy_onArtist_height = small_df.groupby('artist')['height']
def diff_with_max_height_transform(series_of_heights):
    numeric_series=pd.to_numeric(series_of_heights,errors='coerce')
    max_height = numeric_series.max()    
    return numeric_series.subtract(max_height)

transform_result = seriesGroupBy_onArtist_height.transform(diff_with_max_height_transform)


small_df_with_height_diff = small_df.copy()

small_df_with_height_diff['deficite_height'] = transform_result


"""
Spit out records only where the tile is repeated 
if the tilte is used only once donot show that record
"""
groupby_onArtist = small_df.groupby('title')
condition = lambda x: len(x.index) > 1
repeated_titles = groupby_onArtist.filter(condition)




"""
