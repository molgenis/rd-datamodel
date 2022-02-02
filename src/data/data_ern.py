#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-05-05
#' MODIFIED: 2021-10-08
#' PURPOSE: Pull ERN reference table and clean names
#' STATUS: working
#' PACKAGES: requests, bs4/BeautifulSoup, re, csv
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

import requests
from bs4 import BeautifulSoup
import re
import csv

# fetch ERN table
url = 'https://ec.europa.eu/health/ern/networks_en'
page = requests.get(url)
content = BeautifulSoup(page.text, 'html.parser')
table = content.find('table')

# extract data
data = []
for row in table.findAll('tr'):
    data.append({
        'id': re.sub(r'[\s-]+', '_',row.select('td:nth-child(1)')[0].text.strip()).lower(),
        'shortname': row.select('td:nth-child(1)')[0].text.strip(),
        'fullname': re.sub(r'\([^)]*\)', '', row.select('td:nth-child(2)')[0].text.strip()).strip(),
        'factsheet_url': re.sub(
            pattern = 'http:',
            repl = 'https',
            string = row.select('td:nth-child(2) > a:nth-child(1)')[0]['href']
        ),
        'website': re.sub(
            pattern = 'http:',
            repl = 'https:',
            string = row.select('td:nth-child(2) > a:nth-child(2)')[0]['href']
        )
    })

# write
with open('data/ern_metadata.csv', mode='w') as csv_file:
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
        writer.writerow(d)