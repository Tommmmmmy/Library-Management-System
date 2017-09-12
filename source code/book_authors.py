import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()
S = set()
count = 1
with open(r'f:\database design\books.csv', 'rb') as f:
    csv_data = csv.reader(f, delimiter='\t')
    first = True
    for row in csv_data:
        if first:
            first = False
            continue
        array = row[3].split(",")
        for author in array:
            if author in S:
                continue
            set.add(S, author)
            cursor.execute('''INSERT INTO AUTHORS VALUES(%s, %s)''', (count, author))
            count += 1

        number = row[0]
        name = row[2]
        cursor.execute('''INSERT INTO BOOK VALUES(%s, %s)''', (number, name))
#         for element in row:
#             print element.split('\t')

with open(r'f:\database design\books.csv', 'rb') as f:
    csv_data = csv.reader(f, delimiter='\t')
    first = True
    for row in csv_data:
        if first:
            first = False
            continue
        number = row[0]
        array = row[3].split(',')
        S = set()
        for author in array:
            if author in S:
                continue
            set.add(S, author)
            cursor.execute('''SELECT Author_id FROM AUTHORS WHERE Name = %s''', (author, ))
            data = cursor.fetchone()
            cursor.execute('''INSERT INTO BOOK_AUTHORS VALUES(%s, %s)''', (number, data))
mydb.commit()
cursor.close()
print "Done"