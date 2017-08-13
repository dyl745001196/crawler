import json
import numpy
import csv
import sys

with open('out.json', 'r') as f:
    data = json.load(f)

index = list(range(0,len(data)))


for i in index:
    index[i] =data[i]['index']
    index[i] = -int(index[i])

index = numpy.array(index)

sort_index = numpy.argsort(index)
sort = numpy.sort(index)
print(sort)
print(sort_index)

data_out = []

for i in range(0, len(data)):

    entry =  data[sort_index[i]]
    print(str(entry['detail']))
    data_out.append(entry)
print(data_out)


csvfile = open('out.csv', 'w')
writer = csv.writer(csvfile)


for entry in data_out:
    detail = entry['detail']
    date = entry['date']
    index = entry['index']
    url = entry['url']
    writer.writerow([index, date, detail, url])
    
