import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import os
getlink = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
sourcecode= urllib.request.urlopen(getlink)
#To get the title of the webpage
soup= BeautifulSoup(sourcecode,'html.parser')
# To display every link in the webpage
print(soup.title)
print(soup.findAll('a'))
for link in soup.findAll('a'):
        print(link.get('href'))
result_list = soup.findAll('table', {'class':'wikitable sortable plainrowheaders'})
for tr in result_list:
    s=tr.findAll('td')
    h=tr.findAll('tr')
    print(s)
    print(h)

df=pd.read_html(getlink, attrs={'class': 'wikitable sortable plainrowheaders'})
print(df)

