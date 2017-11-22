import requests,lxml
from bs4 import BeautifulSoup
import pandas as pd
import sys
import re
import requests.exceptions
# from urllib.parse import urlsplit
from collections import deque

page = requests.get("https://www.linkca.co.uk")
# print page
soup = BeautifulSoup(page.content,"html.parser")

[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
# print visible_text


# Removing extra white space
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in visible_text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
print text

re.findall(r"\+\d{2}\s?0?\d{10}",text)
a = []
a = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",text)
print a


# new_urls = deque(['http://www.themoscowtimes.com/contact_us/'])
# print new_urls
