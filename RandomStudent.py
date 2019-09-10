import random

dict1 = {'A': [1,2,3,4,5],
         'B': [6,7,8,9,10]}


x = random.randint(0,3)
print(x)
print(dict1)

if (x == 0):
    randS = random.randint(0,5)
    print(dict1.get('A',randS))
    
