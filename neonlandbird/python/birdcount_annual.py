import pandas
import sys
import os
from pathlib import Path
import shutil 

sites=0
for path in Path('spreadsheet').rglob('*.2017-06*'):
    
    counts = 0
    sites = sites+1
    family_list = []
    
    #print("["+str(sites)+"]SPREADSHEET NAME: "+str(path))
    site_name = str(path).split(".")
    #print(site_name[2])
    df = pandas.read_csv(path,usecols=["pointCountMinute","family"])
    sorted_df = df.sort_values(by=["family"], ascending=True)
    
    for index, row in sorted_df.iterrows():
        convert = row.to_string(index=False).split()
        counts=counts+int(convert[0])
    #print(str(site_name[2]))
    print(str(counts))

