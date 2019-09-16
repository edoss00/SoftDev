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

#added key value pairs to dictionary
occupations = {}
fNewList = fNewList[1:-2]
for a in fNewList:
    occupations[float(a[1])] = a[0]

print(occupations)

#generate random number
randNum = random.randint(0,998) / 10.0
print(randNum)

#iterate and subtract through list until number is less than or equal to 0
iterator = 0
subtracter = randNum
while (subtracter > 0):
    item = float(fNewList[iterator][1])
    subtracter = subtracter - item
    iterator += 1

#print result
print(fNewList[iterator-1][0])
