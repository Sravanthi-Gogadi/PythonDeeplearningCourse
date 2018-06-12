from bs4 import BeautifulSoup
import urllib.request
import csv

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
print(soup.find('title').string)
result_list = soup.findAll('a')

for i in result_list:
    link = i.get('href')
    print(link)

result_table = soup.findAll('table', {'class': 'wikitable sortable plainrowheaders'})
for tr in result_table:
    table_data = tr.findAll('td')
    table_head = tr.findAll('th')
    print(table_data, table_head)



table = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})
headers = [th.text for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])