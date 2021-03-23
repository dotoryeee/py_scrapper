import csv

def saveToFile(jobs):
    file = open('jobs.csv', mode='w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['title','company','location','link'])
    for job in jobs:
        writer.writerow(list(job.values())) #dict -> list 변환
    return
