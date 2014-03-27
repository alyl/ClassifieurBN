import time
import collections
import csv


User = collections.namedtuple(
    'User', ['id', 'age', 'sexe', 'job', 'zip', 'ratings'])


start = time.time()

users = []
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
        users[int(movie[0])-1].ratings[int(movie[1])] = float(movie[2])

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
