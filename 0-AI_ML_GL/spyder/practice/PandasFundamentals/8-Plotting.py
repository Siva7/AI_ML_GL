import numpy as np
import pandas as pd
import os
#Read the csv using pandas
CSV_PATH = os.path.join(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master","artwork_data.csv")

COL_TO_USE = ["id","artist","title","medium","year","acquisitionYear","height","width","units"]

input_df = pd.read_csv(CSV_PATH,usecols=COL_TO_USE,index_col="id")


small_df = input_df.iloc[49980:50019,:].copy()


"""
pandas plot is wrapper around the matplotlib library
"""

small_df.plot()

"""
plot how many artwors are auired evry year
"""

grouped_by_year = input_df.groupby('acquisitionYear').size().plot() 

