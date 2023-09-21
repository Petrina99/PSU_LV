import requests
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.3.2017'

response = requests.get(url)

root = ET.fromstring(response.content)

data = []
for child in root:
    row = {}
    for element in child:
        row[element.tag] = element.text
    data.append(row)

df = pd.DataFrame(data)

print(df.tail(3))
new_df = df.sort_values(['vrijednost'])

