# csv file 
# John, 567, Programmer
# Bob, 857, Sys Admin
# Amy, 769, Marketing

import csv 

f = open('csv_file.txt')  
csv_f = csv.reader(f)
for row in csv_f: 
  name, phone, role = row 
  print('Name: {}, Phone : {}, Role: {}'.format(name, phone, role))

f.close()


