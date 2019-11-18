import numpy as np
import pandas as pd
import os

"""
Selecting columns
    df["artists"]
    df.artists => donot use this 
    
"""
#Read the csv using pandas
CSV_PATH = os.path.join(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master","artwork_data.csv")

COL_TO_USE = ["id","artist","title","medium","year","acquisitionYear","height","width","units"]

input_df = pd.read_csv(CSV_PATH,usecols=COL_TO_USE,index_col="id")

""" find number of distinct artits in the dataFrame"""
len(pd.unique(input_df["artist"]))

"""how many arts form Bacon, Francis"""

series_with_truefalse= input_df["artist"] == "Bacon, Francis"

input_df["artist"].value_counts()
 """
 Turner, Joseph Mallord William    39389
Jones, George                      1046
Moore, Henry, OM, CH                623
Daniell, William                    612
Beuys, Joseph                       578
 
Allinson, Adrian                      1
Mednikoff, Reuben                     1
Kaufmann, Isidor                      1
Askew, Victor                         1
Pether, Henry                         1
Name: artist, Length: 3336, dtype: int64
"""
artistname_count_series = input_df["artist"].value_counts()

artistname_count_series["Bacon, Francis"]

series_truefalse=dfwith_truefalse.value_counts()
"""
False    69151
True        50
Name: artist, dtype: int64

"""
