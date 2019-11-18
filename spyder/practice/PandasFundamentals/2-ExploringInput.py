import pandas as pd
import numpy as np
import os

#Read the csv using pandas
CSV_PATH = os.path.join(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master","artwork_data.csv")

#Read just 5 rows from the file

fiveRows_df = pd.read_csv(CSV_PATH,nrows=5)

#To take a specific column as index from the data itself

fiveRows_with_inbuild_index_df= pd.read_csv(CSV_PATH,nrows=5,index_col="id")

#limit number of columns

fiverows_twocolumns_df = pd.read_csv(CSV_PATH,nrows=5,index_col="id",usecols=["id","artist"])

"""
can use index instead of names but not amix
"""

COL_TO_USE = ["id","artist","title","medium","year","acquisitionYear","height","width","units"]

#proper data nad entire data

entiredata_df = pd.read_csv(CSV_PATH,index_col="id",usecols=COL_TO_USE)

"""
Save for later
One of the best ways to save is to use pickle if you are only interatcing with the data in python
"""

entiredata_df.to_pickle(os.path.join(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master","artwork_data.pickle"))