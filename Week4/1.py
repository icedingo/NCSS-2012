import csv
import sys

fieldnames = ['firstname', 'lastname', 'email', 'street', 'town', 'state']
addresses = csv.DictReader(open('addresses.csv','rU'), fieldnames=fieldnames)
output = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

queries = raw_input('Query: ').split(',')

for address in addresses:
    for query in queries:
        split_query = query.split('=')
        field = split_query[0].strip()
        value = split_query[1].strip()
        if address[field] != value:
            break
    else:
        output.writerow(address)

