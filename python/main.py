from indeed import scrapJobs as getIndeedJobs
from so import scrapJobs as getSOJobs
from save import saveToFile

indeed_jobs = getIndeedJobs()
so_jobs = getSOJobs()
jobs = indeed_jobs + so_jobs

saveToFile(jobs)

