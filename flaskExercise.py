from flask import Flask, render_template, request, redirect
from scrapper import scrapJobs
app = Flask('superScraper')

db = {}

@app.route("/")
def home():
    return render_template("potato.html")

@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = scrapJobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template('report.html',
                           resultNumber=len(jobs),
                           searching_by=word)

app.run(host = 'localhost')
