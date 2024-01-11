import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import os
import re

years = list(range(2000,2023))
url_start = "https://www.sports-reference.com/cfb/schools/north-carolina/{}/gamelog/"

if len(os.listdir('records')) == 0:
    for year in years:
        url = url_start.format(year)
        data = requests.get(url)

        with open("records/{}.html".format(year), "w+") as f:
            f.write(data.text)
else:
    print("records file contains html files")

dfs = []
for year in years:
    with open("records/{}.html".format(year)) as f:
        page = f.read()
    
    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="over_header").decompose()
    offense_table = soup.find(id="offense")
    offense = pd.read_html(StringIO(str(offense_table)))[0]["Result"]
    # offense = offense[]
    pattern = r'\((\d+-\d+)\)'
    for o in offense:
        match = re.search(pattern, str(o))
        if match:
            score = match.group(1)
            dfs.append(score)
    
# print(dfs)
df = pd.DataFrame(dfs)
print(df)
df.to_csv('records.csv')