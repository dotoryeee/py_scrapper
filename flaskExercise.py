from flask import Flask, render_template, request
from scrapper import scrapJobs
app = Flask('superScraper')

@app.route("/")
def home():
    return render_template("potato.html")

@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = scrapJobs(word)
        print(jobs)
    else:
        return redirect("/")
    return render_template('report.html', searching_by=word)

app.run(host = 'localhost')
