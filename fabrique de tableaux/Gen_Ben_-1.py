import time
import collections
import csv
import os

User = collections.namedtuple(
    'User', ['id', 'age', 'sexe', 'job', 'zip', 'ratings'])


start = time.time()


users = []
notes = [[-1]*1682]*943

with open('u.user', 'rb') as user_file:
    user_reader = csv.reader(user_file, delimiter='|')
    for user in user_reader:
        user[0] = int(user[0])
        user.append({})
        users.append(User._make(user))

user_file.close()
print '===================='
print 'User file parsed'
print str(int((time.time() - start) * 1000)) + 'ms'

with open('u.data', 'rb') as movie_file:
    movie_reader = csv.reader(movie_file, delimiter='\t')
    for movie in movie_reader:
        users[int(movie[0])-1].ratings[int(movie[1])] = int(movie[2])

movie_file.close()
print '===================='
print 'Movie file parsed'
print str(int((time.time() - start) * 1000)) + 'ms'

with open('users.csv','wb') as user_drop:
    user_writer = csv.writer(user_drop, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for user in users :
        user_writer.writerow(user)

user_drop.close()
print '===================='
print 'Users dropped in users.csv'
print str(int((time.time() - start) * 1000)) + 'ms'


truc = [[1,1],[2,2]]
with open('ratings.csv','wb') as rating_drop :
    rating_writer = csv.writer(rating_drop, delimiter=',', quotechar='|', quoting = csv.QUOTE_MINIMAL)
    attr = ['job']
    for i in range(1682):
        attr.append("film " +str(i+1))
    rating_writer.writerow(attr)
    for i in range(943):
        row = [users[i].job]
        for j in range(1682):
            if j+1 in users[i].ratings.keys():
                row.append(users[i].ratings[j+1])
            else:
                row.append(-1)
        rating_writer.writerow(row)
            
rating_drop.close()
print '===================='
print 'Ratings dropped in ratings.csv'
print str(int((time.time() - start) * 1000)) + 'ms'            
    
