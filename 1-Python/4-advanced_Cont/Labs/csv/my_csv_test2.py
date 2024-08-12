import csv

reader = csv.reader(open('output.csv','r'))
mydict = {}
for line in reader:
    mydict[line[0]] = {line[1],line[2]}
    
    print('\t'.join(line))

print(mydict)