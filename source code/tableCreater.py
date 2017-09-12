import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()
cursor.execute('''
CREATE TABLE BOOK (
       Isbn VARCHAR(10) NOT NULL PRIMARY KEY,
       Title VARCHAR(500) NOT NULL
)ENGINE = InnoDB;
CREATE TABLE AUTHORS (
       Author_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       Name TEXT NOT NULL
)ENGINE = InnoDB;
CREATE TABLE BOOK_AUTHORS (
       Isbn VARCHAR(10) NOT NULL,
       Author_id INT NOT NULL,
       PRIMARY KEY(Isbn, Author_id),
       FOREIGN KEY(Isbn) REFERENCES BOOK(Isbn) on delete cascade,
       FOREIGN KEY(Author_id) REFERENCES AUTHORS(Author_id) on delete cascade
)ENGINE = InnoDB;
CREATE TABLE BORROWER (
       Card_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       Ssn VARCHAR(11) NOT NULL,
       Bname VARCHAR(100) NOT NULL,
       Address TEXT,
       Phone TEXT
)ENGINE = InnoDB;
CREATE TABLE BOOK_LOANS (
       Loan_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       Isbn VARCHAR(10) NOT NULL,
       Card_id INT NOT NULL,
       Date_out TEXT,
       Date_in TEXT,
       Due_date TEXT,
       FOREIGN KEY(Isbn) REFERENCES BOOK(Isbn) on delete cascade,
       FOREIGN KEY(Card_id) REFERENCES BORROWER(Card_id) on delete cascade
)ENGINE = InnoDB;
CREATE TABLE FINES (
       Loan_id INT NOT NULL PRIMARY KEY,
       Fine_amt DECIMAL(10,2) NOT NULL ,
       Paid INT NOT NULL ,
       FOREIGN KEY(Loan_id) REFERENCES BOOK_LOANS(Loan_id) on delete cascade
)ENGINE = InnoDB;
       ''')
cursor.close()
print "Done"