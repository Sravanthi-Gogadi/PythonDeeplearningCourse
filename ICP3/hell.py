import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from tabulate import tabulate

res = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
soup = BeautifulSoup(res,'lxml')
table = soup.find_all('table')[1]
df = pd.read_html(str(table),header=0)
print( tabulate(df[0], headers='keys', tablefmt='psql') )