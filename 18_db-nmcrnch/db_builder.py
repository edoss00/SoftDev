#Elizabeth Doss
#SoftDev 1 pd1 
#K17 -- No Trouble
#2019-10-9

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
command = "CREATE TABLE IF NOT EXISTS courses (courses TEXT, mark INTEGER, id INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#creates table for courses
with open('courses.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         command = "INSERT INTO courses VALUES(\"" + row['code'] + "\"," + row['mark'] + "," + row['id'] + ")"
         #print(command)
         c.execute(command)

command = "CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#creates table for students
with open("students.csv", newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row)
         command = "INSERT INTO students VALUES(\"" + row['name'] + "\"," + row['age'] + "," + row['id'] + ")"
         #print(command)
         c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database


#use .header on
#use .mode columns, csv, list, html, insert, live, tabs



