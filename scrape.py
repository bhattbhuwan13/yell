import webbrowser as wb
import requests,lxml
from bs4 import BeautifulSoup
import pandas as pd
import sys
import re
import requests.exceptions

# opening the site
page = requests.get('https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=681700612&keywords=accountants&location=London')

# Create a BeautifulSoup object
print page
soup = BeautifulSoup(page.text, 'html.parser')
print soup.prettify()
