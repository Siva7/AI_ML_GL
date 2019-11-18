import numpy as np
import pandas as pd
import os
import json

"""
Pandas donot havea direct way to read all the contents in a directory 
Hence we use python to fill in the gap

pd.DataFramee.from_*
api helps in creating DataFrame from memory
"""

"""
pd.DataFrame.from_reccords
    This expects a record which is tuple 
    each tuple is considered a record

"""

records = [("Coffee","5"),
           ("Tea","10")]

df_from_mem = pd.DataFrame.from_records(records)

""" Adding custom columns"""
df_from_mem_withcolumn_names = pd.DataFrame.from_records(records,columns=["Drink","Cost"]) 

"""
Read contents from the folder 
"""
list_of_fields = ["id","all_artists","title","medium","width","height"]

def read_json_get_tuple(file_location,list_of_fileds):
    with open(file_location) as file:
        json_content = json.load(file)
    return tuple([json_content[x] for x in list_of_fields])

dirPath,dirName,fileNames=next(os.walk(r"D:\IT\SelfTut\PluralSight- Pandas Fundamentals\pandas-fundamentals\02\demos\demos\collection-master\artworks\a\000"))

tuples_list = [read_json_get_tuple(os.path.join(dirPath,filename),list_of_fields) for filename in fileNames]

df_from_json_files = pd.DataFrame.from_records(tuples_list,columns=list_of_fields,index="id")
        
