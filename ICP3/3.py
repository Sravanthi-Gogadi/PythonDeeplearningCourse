from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import csv
# Read the web url into a variable
url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
# use urllib to open the url
res = urllib.request.urlopen(url)
plain_text = res
# Use beautiful soup to get the content of webpage
soup = BeautifulSoup(plain_text, "html.parser")
# Print the title of the web page
print(soup.find('title').string)
# Print all the anchor tags in the webpage
result_list = soup.findAll('a')
# Print the text of href
for i in result_list:
    link = i.get('href')
    print(link)
# Read the table from webpage
result_table = soup.findAll('table', {'class': 'wikitable sortable plainrowheaders'})
for tr in result_table:
    table_data = tr.findAll('td')
    table_head = tr.findAll('th')
# Print td and th
print(table_data, table_head)
# using tabulate to display the pandas dataframe
from tabulate import tabulate
# To display the list of union territories
table = soup.find_all('table')[1]
# using pandas object read the table and assign header
df = pd.read_html(str(table),header=0)
# display the output
print( tabulate(df[0], headers='keys', tablefmt='psql') )
