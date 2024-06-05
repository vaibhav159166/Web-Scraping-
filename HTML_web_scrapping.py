# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:13:12 2023

@author: Vaibhav Bhorkade

Web Scrapping
HTML page
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(open("C:/datasets/sample_doc.html"),'html.parser')
print(soup)
# It is going to to show all the html contents extracted
soup.text
# It will show only text
soup.contents
# It is going to show all the html contents extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)

# It will show all the rows except first row 
# Now we want to display M.tech which is located in third row and second column
# I need to give [3][2]
table.find_all('tr')[3].find_all('td')[2]
