import pandas
import sys
from pathlib import Path

for path in Path('plant_spreadsheet').rglob('*.csv'):
    print("SPREADSHEET NAME: "+str(path))
    family_list=[]
    counts=0
    df = pandas.read_csv(path,usecols=["pointCountMinute","family"])
    sorted_df = df.sort_values(by=["family"], ascending=True)

    for index, row in sorted_df.iterrows():
        convert = row.to_string(index=False).split()
        if convert[1] not in family_list:
            family_list.append(convert[1])
            if counts != 0:
                print(counts)
            print(convert[1])
            counts=0
            counts=counts+int(convert[0])
        else:
            counts=counts+int(convert[0])
