import csv

teste = csv.DictReader(open("./gazetteer_ln.csv"))
classes = []

for item in teste:
    if not classes.__contains__(item['fclass']):
        classes.append(item['fclass'])

print(classes)