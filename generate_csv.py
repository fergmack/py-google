import csv
hosts = [ ["France", "Paris"], ["Spain", "UK"] ]
with open('countries.csv', 'w') as hosts_csv:
  writer = csv.writer(hosts_csv)
  # use writerow to write one line at time. Since we have all our datea we can use writerows
  writer.writerows(hosts)
