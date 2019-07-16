#!/usr/bin/env python
# coding: utf-8

# In[25]:


#https://medium.com/fintechexplained/nlp-python-data-extraction-from-social-media-emails-images-documents-web-pages-58d2f148f5f4
#https://textblob.readthedocs.io/en/dev/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://www.datacamp.com/community/tutorials/web-scraping-using-python
#https://stackoverflow.com/questions/8554035/remove-all-javascript-tags-and-style-tags-from-html-with-python-and-the-lxml-mod

from textblob import TextBlob
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import etree

url = 'https://www.foxnews.com/politics/aoc-squad-news-conference-trump-call-go-back-home'

def subjectivity(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())

    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    text = '\n'.join(chunk for chunk in chunks if chunk)

    return TextBlob(text).sentiment.subjectivity
    # return text.encode("utf-8")

print(subjectivity(url))

