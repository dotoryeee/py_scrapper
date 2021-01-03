from flask import Flask, render_template, request

app = Flask('superScraper')

@app.route("/")
def home():
    return render_template("potato.html")

@app.route('/report')
def report():
    word = request.args.get('word')
    return render_template('report.html', searching_by=word)

app.run(host = 'localhost')
