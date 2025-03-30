import csv
# file = open('Highscore.csv', 'r')
# fileReader = csv.reader(file, delimiter = ',')
mylist = []
# for row in fileReader:
#     score = row[0]
#     name=row[1]
#     score=int(score)
#     newRow=[score,name]
#     mylist.append(newRow)

#file.close()
file = open('Highscore.csv', 'a', newline='')
fileWriter = csv.writer(file, delimiter = ',')
mylist.append(100)
mylist.append('silvia')
fileWriter.writerow(mylist)
file.close()
