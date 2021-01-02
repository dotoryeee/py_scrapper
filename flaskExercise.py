from flask import Flask, render_template

app = Flask('superScraper')

@app.route("/")
def home():
    return render_template("potato.html")

app.run(host = 'localhost')
