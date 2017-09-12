import Tkinter
import MySQLdb
from Tkinter import IntVar
from Tkinter import BOTH, END, EXTENDED, VERTICAL, HORIZONTAL
import datetime
import ttk
import tkFont

class Library(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.create_main_page()

    def create_main_page(self):
        self.parent.title("Library Manager")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")
        self.headline = Tkinter.Label(self.parent, text="Welcome!!!!!!!!!!!!!!!!!")
        self.headline.pack(expand=True, fill=Tkinter.BOTH)
        self.headline.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.username = Tkinter.Label(self.parent, text="Username: ", background="Red", foreground="white",
                                      font="Tahoma 8 bold", anchor="center")
        self.password = Tkinter.Label(self.parent, text="Password: ", background="Red", foreground="white",
                                      font="Tahoma 8 bold", anchor="center")
        self.username.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.password.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_username = Tkinter.Entry(self.parent)
        self.type_password = Tkinter.Entry(self.parent, show="*")
        self.type_username.grid(row=1, column=1, sticky=Tkinter.E+Tkinter.W)
        self.type_password.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.login = Tkinter.Button(self.parent, text="Log in", font="Tahoma 10 bold", command=self.check_run)
        self.exit = Tkinter.Button(self.parent, text="Cancel", font="Tahoma 10 bold", command=self.parent.quit)

        self.login.grid(row=1, column=3, sticky=Tkinter.W)
        self.exit.grid(row=2, column=3, sticky=Tkinter.W)


    def check_run(self):
        if self.type_username.get() == "Tommy" and self.type_password.get() == "Tommy":
            self.function_selection()
        else:
            self.create_main_page()

    def function_selection(self):
        self.menu_window = Tkinter.Toplevel(self)
        self.menu_window.wm_title("Choose a manager")
        self.menu_window.grid_rowconfigure(0, weight=1)
        self.menu_window.grid_columnconfigure(0, weight=1)
        self.headline1 = Tkinter.Label(self.menu_window, text="Choose a manager")
        self.headline1.pack(expand=True, fill=Tkinter.BOTH)
        self.headline1.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.book_manager = Tkinter.Button(self.menu_window, text="Book Manager", command=self.book_menu_window)
        self.borrower_manager = Tkinter.Button(self.menu_window, text="Borrower Manager",
                                               command=self.borrower_menu_window)
        self.fine = Tkinter.Button(self.menu_window, text="Fine Manager", command=self.fine_menu_window)
        self.exit1 = Tkinter.Button(self.menu_window, text="Exit", command=self.menu_window.quit)
        self.book_manager.grid(row=1, column=0)
        self.borrower_manager.grid(row=2, column=0)
        self.exit1.grid(row=4, column=0)
        self.fine.grid(row=3, column=0)

    def book_menu_window(self):
        self.book_window = Tkinter.Toplevel(self)
        self.book_window.wm_title("Choose a function")
        self.book_window.grid_rowconfigure(0, weight=1)
        self.book_window.grid_columnconfigure(0, weight=1)
        self.headline2 = Tkinter.Label(self.book_window, text="Choose a function")
        self.headline2.pack(expand=True, fill=Tkinter.BOTH)
        self.headline2.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.search_window = Tkinter.Button(self.book_window, text="Search a book", command=self.search_book)
        self.return_window = Tkinter.Button(self.book_window, text="Return a book", command=self.return_book)
        self.exit2 = Tkinter.Button(self.book_window, text="Exit", command=self.book_window.quit)
        self.search_window.grid(row=1, column=0)
        self.return_window.grid(row=2, column=0)
        self.exit2.grid(row=3, column=0)

    def borrower_menu_window(self):
        self.borrower_window = Tkinter.Toplevel(self)
        self.borrower_window.wm_title("Choose a function")
        self.borrower_window.grid_rowconfigure(0, weight=1)
        self.borrower_window.grid_columnconfigure(0, weight=1)
        self.headline3 = Tkinter.Label(self.borrower_window, text="Choose a function")
        self.headline3.pack(expand=True, fill=Tkinter.BOTH)
        self.headline3.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.add_user = Tkinter.Button(self.borrower_window, text="Add a borrower", command=self.add_window)
        self.exit3 = Tkinter.Button(self.borrower_window, text="Exit", command=self.borrower_window.quit)
        self.add_user.grid(row=1, column=0)
        self.exit3.grid(row=3, column=0)

    def search_book(self):
        self.search_book_window = Tkinter.Toplevel(self)
        self.search_book_window.wm_title("Choose a function")
        self.search_book_window.grid_rowconfigure(0, weight=1)
        self.search_book_window.grid_columnconfigure(0, weight=1)
        self.headline4 = Tkinter.Label(self.search_book_window, text="Enter any information you have and separate them with ','")
        self.headline4.pack(expand=True, fill=Tkinter.BOTH)
        self.headline4.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.type_in_label = Tkinter.Label(self.search_book_window, text="Key words: ", background="Red", foreground="white",
                                      font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_label.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_in = Tkinter.Entry(self.search_book_window)
        self.type_in.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.headline5 = Tkinter.Label(self.search_book_window,
                                       text="If you want to borrow a book, please type in your card number")
        self.headline5.pack(expand=True, fill=Tkinter.BOTH)
        self.headline5.grid(row=2, sticky=Tkinter.E + Tkinter.W)
        self.borrower_label = Tkinter.Label(self.search_book_window, text="Borrower card number: ", background="Red",
                                           foreground="white",
                                           font="Tahoma 8 bold", anchor="center", relief="groove")
        self.borrower_label.grid(row=3, column=0, sticky=Tkinter.E + Tkinter.W)
        self.borrower_in = Tkinter.Entry(self.search_book_window)
        self.borrower_in.grid(row=3, column=1, sticky=Tkinter.E + Tkinter.W)
        self.search = Tkinter.Button(self.search_book_window, text="Search", font="Tahoma 10 bold", command=self.show_result)
        self.exit4 = Tkinter.Button(self.search_book_window, text="Exit", font="Tahoma 10 bold", command=self.search_book_window.quit)
        self.search.grid(row=4, column=0, sticky=Tkinter.W)
        self.exit4.grid(row=4, column=1, sticky=Tkinter.E)

    def show_result(self):
        self.search_result_window = Tkinter.Toplevel(self)
        self.search_result_window.geometry("650x400")
        self.search_result_window.wm_title("Searching results")
        self.search_result_window.grid_rowconfigure(0, weight=1)
        self.search_result_window.grid_columnconfigure(0, weight=1)
        self.information = self.type_in.get()
        self.connecttodb = MySQLdb.connect(host='localhost',
                                           user='root',
                                           passwd='',
                                           db='mydb')
        self.cursor = self.connecttodb.cursor()
        scrollbary = Tkinter.Scrollbar(self.search_result_window, orient="vertical")
        scrollbarx = Tkinter.Scrollbar(self.search_result_window, orient="horizontal")
        self.result_tree = ttk.Treeview(self.search_result_window, columns=("A", "B", "C"), yscrollcommand=scrollbary.set)
        self.result_tree.heading("#0", text="ISBN")
        self.result_tree.column("#0", minwidth=0, width=50, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree.heading("A", text="BOOK TITLE")
        self.result_tree.column("A", minwidth=0, width=250, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree.heading("B", text="AUTHOR(S)")
        self.result_tree.column("B", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree.heading("C", text="Availability")
        self.result_tree.column("C", minwidth=0, width=30, stretch="YES", anchor=Tkinter.CENTER)
        scrollbary.config(command=self.result_tree.yview)
        scrollbary.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        scrollbarx.config(command=self.result_tree.xview)
        scrollbarx.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        self.result_tree.pack(side="bottom", expand=True, fill='both')


        # self.listbox = Tkinter.Listbox(self.search_result_window, selectmode=EXTENDED)
        # self.listbox.grid(row=0, column=0, sticky=Tkinter.N + Tkinter.S + Tkinter.E + Tkinter.W)
        # vsb = Tkinter.Scrollbar(self.search_result_window, orient="vertical",
        #                    command=self.listbox.yview)
        # hsb = Tkinter.Scrollbar(self.search_result_window, orient="horizontal",
        #                     command=self.listbox.xview)
        self.result_tree.bind('<<TreeviewSelect>>')
        # self.listbox.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        # vsb.grid(column=1, row=0, sticky='ns', in_=Tkinter.Frame())
        # hsb.grid(column=0, row=1, sticky='ew', in_=Tkinter.Frame())
        # if self.isbn == "" and self.title == "" and self.author == "":
        #     self.none_label = Tkinter.Label(self.search_book_window, text="No matching results")
        #     self.none_label.pack(expand=True, fill=Tkinter.BOTH)
        #     self.none_label.grid(row=5)
        # elif self.isbn == "" and self.title == "":
        S = set()
        self.resultlist = []
        self.dict = {}
        self.information_array = self.information.split(",")
        for information_sub in self.information_array:
            self.cursor.execute("""SELECT * FROM BOOK WHERE INSTR(BOOK.Title, %s) > 0 OR INSTR(BOOK.Isbn, %s)""",
                                (information_sub, information_sub))
            book_data = self.cursor.fetchall()
            for book_dataa in book_data:
                if str(book_dataa[0]) not in S:
                    templist = []
                    templist.append(str(book_dataa[0]))
                    templist.append(str(book_dataa[1]))
                    self.cursor.execute("""SELECT Author_id FROM BOOK_AUTHORS WHERE Isbn = %s""",
                                        (str(book_dataa[0]),))
                    authorids = self.cursor.fetchall()
                    authornames = []
                    for authorid in authorids:
                        self.cursor.execute("""SELECT Name FROM AUTHORS WHERE Author_id = %s""",
                                            (str(authorid[0]),))
                        tempname = self.cursor.fetchone()
                        authornames.append(str(tempname[0]))
                    authorname_string = self.generate_authorname(namelist=authornames)
                    templist.append(authorname_string)
                    S.add(str(book_dataa[0]))
                    self.resultlist.append(templist)
                    self.dict[str(book_dataa[0])] = templist
        for information_sub in self.information_array:
            self.cursor.execute("""SELECT * FROM AUTHORS WHERE INSTR(Name, %s) > 0""",
                                (information_sub,))
            author_data = self.cursor.fetchall()
            for author_dataa in author_data:
                self.cursor.execute("""SELECT Isbn FROM BOOK_AUTHORS WHERE Author_id = %s""",
                                    (str(author_dataa[0]),))
                isbns = self.cursor.fetchall()
                for isbn in isbns:
                    templist = []
                    if str(isbn[0]) not in S:
                        self.cursor.execute("""SELECT Author_id FROM BOOK_AUTHORS WHERE Isbn = %s""", (str(isbn[0]),))
                        authorids = self.cursor.fetchall()
                        authornames = []
                        for authorid in authorids:
                            self.cursor.execute("""SELECT Name FROM AUTHORS WHERE Author_id = %s""",
                                                (str(authorid[0]),))
                            tempname = self.cursor.fetchone()
                            authornames.append(str(tempname[0]))
                        authorname_string = self.generate_authorname(namelist=authornames)
                        self.cursor.execute("""SELECT Title FROM BOOK WHERE Isbn = %s""", (str(isbn[0]),))
                        title = self.cursor.fetchone()
                        templist.append(str(isbn[0]))
                        templist.append(str(title[0]))
                        templist.append(authorname_string)
                        S.add(str(isbn[0]))
                        self.resultlist.append(templist)
                        self.dict[str(isbn[0])] = templist
        self.counter = {}
        for tuple in self.resultlist:
            count = 0
            for information_sub in self.information_array:
                information_sub = information_sub.lower()
                if tuple[0].lower().find(information_sub) >= 0:
                    count += 1
                if tuple[1].lower().find(information_sub) >= 0:
                    count += 1
                if tuple[2].lower().find(information_sub) >= 0:
                    count += 1
            self.counter[tuple[0]] = count
        sorted_resultlist = []
        for pair in sorted(self.counter, key=self.counter.get, reverse=True):
            sorted_resultlist.append(self.dict[pair])
        for tuple in sorted_resultlist:
            self.cursor.execute("""SELECT * FROM BOOK_LOANS WHERE Isbn = %s AND Date_in IS NULL""", (tuple[0],))
            available = self.cursor.fetchone()
            if not available:
                tuple.append("available")
                self.result_tree.insert("", "end", text=tuple[0], values=(
                    tuple[1], tuple[2], tuple[3]))
            else:
                tuple.append("unavailable")
                self.result_tree.insert("", "end", text=tuple[0], values=(
                    tuple[1], tuple[2], tuple[3]))
                self.result_tree.pack(side="top", fill="both", expand=1)
        check_out = Tkinter.Button(self.search_result_window, text="CHECK_OUT", command=self.immediately1)
        check_out.pack(side="bottom")


        # elif
        # self.listbox.pack(fill=BOTH, expand=True)
        # self.connecttodb.commit()
        # self.connecttodb.close()

    def add_window(self):
        self.add_user_window = Tkinter.Toplevel(self)
        self.add_user_window.wm_title("Add a borrower")
        self.add_user_window.grid_rowconfigure(0, weight=1)
        self.add_user_window.grid_columnconfigure(0, weight=1)
        self.headline6 = Tkinter.Label(self.add_user_window,
                                       text="Enter Ssn, Name, and Address:")
        self.headline6.pack(expand=True, fill=Tkinter.BOTH)
        self.headline6.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.type_in_ssn = Tkinter.Label(self.add_user_window, text="Ssn: ", background="Red",
                                           foreground="white",
                                           font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_ssn.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_ssn = Tkinter.Entry(self.add_user_window)
        self.type_ssn.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_name = Tkinter.Label(self.add_user_window, text="Name: ", background="Red",
                                            foreground="white",
                                            font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_name.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_name = Tkinter.Entry(self.add_user_window)
        self.type_name.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_address = Tkinter.Label(self.add_user_window, text="Address: ", background="Red",
                                          foreground="white",
                                          font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_address.grid(row=3, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_address = Tkinter.Entry(self.add_user_window)
        self.type_address.grid(row=3, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_phone = Tkinter.Label(self.add_user_window, text="Phone: (Optional)", background="Red",
                                             foreground="white",
                                             font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_phone.grid(row=4, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_phone = Tkinter.Entry(self.add_user_window)
        self.type_phone.grid(row=4, column=1, sticky=Tkinter.E + Tkinter.W)
        self.add_button = Tkinter.Button(self.add_user_window, text="Add", font="Tahoma 10 bold",
                                     command=self.add_function)
        self.exit6 = Tkinter.Button(self.add_user_window, text="Exit", font="Tahoma 10 bold",
                                    command=self.add_user_window.quit)
        self.add_button.grid(row=5, column=0, sticky=Tkinter.W)
        self.exit6.grid(row=5, column=1, sticky=Tkinter.E)

    def add_function(self):
        ssn = self.type_ssn.get()
        name = self.type_name.get()
        address = self.type_address.get()
        phone = self.type_phone.get()
        self.connecttodb = MySQLdb.connect(host='localhost',
                                           user='root',
                                           passwd='',
                                           db='mydb')
        self.cursor = self.connecttodb.cursor()
        row_count = self.cursor.execute('''SELECT * FROM BORROWER WHERE Ssn=%s''', (ssn, ))
        if row_count == 0:
            self.cursor.execute(
                '''INSERT INTO BORROWER(Ssn, Bname, Address, Phone) VALUES(%s, %s, %s, %s)''',
                (ssn, name, address, phone))
            self.cursor.execute(
                '''SELECT Card_id FROM BORROWER WHERE Ssn = %s''',
                (ssn, ))
            data = self.cursor.fetchone()
            self.warning_window = Tkinter.Toplevel(self)
            self.warning_window.geometry("500x250")
            self.warning_window.wm_title("Warning message")
            self.warning_window.grid_rowconfigure(0, weight=1)
            self.warning_window.grid_columnconfigure(0, weight=1)
            self.headline5 = Tkinter.Label(self.warning_window,
                                           text="Congratulations!\n Your Card ID is " + str(data[0]), background="Red",
                                           foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline5.pack(expand=True, fill=Tkinter.BOTH)
            self.headline5.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        else:
            self.warning_window = Tkinter.Toplevel(self)
            self.warning_window.geometry("500x250")
            self.warning_window.wm_title("Warning message")
            self.warning_window.grid_rowconfigure(0, weight=1)
            self.warning_window.grid_columnconfigure(0, weight=1)
            self.headline5 = Tkinter.Label(self.warning_window,
                                           text="You already have a library card!", background="Red",
                                           foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline5.pack(expand=True, fill=Tkinter.BOTH)
            self.headline5.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.connecttodb.commit()

    def fine_menu_window(self):
        self.fine_window = Tkinter.Toplevel(self)
        self.fine_window.wm_title("Choose a function")
        self.fine_window.grid_rowconfigure(0, weight=1)
        self.fine_window.grid_columnconfigure(0, weight=1)
        self.update_fine = Tkinter.Button(self.fine_window, text="Update fines", command=self.update_function)
        self.update_fine.grid(row=0)
        self.show_fine = Tkinter.Button(self.fine_window, text="Show fines", command=self.show_function)
        self.show_fine.grid(row=1)
        self.pay = Tkinter.Button(self.fine_window, text="Pay fines", command=self.pay_function)
        self.pay.grid(row=2)

    def update_function(self):
        self.connecttodb = MySQLdb.connect(host='localhost',
                                           user='root',
                                           passwd='',
                                           db='mydb')
        self.cursor = self.connecttodb.cursor()
        self.cursor.execute('''SELECT * FROM BOOK_LOANS WHERE Date_in IS NULL''')
        data1 = self.cursor.fetchall()
        self.cursor.execute('''SELECT * FROM BOOK_LOANS,FINES WHERE BOOK_LOANS.Loan_id=FINES.Loan_id AND FINES.Paid=0''')
        data2 = self.cursor.fetchall()
        for dd in data1:
            if dd[5] < str(datetime.date.today()):
                temp_array = dd[5].split("-")
                temp_string = temp_array[2] + temp_array[1] + temp_array[0]
                fine_amountt = int(
                    (datetime.date.today() - datetime.datetime.strptime(temp_string, "%d%m%Y").date()).days)
                count_roww = self.cursor.execute('''SELECT * FROM FINES WHERE Loan_id = %s''', (dd[0],))
                if count_roww == 0:
                    self.cursor.execute(
                        """INSERT INTO FINES(Loan_id, Fine_amt, Paid) VALUES(%s, %s, %s)""",
                        (dd[0], fine_amountt * 0.25, 0))
                else:
                    self.cursor.execute("""
                                                                               UPDATE FINES SET Fine_amt = %s WHERE Loan_id=%s
                                                                            """, (fine_amountt * 0.25, dd[0]))
        for dd in data2:
            temp_array1 = dd[4].split("-")
            temp_string1 = temp_array1[2] + temp_array1[1] + temp_array1[0]
            temp_array2 = dd[5].split("-")
            temp_string2 = temp_array2[2] + temp_array2[1] + temp_array2[0]
            fine_amount = (datetime.datetime.strptime(temp_string1, "%d%m%Y").date()) - (
                datetime.datetime.strptime(temp_string2, "%d%m%Y").date())
            fine_amount = int(str(fine_amount).split(" ")[0])
            count_row = self.cursor.execute('''SELECT * FROM FINES WHERE Loan_id = %s''', (dd[0],))
            temp_data = self.cursor.fetchone()
            if count_row == 0:
                self.cursor.execute(
                    """INSERT INTO FINES(Loan_id, Fine_amt, Paid) VALUES(%s, %s, %s)""",
                    (dd[0], fine_amount * 0.25, 0))
            else:
                if int(temp_data[2]) == 0:
                    self.cursor.execute("""
                                                       UPDATE FINES SET Fine_amt = %s WHERE Loan_id=%s
                                                    """, (fine_amount * 0.25, dd[0]))
        self.connecttodb.commit()

    def pay_function(self):
        self.pay_window = Tkinter.Toplevel(self)
        self.pay_window.wm_title("Search a fine")
        self.pay_window.grid_rowconfigure(0, weight=1)
        self.pay_window.grid_columnconfigure(0, weight=1)
        self.headline7 = Tkinter.Label(self.pay_window,
                                       text="Enter Name or Card_id:")
        self.headline7.pack(expand=True, fill=Tkinter.BOTH)
        self.headline7.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.type_in_name1 = Tkinter.Label(self.pay_window, text="Name: ", background="Red",
                                         foreground="white",
                                         font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_name1.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_name1 = Tkinter.Entry(self.pay_window)
        self.type_name1.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_cardid = Tkinter.Label(self.pay_window, text="Card_id: ", background="Red",
                                          foreground="white",
                                          font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_cardid.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_cardid = Tkinter.Entry(self.pay_window)
        self.type_cardid.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.search_button = Tkinter.Button(self.pay_window, text="Search", font="Tahoma 10 bold", command=self.search_function)
        self.exit7 = Tkinter.Button(self.pay_window, text="Exit", font="Tahoma 10 bold")
        self.search_button.grid(row=3, column=0, sticky=Tkinter.W)
        self.exit7.grid(row=3, column=1, sticky=Tkinter.E)

    def show_function(self):
        self.pay_window = Tkinter.Toplevel(self)
        self.pay_window.wm_title("Search a fine")
        self.pay_window.grid_rowconfigure(0, weight=1)
        self.pay_window.grid_columnconfigure(0, weight=1)
        self.headline7 = Tkinter.Label(self.pay_window,
                                       text="Enter Name or Card_id:")
        self.headline7.pack(expand=True, fill=Tkinter.BOTH)
        self.headline7.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.type_in_name1 = Tkinter.Label(self.pay_window, text="Name: ", background="Red",
                                           foreground="white",
                                           font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_name1.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_name1 = Tkinter.Entry(self.pay_window)
        self.type_name1.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_cardid = Tkinter.Label(self.pay_window, text="Card_id: ", background="Red",
                                            foreground="white",
                                            font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_cardid.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_cardid = Tkinter.Entry(self.pay_window)
        self.type_cardid.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.search_button = Tkinter.Button(self.pay_window, text="Search", font="Tahoma 10 bold",
                                            command=self.sum_function)
        self.exit7 = Tkinter.Button(self.pay_window, text="Exit", font="Tahoma 10 bold")
        self.search_button.grid(row=3, column=0, sticky=Tkinter.W)
        self.exit7.grid(row=3, column=1, sticky=Tkinter.E)

    def search_function(self):
        name = self.type_name1.get()
        cardid = self.type_cardid.get()
        if name == "":
            name = "******"
        if cardid == "":
            cardid = 0
        self.search_window = Tkinter.Toplevel(self)
        self.search_window.wm_title("Search results")
        self.search_window.grid_rowconfigure(0, weight=1)
        self.search_window.grid_columnconfigure(0, weight=1)
        self.connecttodb = MySQLdb.connect(host='localhost',
                                           user='root',
                                           passwd='',
                                           db='mydb')
        self.cursor = self.connecttodb.cursor()
        scrollbar = Tkinter.Scrollbar(self.search_window, orient="vertical")
        self.result_tree2 = ttk.Treeview(self.search_window, columns=("A", "B", "C", "D", "E"),
                                        yscrollcommand=scrollbar.set)
        self.result_tree2.heading("#0", text="Loan Id")
        self.result_tree2.column("#0", minwidth=0, width=30, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree2.heading("A", text="Isbn")
        self.result_tree2.column("A", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree2.heading("B", text="Title")
        self.result_tree2.column("B", minwidth=0, width=250, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree2.heading("C", text="Card Id")
        self.result_tree2.column("C", minwidth=0, width=30, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree2.heading("D", text="Borrower Name")
        self.result_tree2.column("D", minwidth=0, width=50, stretch="YES", anchor=Tkinter.CENTER)
        self.result_tree2.heading("E", text="Fine amount")
        self.result_tree2.column("E", minwidth=0, width=30, stretch="YES", anchor=Tkinter.CENTER)
        scrollbar.config(command=self.result_tree2.yview)
        scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        self.result_tree2.pack(side="bottom",expand=True, fill='both')
        self.result_tree2.bind('<<TreeviewSelect>>')
        # self.listbox2 = Tkinter.Listbox(self.search_window, selectmode=EXTENDED)
        # self.listbox2.grid(row=0, column=0, sticky=Tkinter.N + Tkinter.S + Tkinter.E + Tkinter.W)
        # self.listbox2.bind('<<ListboxSelect>>', self.immediately2)
        self.cursor.execute('''SELECT Fine_amt, BORROWER.Bname, BORROWER.Card_id, BOOK.Title, BOOK.Isbn, FINES.Loan_id FROM FINES, BOOK_LOANS, BORROWER, BOOK WHERE FINES.Loan_id
        =BOOK_LOANS.Loan_id AND BOOK_LOANS.Card_id=BORROWER.Card_id AND BOOK_LOANS.Isbn=BOOK.Isbn AND FINES.Paid=0 AND (INSTR(BORROWER.Bname, %s) >= 0 OR BORROWER.Card_id = %s)''', (str(name), str(cardid)))
        data = self.cursor.fetchall()
        for tuple in data:
            self.result_tree2.insert("", "end", text=tuple[5], values=(
                tuple[4], tuple[3], tuple[2], tuple[1], tuple[0]))
        check_out = Tkinter.Button(self.search_window, text="Pay!", command=self.immediately2)
        check_out.pack(side="bottom")

    def sum_function(self):
        name = self.type_name1.get()
        cardid = self.type_cardid.get()
        if name == "":
            name = "******"
        if cardid == "":
            cardid = 0
        self.connecttodb = MySQLdb.connect(host='localhost',
                                           user='root',
                                           passwd='',
                                           db='mydb')
        self.cursor = self.connecttodb.cursor()
        count = self.cursor.execute('''SELECT BORROWER.Bname, BORROWER.Card_id, SUM(Fine_amt) FROM FINES, BOOK_LOANS, BORROWER, BOOK WHERE FINES.Loan_id
        =BOOK_LOANS.Loan_id AND BOOK_LOANS.Card_id=BORROWER.Card_id AND BOOK_LOANS.Isbn=BOOK.Isbn AND FINES.Paid=0 AND (BORROWER.Bname = %s OR BORROWER.Card_id = %s) GROUP BY BORROWER.Bname''', (str(name), str(cardid)))
        data = self.cursor.fetchall()
        if count == 0:
            self.warning_window2 = Tkinter.Toplevel(self)
            self.warning_window2.geometry("500x250")
            self.warning_window2.wm_title("Warning message")
            self.warning_window2.grid_rowconfigure(0, weight=1)
            self.warning_window2.grid_columnconfigure(0, weight=1)
            self.headline9 = Tkinter.Label(self.warning_window2,
                                           text="There is no such a matching record!", background="Red",
                                           foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline9.pack(expand=True, fill=Tkinter.BOTH)
            self.headline9.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        else:
            self.sum_window = Tkinter.Toplevel(self)
            self.sum_window.wm_title("Search results")
            self.sum_window.grid_rowconfigure(0, weight=1)
            self.sum_window.grid_columnconfigure(0, weight=1)
            scrollbar = Tkinter.Scrollbar(self.sum_window, orient="vertical")
            self.result_tree3 = ttk.Treeview(self.sum_window, columns=("A", "B"),
                                             yscrollcommand=scrollbar.set)
            self.result_tree3.heading("#0", text="Borrower Name", anchor=Tkinter.CENTER)
            self.result_tree3.column("#0", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
            self.result_tree3.heading("A", text="Borrower ID", anchor=Tkinter.CENTER)
            self.result_tree3.column("A", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
            self.result_tree3.heading("B", text="Total Fine Amount", anchor=Tkinter.CENTER)
            self.result_tree3.column("B", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
            scrollbar.config(command=self.result_tree3.yview)
            scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
            self.result_tree3.pack(side="bottom", expand=True, fill='both')
            self.result_tree3.bind('<<TreeviewSelect>>')
            # self.listbox4 = Tkinter.Listbox(self.sum_window, selectmode=EXTENDED)
            # self.listbox4.grid(row=0, column=0, sticky=Tkinter.N + Tkinter.S + Tkinter.E + Tkinter.W)
            # self.listbox4.bind('<<ListboxSelect>>', self.immediately4)
            for tuple in data:
                self.result_tree3.insert("", "end", text=tuple[0], values=(
                    tuple[1], tuple[2]))
            check_out = Tkinter.Button(self.sum_window, text="Pay!", command=self.immediately4)
            check_out.pack(side="bottom")

    def return_book(self):
        self.return_book_window = Tkinter.Toplevel(self)
        self.return_book_window.wm_title("Choose a function")
        self.return_book_window.grid_rowconfigure(0, weight=1)
        self.return_book_window.grid_columnconfigure(0, weight=1)
        self.headline7 = Tkinter.Label(self.return_book_window,
                                       text="Enter any information you have:")
        self.headline7.pack(expand=True, fill=Tkinter.BOTH)
        self.headline7.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.type_in_title = Tkinter.Label(self.return_book_window, text="Title: ", background="Red",
                                           foreground="white",
                                           font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_title.grid(row=3, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_title = Tkinter.Entry(self.return_book_window)
        self.type_title.grid(row=3, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_id = Tkinter.Label(self.return_book_window, text="Card id: ", background="Red",
                                            foreground="white",
                                            font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_id.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_id = Tkinter.Entry(self.return_book_window)
        self.type_id.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.type_in_borrower = Tkinter.Label(self.return_book_window, text="Borrower name: ", background="Red",
                                        foreground="white",
                                        font="Tahoma 8 bold", anchor="center", relief="groove")
        self.type_in_borrower.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.type_borrower = Tkinter.Entry(self.return_book_window)
        self.type_borrower.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.return_book = Tkinter.Button(self.return_book_window, text="Search", font="Tahoma 10 bold", command=self.return_function)
        self.exit4 = Tkinter.Button(self.return_book_window, text="Exit", font="Tahoma 10 bold",
                                    command=self.return_book_window.quit)
        self.return_book.grid(row=4, column=0, sticky=Tkinter.W)
        self.exit4.grid(row=4, column=1, sticky=Tkinter.E)

    def return_function(self):
        title = self.type_title.get()
        cardid = self.type_id.get()
        name = self.type_borrower.get()
        if title == "":
            title = "*****"
        if cardid == "":
            cardid = 0
        if name == "":
            name = "******"
        self.connecttodb = MySQLdb.connect(host='localhost',
                                           user='root',
                                           passwd='',
                                           db='mydb')
        self.cursor = self.connecttodb.cursor()
        count = self.cursor.execute('''SELECT BOOK_LOANS.Loan_id, BOOK.Isbn, BOOK.Title, BORROWER.Card_id, BORROWER.Bname FROM BOOK_LOANS, BOOK, BORROWER WHERE BOOK_LOANS.Isbn=BOOK.Isbn AND BOOK_LOANS.Card_id=BORROWER.Card_id AND
        ((BOOK_LOANS.Card_id=%s OR BORROWER.Bname=%s OR INSTR(BOOK.Title,%s)) AND BOOK_LOANS.Date_in IS NULL)''', (str(cardid), str(name), str(title)))
        data = self.cursor.fetchall()
        if count == 0:
            self.warning_window2 = Tkinter.Toplevel(self)
            self.warning_window2.geometry("500x250")
            self.warning_window2.wm_title("Warning message")
            self.warning_window2.grid_rowconfigure(0, weight=1)
            self.warning_window2.grid_columnconfigure(0, weight=1)
            self.headline9 = Tkinter.Label(self.warning_window2,
                                           text="There is no such a matching record!", background="Red", foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline9.pack(expand=True, fill=Tkinter.BOTH)
            self.headline9.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        else:
            self.search_window1 = Tkinter.Toplevel(self)
            self.search_window1.wm_title("Search results")
            self.search_window1.grid_rowconfigure(0, weight=1)
            self.search_window1.grid_columnconfigure(0, weight=1)
            self.search_window1.geometry("400x300")
            self.connecttodb = MySQLdb.connect(host='localhost',
                                               user='root',
                                               passwd='',
                                               db='mydb')
            self.cursor = self.connecttodb.cursor()
            scrollbar = Tkinter.Scrollbar(self.search_window1, orient="vertical")
            self.result_tree4 = ttk.Treeview(self.search_window1, columns=("A", "B", "C", "D"),
                                             yscrollcommand=scrollbar.set)
            self.result_tree4.heading("#0", text="Loan Id", anchor=Tkinter.CENTER)
            self.result_tree4.column("#0", minwidth=0, width=50, stretch="YES", anchor=Tkinter.CENTER)
            self.result_tree4.heading("A", text="Isbn", anchor=Tkinter.CENTER)
            self.result_tree4.column("A", minwidth=0, width=50, stretch="YES", anchor=Tkinter.CENTER)
            self.result_tree4.heading("B", text="Title", anchor=Tkinter.CENTER)
            self.result_tree4.column("B", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
            self.result_tree4.heading("C", text="Card Id", anchor=Tkinter.CENTER)
            self.result_tree4.column("C", minwidth=0, width=50, stretch="YES", anchor=Tkinter.CENTER)
            self.result_tree4.heading("D", text="Borrower Name", anchor=Tkinter.CENTER)
            self.result_tree4.column("D", minwidth=0, width=100, stretch="YES", anchor=Tkinter.CENTER)
            scrollbar.config(command=self.result_tree4.yview)
            scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
            self.result_tree4.pack(side="bottom", expand=True, fill='both')
            self.result_tree4.bind('<<TreeviewSelect>>')
            # self.listbox3 = Tkinter.Listbox(self.search_window1, selectmode=EXTENDED)
            # self.listbox3.grid(row=0, column=0, sticky=Tkinter.N + Tkinter.S + Tkinter.E + Tkinter.W)
            # self.listbox3.bind('<<ListboxSelect>>', self.immediately3)
            for tuple in data:
                self.result_tree4.insert("", "end", text=tuple[0], values=(
                    tuple[1], tuple[2], tuple[3], tuple[4]))
            check_out = Tkinter.Button(self.search_window1, text="Return!", command=self.immediately3)
            check_out.pack(side="bottom")

    def generate_authorname(self, namelist):
        author = ""
        boolean = False
        for authorname in namelist:
            if boolean == True:
                author += ", "
            else:
                boolean = True
            author += str(authorname)
        return author

    def immediately1(self):
        # Note here that Tkinter passes an event object to onselect()
        for item in self.result_tree.selection():
            chosen = self.result_tree.item(item, "text")
        row_count = self.cursor.execute("""SELECT * FROM BOOK_LOANS WHERE Isbn = %s AND Date_in IS NULL""", (chosen,))
        if row_count == 0:
            if not self.borrower_in.get() == "":
                self.cursor.execute("""SELECT COUNT(*) FROM BOOK_LOANS WHERE Card_id = %s AND Date_in IS NULL""", (self.borrower_in.get(),))
                times = self.cursor.fetchone()
                if int(times[0]) < 3:
                    self.cursor.execute(
                        """INSERT INTO BOOK_LOANS(Card_id, Isbn, Date_out, Due_date) VALUES(%s, %s, %s, %s)""",
                        (self.borrower_in.get(), chosen, datetime.date.today(),
                         datetime.date.today() + datetime.timedelta(days=14)))
                    self.warning_window = Tkinter.Toplevel(self)
                    self.warning_window.geometry("500x250")
                    self.warning_window.wm_title("Warning message")
                    self.warning_window.grid_rowconfigure(0, weight=1)
                    self.warning_window.grid_columnconfigure(0, weight=1)
                    self.headline5 = Tkinter.Label(self.warning_window,
                                                   text="The borrower with Card_id " + self.borrower_in.get() +
                                                        " borrowed book with\n" + chosen + " successfully!" + "\n"
                                                        "Borrowing Date: " + str(datetime.date.today()) + "\n"
                                                        "Returning Date: " + str(datetime.date.today() + datetime.timedelta(days=14)),
                                                   background="Red", foreground="white",
                                                   font="Tahoma 8 bold", anchor="center", relief="groove")
                    self.headline5.pack(expand=True, fill=Tkinter.BOTH)
                    self.headline5.grid(row=0, sticky=Tkinter.E + Tkinter.W)
                else:
                    self.warning_window = Tkinter.Toplevel(self)
                    self.warning_window.geometry("500x250")
                    self.warning_window.wm_title("Warning message")
                    self.warning_window.grid_rowconfigure(0, weight=1)
                    self.warning_window.grid_columnconfigure(0, weight=1)
                    self.headline5 = Tkinter.Label(self.warning_window,
                                                   text="The borrower with Card_id " + self.borrower_in.get() + " has reached the maximum of 3 loans!", background="Red", foreground="white",
                                      font="Tahoma 8 bold", anchor="center", relief="groove")
                    self.headline5.pack(expand=True, fill=Tkinter.BOTH)
                    self.headline5.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        else:
            self.warning_window = Tkinter.Toplevel(self)
            self.warning_window.geometry("500x250")
            self.warning_window.wm_title("Warning message")
            self.warning_window.grid_rowconfigure(0, weight=1)
            self.warning_window.grid_columnconfigure(0, weight=1)
            self.headline5 = Tkinter.Label(self.warning_window,
                                           text="The book you have chosen has been borrowed!", background="Red", foreground="white",
                                      font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline5.pack(expand=True, fill=Tkinter.BOTH)
            self.headline5.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.connecttodb.commit()

    def immediately2(self):
        # Note here that Tkinter passes an event object to onselect()
        for item in self.result_tree2.selection():
            chosen = self.result_tree2.item(item)
        self.cursor.execute("""SELECT * FROM BOOK_LOANS WHERE Loan_id = %s""", (str(chosen['text']),))
        data = self.cursor.fetchone()
        if not bool(data[4]):
            self.warning_window1 = Tkinter.Toplevel(self)
            self.warning_window1.geometry("500x250")
            self.warning_window1.wm_title("Warning message")
            self.warning_window1.grid_rowconfigure(0, weight=1)
            self.warning_window1.grid_columnconfigure(0, weight=1)
            self.headline8 = Tkinter.Label(self.warning_window1,
                                           text="The borrower with ID " + str(chosen['values'][2]) + " has not returned the book yet!", background="Red",
                                           foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline8.pack(expand=True, fill=Tkinter.BOTH)
            self.headline8.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        else:
            self.cursor.execute("""UPDATE FINES SET Paid=1 WHERE Loan_id=%s""", (str(chosen['text']),))
            self.warning_window1 = Tkinter.Toplevel(self)
            self.warning_window1.geometry("500x250")
            self.warning_window1.wm_title("Warning message")
            self.warning_window1.grid_rowconfigure(0, weight=1)
            self.warning_window1.grid_columnconfigure(0, weight=1)
            self.headline8 = Tkinter.Label(self.warning_window1,
                                           text="The fine related with " + str(chosen['values'][0]) + " has been paid! Thank you!",
                                           background="Red",
                                           foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline8.pack(expand=True, fill=Tkinter.BOTH)
            self.headline8.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.connecttodb.commit()

    def immediately3(self):
        for item in self.result_tree4.selection():
            chosen = self.result_tree4.item(item)
        self.warning_window2 = Tkinter.Toplevel(self)
        self.warning_window2.geometry("500x250")
        self.warning_window2.wm_title("Message")
        self.warning_window2.grid_rowconfigure(0, weight=1)
        self.warning_window2.grid_columnconfigure(0, weight=1)
        self.headline9 = Tkinter.Label(self.warning_window2,
                                       text="The book with ISBN " + str(chosen['values'][0]) + " has been returned successfully!",
                                       background="Red",
                                       foreground="white",
                                       font="Tahoma 10 bold", anchor="center", relief="groove")
        self.headline9.pack(expand=True, fill=Tkinter.BOTH)
        self.headline9.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        self.cursor.execute("""
                            UPDATE BOOK_LOANS SET Date_in=%s WHERE Loan_id=%s
                            """, (datetime.date.today(), str(chosen['text'])))
        self.cursor.execute("""
                               SELECT * FROM BOOK_LOANS WHERE Loan_id=%s
                                    """, (str(chosen['text']), ))
        data = self.cursor.fetchone()
        if data[4] > data[5]:
            count = self.cursor.execute("""
                                   SELECT * FROM FINES WHERE Loan_id=%s
                                                            """, (str(chosen['text']),))
            if count == 0:
                self.cursor.execute("""
                                                    INSERT INTO FINES VALUES(%s, %s, %s)
                                                                """, (str(chosen['text']), 0, 0))
        self.connecttodb.commit()

    def immediately4(self):
        for item in self.result_tree3.selection():
            chosen = self.result_tree3.item(item)
        count = self.cursor.execute("""SELECT * FROM BOOK_LOANS WHERE Card_id = %s AND Date_in IS NULL""", (str(chosen['values'][0]),))
        if not count == 0:
            self.warning_window1 = Tkinter.Toplevel(self)
            self.warning_window1.geometry("500x250")
            self.warning_window1.wm_title("Warning message")
            self.warning_window1.grid_rowconfigure(0, weight=1)
            self.warning_window1.grid_columnconfigure(0, weight=1)
            self.headline8 = Tkinter.Label(self.warning_window1,
                                           text="The borrower with ID " + str(
                                               chosen['values'][0]) + " has not returned all the books yet!",
                                           background="Red",
                                           foreground="white",
                                           font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline8.pack(expand=True, fill=Tkinter.BOTH)
            self.headline8.grid(row=0, sticky=Tkinter.E + Tkinter.W)
        else:
            self.warning_window3 = Tkinter.Toplevel(self)
            self.warning_window3.geometry("500x250")
            self.warning_window3.wm_title("Message")
            self.warning_window3.grid_rowconfigure(0, weight=1)
            self.warning_window3.grid_columnconfigure(0, weight=1)
            self.headline10 = Tkinter.Label(self.warning_window3,
                                            text="The borrower with Name " + str(
                                                chosen['text']) + " has paid all the fines! (" + str(
                                                chosen['values'][1]) + ")",
                                            background="Red",
                                            foreground="white",
                                            font="Tahoma 10 bold", anchor="center", relief="groove")
            self.headline10.pack(expand=True, fill=Tkinter.BOTH)
            self.headline10.grid(row=0, sticky=Tkinter.E + Tkinter.W)
            self.cursor.execute("""
                                                UPDATE FINES, BOOK_LOANS, BORROWER SET FINES.Paid=1 WHERE FINES.Loan_id=BOOK_LOANS.Loan_id AND BOOK_LOANS.Card_id=BORROWER.Card_id
                                                AND BORROWER.Card_id=%s
                                                """, (chosen['values'][0],))

        self.connecttodb.commit()

def main():
    root = Tkinter.Tk()
    Library(root)
    root.mainloop()

if __name__ == "__main__":
    main()