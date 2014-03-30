import csv

jobs = {}

with open ('u.user','rb') as user_file:
    user_reader = csv.reader(user_file, delimiter='|')
    for user in user_reader:
        job = str(user[3])
        if job in jobs.keys():
            jobs[job] += 1
        else:
            jobs[job] = 0

with open ('jobs_repartition.csv', 'wb') as drop_file:
    repartition_writer = csv.writer( drop_file, delimiter =',')
    for key in jobs.keys():
        row = [ key, jobs[key] ]
        repartition_writer.writerow( row )
