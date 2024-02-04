import shutil
from pathlib import Path

for path in Path('bird_full').rglob('*.csv'):
    #print(path.name)
    if "brd_countdata" in path.name:
       #print(path)
        shutil.copy(path,"bird_spreadsheet")
