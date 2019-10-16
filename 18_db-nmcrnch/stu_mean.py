#Elizabeth Doss
#SoftDev 1 pd1 
#K18 -- Average
#2019-10-14

import sqlite3
import statistics

db = sqlite3.connect('discobandit.db')
c = db.cursor()
#SELECTS FROM database
q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
#collects all values
data = c.execute(q).fetchall()

#create a dictionary of names and grades
id_name = dict()
id_grades = dict()
#average the grades
for row in data:
    id_name.update({row[1]: row[0]})
    if id_grades.get(row[1]) == None :
        id_grades.update({row[1]: [row[2]]})
    else:
        id_grades.update({row[1]: id_grades.get(row[1]) + [row[2]]})

#print in column form
for key in id_name:
    print("student: {}\t ID: {}\t AVG: {}".format(id_name.get(key), key, statistics.mean(id_grades.get(key))))

#creates table stu_avg
command = "CREATE TABLE IF NOT EXISTS stu_avg(id INTEGER, avg INTEGER)"
c.execute(command)

#print statements to check
#print(id_name)
#print(id_grades)

#populates the new table with ids and averages
for key in id_grades:
    command = "INSERT INTO stu_avg VALUES(" + str(key) + "," + str(statistics.mean(id_grades.get(key))) +  ")"
    print(command)
    c.execute(command)

db.commit() #save changes
db.close()  #close database
