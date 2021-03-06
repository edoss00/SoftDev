#Elizabeth Doss & Yevgeniy Gorbachev (Team Special Disco)
#SoftDev1 pd1
#K10 -- Import/Export Bank
#2020-02-28

"""
Sample Data from grad_results.json
 {
     "Cohort Year": "2001",
     "Cohort Category": "4 Year  June",
     "Demographic": "English Language Learner",
     "# Total Cohort": "10540",
     "# Total Grads": "2791",
     "% of cohort Total Grads": "26.5",
     "# of cohort Total Grads": "992",
     "% of cohort Total Regents": "9",
     "% of grads  Total Regents": "35.5",
     "# of grads  Total Regents": "315",
     "% of cohort  Advanced Regents": "3",
     "% of grads  Advanced Regents": "11.3",
     "# of grads  Advanced Regents": "677",
     "% of cohort  Regents w/o Advanced": "6.4",
     "% of grads  Regents w/o Advanced": "24.3",
     "# of grads  Regents w/o Advanced": "1803",
     "% of cohort Local": "17.1",
     "% of grads Local": "64.6",
     "# Still Enrolled": "3895",
     "% of cohort Still Enrolled": "37",
     "# Dropped Out": "3220",
     "% of cohort Dropped Out": "30.6"
 }

When inserting your own values you can use:
Cohort Year: 2001-2011
Cohort Category: 4 Year  June, 4 Year August, 5 Year  June, 5 Year August, 6 Year
Demographic: English Language Learner, English Language Proficient,
             Not Student with Disability, Student with Disability,
             Asian, Black, Hispanic, White, Female, Male
"""
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # default mongo port is 27017
schools = client['specialdisco'].collection

### Dropout Rates
def findDrop_year(year):
    return schools.find(
        {'Cohort Year':str(year)},
        {'% of cohort Dropped Out':1, '_id':0}
    )
def findDrop_year_dem(year,dem):
    return schools.find(
        {'Cohort Year':str(year),
         'Demographic': dem},
        {'% of cohort Dropped Out':1, '_id':0}
    )
def findDrop_year_cat(year,cat):
    return schools.find(
        {'Cohort Year':str(year),
         'Cohort Category': cat},
        {'% of cohort Dropped Out':1, '_id':0}
    )

### Advanced Regents
def findAdReg_year(year):
    return schools.find(
        {'Cohort Year':str(year)},
        {'% of cohort  Advanced Regents':1, '_id':0}
    )
def findAdReg_year_dem(year,dem):
    return schools.find(
        {'Cohort Year':str(year),
         'Demographic': dem},
        {'% of cohort  Advanced Regents':1, '_id':0}
    )
def findAdReg_year_cat(year,cat):
    return schools.find(
        {'Cohort Year':str(year),
         'Cohort Category': cat},
        {'% of cohort  Advanced Regents':1, '_id':0}
    )

### Mins and Maxs
def findYear_dem_min(dem,min):
    return schools.find(
        {'Demographic': dem,
         '% of cohort Dropped Out': {'$gt': str(min)}},
        {'Cohort Year':1, '_id':0}
    )
def findDrop_enrollmax(max):
    return schools.find(
        {'% of cohort Still Enrolled': {'$lt': str(max)}},
        {'% of cohort Dropped Out':1, '_id':0}
        )

### Prints
def print_results(results):
    for result in results:
        pprint(result)

### Drop Out Tests
# print('Drop Out in 2001')
# print_results(findDrop_year(2001))
print('Drop Out in 2009 for 6 Year')
print_results(findDrop_year_cat(2009,'6 Year'))
# print('Drop Out in 2006 for Male')
# print_results(findDrop_year_dem(2001,'Male'))
#
### Advanced Regents Tests
# print('Advanced Regents in 2011')
# print_results(findAdReg_year(2011))
# print('Advanced Regents in 2001 for 5 Year August')
# print_results(findAdReg_year_cat(2009,'5 Year August'))
print('Advanced Regents in 2003 for Hispanic')
print_results(findAdReg_year_dem(2001,'Hispanic'))
#
### Mins and Maxs Tests
print('Year for Black > 10% Dropped Out')
print_results(findYear_dem_min('Male', 10))
print('Drop Out when Enrollment < 20%')
print_results(findDrop_enrollmax(20))
