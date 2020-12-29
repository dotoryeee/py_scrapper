from indeed import scrapJobs as getIndeedJobs
from so import scrapJobs as getSOJobs

indeed_jobs = getIndeedJobs()
so_jobs = getSOJobs()

jobs = indeed_jobs + so_jobs

