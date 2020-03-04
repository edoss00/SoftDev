#Elizabeth Doss & Yevgeniy Gorbachev (Team Special Disco)
#SoftDev1 pd1
#K10 -- Import/Export Bank
#2020-02-28
"""
2005 - 2015 Graduation Outcomes
This dataset contains information about different graduation outcomes
from 2001-2011. Information includes Cohort Year, Cohort Category,
Demographic, # and % of grads Advanced Regents, # and % of cohort Still
Enrolled, # and % of cohort Dropped Out, and much more.

The original data was provided in a csv file that we converted
to a JSON file. There is a JSON file available on the page, but it
contains a file that is not easily searchable, so we made our own!
Here is a link to the general download page:
(DOWNLOADING THE JSON DIRECTLY WILL NOT WORK)
https://catalog.data.gov/dataset/regents-exam-results
Here is the link to the csv download page:
https://catalog.data.gov/dataset/regents-exam-results/resource/3152fb23-d46a-4805-91a4-62cd096c945b

This file generates a JSON file and creates a new db used in queries.property
If the JSON does not need to be generated, the user is informed using
main() of what steps to follow
If the json file is already initialized, run "python3 db_init.py -i"
in command line, else run "python3 db_init.py"

See queries.py for sample data and mongo functions
"""

import json
import sys
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # default mongo port is 27017
schools = client['specialdisco'].collection

def generate_json(csvpath, outpath):
    '''uses the given csv file path to generate corresponding json'''
    from csv import DictReader

    with open(csvpath, 'r') as csvfile:
        reader = DictReader(csvfile)
        lines = [line for line in reader]

    with open(outpath,'w') as outfile:
        outfile.write(json.dumps(lines))

def insert_db(jsonpath):
    '''inserts contents of jsonpath into db.specialdisco.collection'''
    from bson.json_util import loads as bson_loads

    with open(jsonpath, 'r') as datafile:
        data = json.loads(datafile.read())
    schools.drop()
    for record in data:
        # data is a dict - must be re-strung, then inserted as bson
        result = schools.insert_one(bson_loads(json.dumps(record)))

def main(argv = None):
    if not argv:
        argv = sys.argv
    if len(argv) == 1:
        print('Usage: \n\t-g: generates json from \"grad.csv\"\n\t-i: inserts contents of \"grad_results.json\" into local mongo')
        return

    flags = argv[1]
    if 'g' in flags:
        generate_json('grad.csv', 'grad_results.json')
    if 'i' in flags:
        insert_db('grad_results.json')

main()
