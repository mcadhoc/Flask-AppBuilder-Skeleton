from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
app = Flask(__name__)

@app.route("/")
def home():
    return "hi"

@app.route("/index")
def index():
    return render_template('login.html', message='')

@app.route('/login', methods=['GET', 'POST'])
def login():
   message = None
   if request.method == 'GET':
        datafromjs = request
        print(datafromjs)
        # Add Summarization and Bias code here.
        result = "return this"
        resp = make_response('{"response": "'+result+'"}')
        resp.headers['Content-Type'] = "application/json"
        print(resp)
        return resp

if __name__ == "__main__":
    app.run(debug = True)
