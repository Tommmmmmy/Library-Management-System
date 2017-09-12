import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()
with open(r'f:\database design\borrowers.csv', 'rb') as f:
    csv_data = csv.reader(f)
    first = True
    for row in csv_data:
        if first:
            first = False
            continue
        bid = row[0]
        ssn = row[1]
        name = row[2] + ' ' + row[3]
        address = row[5] + ',' + row[6] + ',' + row[7]
        phone = row[8]
        cursor.execute('''INSERT INTO BORROWER VALUES(%s, %s, %s, %s, %s)''', (bid, ssn, name, address, phone))
mydb.commit()
cursor.close()
print "Done"