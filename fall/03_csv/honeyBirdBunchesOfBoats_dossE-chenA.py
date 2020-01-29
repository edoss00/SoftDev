#Elizabeth Doss
#SoftDev1 pd1
#K6 -- StI/O: Divine your Destiny!
#2019-09-17

import random

#opening file
f = open("occupations.csv","r")

#storing file into large string
fString = f.read()

#splitting string into array with name and percentage as an element
fList = fString.split('\n')

#creating new array with each element as an array with name and percentage
fNewList = []
for s in fList:
    fNewList.append(s.rsplit(',',1))

#parsed list to remove header and total
fNewList = fNewList[1:-2]


#added key value pairs to dictionary
occupations = {}
for a in fNewList:
    occupations[a[0]] = float(a[1])

print(occupations)

#random occupation generator function
def randomOcc():
    r = random.randint(1, 998) / 10.0
    for s in fNewList:
        r -= float(s[1])
        if (r <= 0):
            return s[0]

#tests
for x in range(20):
    print(randomOcc())
