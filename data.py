import requests
from google.colab import userdata
import xml.etree.cElementTree as ET
import pandas as pd

url = 'https://openapi.gg.go.kr/ANIMALREGSTUS'

params = {
    ('Key', userdata.get('sampleKey')),
    ('Type','xml'),
    ('plndex',1),
    ('pSize', 100)
}

a = requests.get(url, params)
root = ET.fromstring(a.text)

p=[]
v= {}

for i in root.findall('row'):
  for j in i:
    v[j.tag] = j.text
  p.append(v)

dd = pd.DataFrame(p)
dd
