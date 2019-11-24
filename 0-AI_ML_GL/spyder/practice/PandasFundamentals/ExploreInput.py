import numpy as np
import pandas as pd

np_array = np.random.rand(3)
pd_series = pd.Series(np.random.rand(3))

pd_dataFrame = pd.DataFrame(np.random.rand(3,2))

"""
Index is assigned by default we can override it as well
"""

pd_series_with_index = pd.Series(np.random.rand(3),index=["first","second","third"])

"""
can use both the custom index and the number index to refer to items
"""

print(pd_series_with_index["first"])
print(pd_series_with_index[0])

pd_series_with_index
"""
first     0.176973
second    0.666953
third     0.370319
dtype: float64
"""
pd_series_with_index.index
"""
 Index(['first', 'second', 'third'], dtype='object')
"""

pd_dataFrame.columns
"""
RangeIndex(start=0, stop=2, step=1)
"""
pd_dataFrame
"""
          0         1
0  0.285770  0.793492
1  0.087973  0.861112
2  0.741682  0.679179
"""
pd_dataFrame.columns = ["first","second"]
pd_dataFrame

pd_series_from_df = pd_dataFrame["first"]
pd_series_from_df
"""
0    0.285770
1    0.087973
2    0.741682
Name: first, dtype: float64
"""

