import csv
import time
import os

start = time.time()

matching = [ 'unknown', 'Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime',
             'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

jobs = {}
style_representation = [0]*19
user_job = [None]*943
movie_style = [None]*1682
user_favorite_styles = [{} for i in range(943)]
favorite_styles_per_job = [{} for i in range(21)]
favorite_style_per_job = [None for i in range(21)]
all_rates_per_job = [0 for i in range(21)]

# parsing u.user to get the list of jobs (job_list) and the match between jobs and users (user_job)

print 'variables initialized, time = ' + str(int((time.time() - start)*1000)) + 'ms'


with open ('u.user','rb') as user_file:
    user_reader = csv.reader(user_file, delimiter='|')
    for user in user_reader:
        job = str(user[3])
        if job not in jobs.keys():
            jobs[job] = None
        user_job[int(user[0])-1] = job
        
job_list = jobs.keys()

print 'users file parsed, time = ' + str(int((time.time() - start)*1000)) + 'ms'

# parsing u.movie to get the match between movies and styles (movie_style)

with open ('u.item','rb') as movie_file:
    movie_reader = csv.reader(movie_file, delimiter='|')
    for movie in movie_reader:
        movie_id = int(movie[0])-1
        movie = movie[-19:]
        local_movie_style = []
        i = 0
        for item in movie:
            if int(item) == 1:
                local_movie_style.append(i)
            i += 1
        movie_style[movie_id] = []
        for item in local_movie_style:
            movie_style[movie_id].append( matching[item])

for i in range(1682):
    for style in movie_style[i]:
        index = matching.index(style)
        style_representation[index] += 1

print style_representation    

print 'movies file parsed, time = ' + str(int((time.time() - start)*1000)) + 'ms'

# parsing u.data to count the number of ratings for each user for each style ( user_favorite_styles ) and the number of ratings for each job total ( all_rates_per_job)

with open ('u.data', 'rb') as data_file:
    
    data_reader = csv.reader(data_file, delimiter ='\t')
    for data in data_reader:
        styles = movie_style[int(data[1])-1]
        user_id = int(data[0])-1
        job = user_job[user_id]
        dic = user_favorite_styles[user_id]
        for style in styles:
            all_rates_per_job[job_list.index(job)] += 1
            if style in dic.keys():
                dic[style] += 1
            else:
                dic[style] = 1
        user_favorite_styles[user_id] = dic
                        
print 'data file parsed, time = ' + str(int((time.time() - start)*1000)) + 'ms'

# calculating the number of ratings for each job for each style ( favorite_styles_per_job )

for i in range(943):
    job = user_job[i]
    dic = user_favorite_styles[i]
    for key in dic.keys():
        if key in favorite_styles_per_job[job_list.index(job)].keys():
            favorite_styles_per_job[job_list.index(job)][key] += dic[key]
        else:
            favorite_styles_per_job[job_list.index(job)][key] = dic[key]

for i in range(21):
    for key in favorite_styles_per_job[i].keys():
        favorite_styles_per_job[i][key] = float(favorite_styles_per_job[i][key]) / float (style_representation[matching.index(key)])
    total = 0
    for key in favorite_styles_per_job[i].keys():
        total += favorite_styles_per_job[i][key]
    for key in favorite_styles_per_job[i].keys():
        favorite_styles_per_job[i][key] = round(100 * favorite_styles_per_job[i][key] / total, 2)                                                                               
    

print 'job\'s most rated styles calculated, time = ' + str(int((time.time() - start)*1000)) + 'ms'

print favorite_styles_per_job[0]

test = float(0)
for key in favorite_styles_per_job[0].keys():
    test += favorite_styles_per_job[0][key]

# deducing the most rated style for each job ( favorite_style_per_job ) 

for i in range(21):
    my_max = [0,None,0,None]
    for style in favorite_styles_per_job[i].keys():
        if favorite_styles_per_job[i][style] > my_max[0]:
            my_max[0] = favorite_styles_per_job[i][style]
            my_max[1] = style
        elif favorite_styles_per_job[i][style] > my_max[2]:
            my_max[2] = favorite_styles_per_job[i][style]
            my_max[3] = style
            
    favorite_style_per_job[i] = my_max

print 'maxima calculated, time = ' + str(int((time.time() - start)*1000)) + 'ms :'

for i in range(21):
    print job_list[i] + " " + str(favorite_style_per_job[i][0]) + " " + favorite_style_per_job[i][1] + " " + str(favorite_style_per_job[i][2]) + " " + favorite_style_per_job[i][3]

#for i in range(21):
#    print job_list[i] + 's rate ' + favorite_style_per_job[i][1] + ' movies the most with ' + str(favorite_style_per_job[i][0]) + ' ratings.'

# dumping it into most_rated_styles.csv

with open ('most_rated_styles.csv', 'wb') as drop_file:
    repartition_writer = csv.writer( drop_file, delimiter =',')
    for i in range(21):
        row = [ job_list[i], favorite_style_per_job[i][0], favorite_style_per_job[i][1], favorite_style_per_job[i][2], favorite_style_per_job[i][3]]
        repartition_writer.writerow( row )

print 'data_dropped, time = ' + str(int((time.time() - start)*1000)) + 'ms'
