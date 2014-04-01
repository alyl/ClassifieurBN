# -*- coding: UTF-8 -*-

# we could use this script to find out the most noted films 
# and then we'll test predictions of these films using weka classifier model

# Most noted film : Film 50 is noted 583 times.


# Output 2 files  :  most_noted_film.csv and ratings_job_film_filter_film50.csv


import time
import csv

UserNb = 943
FilmNb = 1682
user_data_filter = []

start = time.time()

filmNoteTimes = [0] * FilmNb
DicFilmsTimes = {}

print 'variables initialized, time = ' + str(int((time.time() - start)*1000)) + 'ms'


with open('u.data', 'rb') as u_data:
    data_reader = csv.reader(u_data, delimiter='\t')
    for item in data_reader: 
    	filmNoteTimes[int(item[1])-1] += 1

u_data.close()
print 'data file parsed, time = ' + str(int((time.time() - start)*1000)) + 'ms'

for i in range(FilmNb):
	if filmNoteTimes[i] in DicFilmsTimes:
		DicFilmsTimes[filmNoteTimes[i]].append(i+1)
	else:
		DicFilmsTimes[filmNoteTimes[i]] = [i+1]

print 'Films Noted Times caculated, time = ' + str(int((time.time() - start)*1000)) + 'ms'

TimesSorted = sorted (DicFilmsTimes, reverse = True)

print 'the most noted film is Film', DicFilmsTimes[TimesSorted[0]]

with open ('most_noted_film.csv', 'wb') as drop_file:
    writer = csv.writer( drop_file, delimiter =',')
    for item in TimesSorted:
        stringTimes = str(item) + ' times'
    	row = [stringTimes] + DicFilmsTimes[item]
        writer.writerow(row)

drop_file.close()
print 'data_dropped, time = ' + str(int((time.time() - start)*1000)) + 'ms'


'''========= filter users : we keep the user who notes Film50 ==========='''

with open('ratings_job_film.csv', 'rb') as data:
    data_reader = csv.reader(data, delimiter=',')

    for item in data_reader:
        # if there's a note for Film 50
        # then we keep this user in our user-data_filter
        if item[50]:
            user_data_filter.append(item)
data.close()

with open ('ratings_job_film_filter_film50.csv', 'wb') as new_file:
    new_writer = csv.writer( new_file, delimiter =',')
    head = ['film ' + str(i) for i in range(1,FilmNb+1)]
    new_writer.writerow(head)
    for item in user_data_filter:
        new_writer.writerow(item)

new_file.close()
print 'ratings_job_film_filter_film50 created, time = ' + str(int((time.time() - start)*1000)) + 'ms'
