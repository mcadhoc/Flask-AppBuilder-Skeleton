from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
app = Flask(__name__)

@app.route("/")
def home():
    return "hi"

@app.route("/index")
def index():
    return render_template('login.html', message='')

url = 'https://www.foxnews.com/politics/aoc-squad-news-conference-trump-call-go-back-home'

@app.route('/login', methods=['GET', 'POST'])
def login():
   message = None
   if request.method == 'GET':
        datafromjs = request
        print(datafromjs)
        # Add Summarization and Bias code here.
        result = subjectivity(url)
        resp = make_response('{"response": "'+str(result)+'"}')
        resp.headers['Content-Type'] = "application/json"
        print(resp)
        return resp

from textblob import TextBlob
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import etree


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

if __name__ == "__main__":
    app.run(debug = True)
