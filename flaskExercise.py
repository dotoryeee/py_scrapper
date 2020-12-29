from flask import Flask

app = Flask('superScraper')

@app.route("/")
def home():
    return 'hello'

@app.route('/contact')
def potato():
    return 'contact page'

app.run(host = 'localhost')
