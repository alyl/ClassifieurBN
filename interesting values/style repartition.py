import csv

styles = [0]*19
matching = [ 'unknown', 'Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime',
             'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
counter = [None]*1682


with open ('u.item','rb') as movie_file:
    movie_reader = csv.reader(movie_file, delimiter='|')
    k = 0
    for movie in movie_reader:
        movie = movie[-19:]
        i = 0
        j = 0
        for i in range(19):
            styles[i] += int(movie[i])
            j += int(movie[i])
        counter[k] = j
        k += 1

counter_dict = {}

for item in counter:
    if item in counter_dict.keys():
        counter_dict[item] += 1
    else:
        counter_dict[item] = 1

with open ('styles_repartition.csv', 'wb') as drop_file:
    repartition_writer = csv.writer( drop_file, delimiter =',')
    for i in range(19):
        row = [ matching[i], styles[i] ]
        repartition_writer.writerow(row)


with open ('number_of_styles_per_movie.csv', 'wb') as drop_file:
    repartition_writer = csv.writer( drop_file, delimiter =',')
    for key in counter_dict.keys():
        row = [ key, counter_dict[key] ]
        repartition_writer.writerow( row )
