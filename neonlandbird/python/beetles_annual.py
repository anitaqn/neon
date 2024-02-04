import pandas
import sys
from pathlib import Path

#Definition for strippping whitespace
def replace(csv_file, toreplace, replaced):
    dataframe = pandas.read_csv(csv_file)  
   
    # using the replace() method
    dataframe.replace(to_replace = toreplace, value = replaced, inplace = True)

    # writing  the dataframe to another csv file
    new_csv_file = str(csv_file)+"_replaced1"
    dataframe.to_csv(new_csv_file, index = False)

sites = 0

for path in Path('beetles_spreadsheet').rglob('*.csv'):
    #print("SPREADSHEET NAME: "+str(path))
    site_name = str(path).split(".")

    dataframe = pandas.read_csv(path)
    dataframe.replace(to_replace="G. M. Miller", value="G.M.Miller", inplace = True)
    dataframe.replace(to_replace="Lowe and Norris", value="LoweandNorris", inplace = True)
    dataframe.replace(to_replace="Wright and Lowe", value="WrightandLowe", inplace = True)
    dataframe.replace(to_replace="Will and Liebherr", value="WillandLiebherr", inplace = True)
    dataframe.replace(to_replace="Van Dyke", value="VanDyke", inplace = True)
    dataframe.replace(to_replace="Tilley and Mahoney", value="TilleyandMahoney", inplace = True)
    dataframe.replace(to_replace="Sokolov and Carlton", value="SokolovandCarlton", inplace = True)
    dataframe.replace(to_replace="Temminck and Schlegel in Von Siebold", value="TemminckandSchlegelinVonSiebold", inplace = True)
    dataframe.replace(to_replace="De Vis", value="DeVis", inplace = True)
    dataframe.replace(to_replace="Audubon and Bachman", value="AudubonandBachman", inplace = True)
    dataframe.replace(to_replace="Bosc and Daudin in Sonnini and Latreille", value="BoscandDaudininSonniniandLatreille", inplace = True)
    dataframe.replace(to_replace="Ball and Negre", value="BallandNegre", inplace = True)
    dataframe.replace(to_replace="Anderson and Rand", value="AndersonandRand", inplace = True)
    dataframe.replace(to_replace="Lowe and Wright", value="LoweandWright", inplace = True)
    dataframe.replace(to_replace="Jockusch; Wake and Yanev", value="Jockusch;WakeandYanev", inplace = True)
    dataframe.replace(to_replace="Bosc and Daudin", value="BoscandDaudin", inplace = True)
    dataframe.replace(to_replace="Good and Wake", value="GoodandWake", inplace = True)
    dataframe.replace(to_replace="Phelan and Brattstrom", value="PhelanandBrattstrom", inplace = True)
    dataframe.replace(to_replace="Dumeril and Bibron", value="DumerilandBibron", inplace = True)
    dataframe.replace(to_replace="Highton and Peabody", value="HightonandPeabody", inplace = True)
    dataframe.replace(to_replace="Messer and Raber", value="MesserandRaber", inplace = True)
    dataframe.replace(to_replace="Palisot de Beauvois", value="PalisotdeBeauvois", inplace = True)
    dataframe.replace(to_replace="Fischer von Waldheim", value="FischervonWaldeim", inplace = True)
    dataframe.replace(to_replace="Gemminger and Harold", value="GemmingerandHarold", inplace = True)
    dataframe.replace(to_replace="Lowe and Zweifel", value="LoweandZweifel", inplace = True)
    dataframe.replace(to_replace="Baird and Girard", value="BairdandGirard", inplace = True)
    dataframe.replace(to_replace="Say in James", value="SayinJames", inplace = True)
    dataframe.replace(to_replace="Shpeley, Hunting and Ball", value="ShpeleyHuntingandBall",inplace = True)
    dataframe.replace(to_replace="Jameson; Makey and Richmond", value="JamesonMakeyandRichmond", inplace = True)
    new_csv_file = str(path)+"_replaced"
    dataframe.to_csv(new_csv_file, index = False)

    counts = 0
    sites = sites+1
    family_list = []
    new_path = str(path)+"_replaced"

    df = pandas.read_csv(new_path,usecols=["individualCount","scientificNameAuthorship"])
    sorted_df = df.sort_values(by=["scientificNameAuthorship"], ascending=True)
    
    for index, row in sorted_df.iterrows():
        convert = row.to_string(index=False).split()
        #print(convert[0])
        #print(convert[1])
        if str(convert[0]) != "NaN" and str(convert[0]) != "nan":
            counts = counts+float(convert[1])
    print(str(counts))
    print(str(site_name[2]))

