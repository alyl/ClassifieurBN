

with open('test.txt','w') as drop:
    for i in range(1682):
        row = "@attribute 'film " + str(i+1) + "' {1,2,3,4,5}\n"
        drop.write(row)

with open('test2.txt','w') as drop2:
    row = '@attribute userID {'
    for i in range(943):
        row += ',' + str(i+1)
    row += '}'
    drop2.write(row)
