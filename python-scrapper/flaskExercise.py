from flask import Flask, render_template, request, redirect, send_file
from scrapper import scrapJobs
from exporter import saveToFile
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
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = scrapJobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template('report.html',
                           resultNumber=len(jobs),
                           searching_by=word,
                           jobs=jobs)

@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception
        saveToFile(jobs)
        return send_file('jobs.csv')
    except:
        return redirect('/')

app.run(host = 'localhost')
