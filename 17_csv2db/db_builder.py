#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


command = "CREATE TABLE IF NOT EXISTS classData (name TEXT, mark INTEGER, id INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

with open('courses.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         command = "INSERT INTO classData VALUES(" + row['code'] + "," + row['mark'] + "," + row['id'] + ")"
         print(command)
         c.execute(command)
      
#==========================================================

db.commit() #save changes
db.close()  #close database
