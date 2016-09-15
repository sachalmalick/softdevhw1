import random

f = open('occupations.csv', 'r')
lfile = f.readlines() #list of occupations


tmp = 0
L=[]
for row in lfile[1:-1]:
    num = int(10 * float(row[row.rfind(',')+1:]))
    start = tmp
    tmp = num + start
    #print "start is" + str(start) + "end is" + str(start + num)
    L.append([start, tmp, row[:row.rfind(',')]])

#print L

def chooser():
    rand = int(random.random() * 1000)
    for row in L:
        if rand > row[0] and rand < row[1]:
            return row[2]

print chooser()
        
    
