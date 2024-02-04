import pandas
import sys
from pathlib import Path

sn = []

for path in Path('veg_spreadsheet').rglob('*.2017*'):
    #print("SPREADSHEET NAME: "+str(path))
    site_name = str(path).split(".")
    #print(site_name[2])
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
    #print("Stem and crown diameter get average size:")
    if (index-nan) != 0 and site_name[2] not in sn:
        #print(str(site_name[2]))
        print(str(int(diameter_total/(index-nan))))
        sn.append(site_name[2])
        #print(sn)

#print("#####")
#print(diameter_total)
#print(index)
#print(nan)


