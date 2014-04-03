# -*- coding: UTF-8 -*-
import time
import csv

UserNb = 943
TypeNb = 19

start = time.time()

userTypeNote_StarWars = []
userTypeNote_nonStarWars = []
filmType = []
tempData = []
head = ['userID'] + ['Note'] + ['type ' + str(i) for i in range(1,TypeNb+1)] 

print '===================='
print 'Init Matrix Finished'
print str(int((time.time() - start) * 1000)) + 'ms'

with open('u.item', 'rb') as film_data:
    film_reader = csv.reader(film_data, delimiter='|')
    for item in film_reader: 
    	filmType.append(item[5:])

film_data.close()

with open('u.data', 'rb') as data_data:
    data_reader = csv.reader(data_data, delimiter='\t')
    for item in data_reader: 
    	tempData.append (item[0])
    	tempData.append (item[2])
    	tempData += filmType[int(item[1])-1]
        if item[1] == '50': 
    	   userTypeNote_StarWars.append(tempData)
        else:
            userTypeNote_nonStarWars.append(tempData)
    	tempData = []

data_data.close()

with open('user_Type_Note_StarWars.csv','wb') as data_drop :
    data_writer = csv.writer(data_drop, delimiter=',')
    data_writer.writerow(head)
    for item in userTypeNote_StarWars:
    	data_writer.writerow(item)


data_drop.close()


with open('user_Type_Note_NonStarWars.csv','wb') as data2_drop :
    data2_writer = csv.writer(data2_drop, delimiter=',')
    data2_writer.writerow(head)
    for item in userTypeNote_nonStarWars:
        data2_writer.writerow(item)


data2_drop.close()

print '===================='
print 'user_Type_Note.csv  and  user_Type_Note_NonStarWars.csv created '
print str(int((time.time() - start) * 1000)) + 'ms'  
