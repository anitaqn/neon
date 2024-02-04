import pandas
import sys
from pathlib import Path

for path in Path('plant_spreadsheet').rglob('*.csv'):
    print("SPREADSHEET NAME: "+str(path))
    plant=[]
    df = pandas.read_csv(path,usecols=["taxonID"])
    sorted_df = df.sort_values(by=["taxonID"], ascending=True)
    
    for index, row in sorted_df.iterrows():
        convert = row.to_string(index=False).split()
        if convert[0] not in plant:
            plant.append(convert[0])
    print("name of plant(taxonID):")
    print(plant)
