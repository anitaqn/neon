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
   
    height = 0

    df = pandas.read_csv(path,usecols=["measurementHeight"])
    for index, row in df.iterrows():
        if str(row) != "nan":
            if float(row) > height:
                height = float(row)
    print("tallest height")
    print(height)
