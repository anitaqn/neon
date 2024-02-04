import pandas
import sys
from pathlib import Path


def isnumber(x):
    try:
        float(x)
        return True
    except:
        return False

for path in Path('vegetation_spreadsheet').rglob('*.csv'):
    print("SPREADSHEET NAME: "+str(path))
   
    diameter = 0
    diameter_total = 0
    nan = 0

    df = pandas.read_csv(path,usecols=["stemDiameter"])
    #print(df)
    for index, row in df.iterrows():
        convert = row.to_string(index=False).split()
        #print(convert[0])
        if convert[0] != "NaN":
            diameter_total = float(convert[0]) + diameter_total
        else:
            nan = nan+1
    print("#####")
    print(diameter_total)
    print(index)
    print(nan)
    print("Stem and crown diameter get average size:")
    if (index-nan) != 0: 
        print(int(diameter_total/(index-nan)))
