# -*- coding: UTF-8 -*-
import time
import csv

UserNb = 943
FilmNb = 1682

start = time.time()

userIDFilmID = [ [None] * FilmNb for i in range(UserNb)]
head = ['film ' + str(i) for i in range(1,FilmNb+1)]

print '===================='
print 'Init Matrix Finished'
print str(int((time.time() - start) * 1000)) + 'ms'

with open('u.data', 'rb') as data:
    data_reader = csv.reader(data, delimiter='\t')
    for item in data_reader: 
    	userIDFilmID[int(item[0])-1][int(item[1])-1] = int(item[2])

data.close()
print '===================='
print 'Generate Matrix userIDFilmID finished'
print str(int((time.time() - start) * 1000)) + 'ms'


with open('ratings_film.csv','wb') as user_drop:
    user_writer = csv.writer(user_drop, delimiter=',')
    user_writer.writerow(head)
    for user in userIDFilmID :
        user_writer.writerow(user)

user_drop.close()
print '===================='
print 'Write in csv finished'
print str(int((time.time() - start) * 1000)) + 'ms'


