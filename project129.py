import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'con_stars.csv'

d1 = []
d2 = []
with open(file1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open(file2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

pd1 = d1[1:]
pd2 = d2[1:]

h = h1 + h2

p_d = []

for i in pd1:
    p_d.append(i)
for j in pd2:
    p_d.append(j)
with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

df = pd.read_csv('total_stars.csv')
df.tail(8)