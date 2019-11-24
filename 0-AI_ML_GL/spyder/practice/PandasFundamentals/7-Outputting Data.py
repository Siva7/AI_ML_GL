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

small_df.to_excel("path",index=False,columns=['artist','title','year'])

"""
multiple worksheet
"""

writer= pd.ExcelWriter('multiple_sheets.xlsx',engine='xlsxwriter')
small_df.to_excel(writer,sheet_name="Preview",index=False)
input_df.to_excel(writer,sheet_name="Comlpete",index=False)
writer.save()

"""
conditional formatting
"""
artists_count = small_df['artists'].value_counts()
artists_count.head()

writer= pd.ExcelWriter('colors.xlsx',engine='xlsxwriter')
artists_count.to_excel(writer,sheet_name="color")
sheet =writer.sheet['Artist Count']


...
"""to sql ""
small_df.to_sql('db',connection)
small_df.to_json(locaiton,orient=table)
"""

