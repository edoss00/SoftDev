import json
import csv

with open('grad.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

with open('grad_results.json','w') as outfile:
    outfile.write([line for line in reader])
