import mysql.connector

#TO CREATE AND CONNECT WITH DATABASE

def create_database():
    con1 = mysql.connector.connect(host = "localhost", user = "root", password = "")
    if con1.is_connected():
        print("**~~CONNECTION SUCCESS~~**")
    else:
        print("**~~CONNECTION FAILED~~**")
    cur1 = con1.cursor()
    cur1.execute("create database bill;")
    print("=============================================================")
    cur1.execute("use bill;")
    print("SUCCESS IN CONNECTING WITH DATABASE")

def user_password():
    # CREATING TABLE FOR STORING THE USERNAME AND PASSWORD OF THE USER
    my = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    mycursor = my.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS user_data(username varchar(30) PRIMARY KEY, password varchar(30) DEFAULT'000')")




#TO CREATE TABLE

def create_table():
    con2 = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    print()
    cur2 = con2.cursor()
    cur2.execute("create table data(SNO int primary key, NAME char(20), PRODCODE int, QTY int, PRICE float, SUB_TOTAL float,  DISCOUNT float, TOTAL float);")
    print("TABLE CREATED SUCCESSFULLY")

#FUNCTION TO INSEERT RECORDS IN THE TABLE
def insert():
    con3 = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    cur3 = con3.cursor()
    ch = 'y'
    s = 0
    while ch == 'y' or ch == 'Y':
        print()
        s += 1
        n = input("Enter ITEM NAME here = ")
        c = int(input("Enter PRODUCT CODE here = "))
        q = int(input("Enter QUANTITY here = "))
        p = float(input("Enter PRODUCT PRICE here = "))
        s_t = (q*p)
        d = 0
        if s_t > 100 and s_t < 199 and p < 20:
            d = 2
        elif s_t > 200 and s_t < 499 and p < 20:
            d = 3
        elif s_t > 500 and s_t < 999 and p < 20:
            d = 5
        elif s_t > 1000 and s_t < 4999 and p < 20:
            d = 10
        elif s_t > 5000 and s_t < 6999 and p < 20:
            d = 20
        elif s_t > 7000 and s_t < 9999 and p < 20:
            d = 30
        elif s_t > 10000 and s_t < 25000 and p < 200:
            d = 50
        # above 20
        elif s_t > 2000 and s_t < 4999 and p < 100:
            d = 13
        elif s_t > 5000 and s_t < 9999 and p < 100:
            d = 15
        elif s_t > 10000 and s_t < 49999 and p < 100:
            d = 20
        elif s_t > 50000 and s_t < 69999 and p < 100:
            d = 30
        t = s_t
        if d != 0:
            t = s_t*d/100
        cur3.execute("insert into data values({}, '{}', {}, {}, {}, {}, {}, {});".format(s,n,c,q,p,s_t,d,t))
        con3.commit()
        print("RECORD INSERTED INTO THE TABLE")
        print()
        ch = input("PRESS 'Y' IF YOU WANT TO ENTER MORE RECORDS HERE = ")
        if ch!= 'y':
            cur3.close()

#TO DISPLAY RECORDS
            
def display():
    con4 = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    cur4 = con4.cursor()
    cur4.execute("select * from data;")
    rec = cur4.fetchall()
    for x in rec:
        print("SNO. = ", x[0])
        print("NAME. = ", x[1])
        print("PRODUCT CODE = ", x[2])
        print("QUANTITY = ", x[3])
        print("PRICE = ", x[4])
        print("SUB-TOTAL = ", x[5])
        print("DISCOUNT APPLIED = ", x[6])
        print("TOTAL = ", x[7])
        print("*********************************************************************")
    cur4.close()

#TO SEARCH THE RECORDS

def search():
    con5 = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    cur5 = con5.cursor()
    found = False
    q = input("You want to search with 'NAME' or 'CODE' = ")
    if q == 'name' or q == 'NAME':
        pname = input("Enter the PRODUCT NAME here = ")
        cur5.execute("select * from data where NAME = '{}';".format(pname))
        d = cur5.fetchall()
        for x in d:
            print("SNO. = ", x[0])
            print("NAME. = ", x[1])
            print("PRODUCT CODE = ", x[2])
            print("QUANTITY = ", x[3])
            print("PRICE = ", x[4])
            found = True
        if found == False:
            print("RECORD DOESN'T EXIST")
        else:
            print("RECORD FOUND SUCCESSFULLY")
    elif q == 'code' or q == 'CODE':
        pcode = int(input("Enter the PRODUCT CODE here = "))
        cur5.execute("select * from data where PRODCODE = {};".format(pcode))
        d = cur5.fetchall()
        for x in d:
            print("SNO. = ", x[0])
            print("NAME. = ", x[1])
            print("PRODUCT CODE = ", x[2])
            print("QUANTITY = ", x[3])
            print("PRICE = ", x[4])
            found = True
        if found == False:
            print("RECORD DOESN'T EXIST")
        else:
            print("RECORD FOUND SUCCESSFULLY")
    cur5.close()

#UPDATING RECORDS OF THE TABLE

def update():
    r = int(input("Enter desired PRODUCT CODE her = "))
    ans = 'y'
    while ans == 'y':
        print("~~~**SELECT SUITABLE  FIELD YOU WISH TO CHANGE**~~~")
        print("1.) NAME")
        print("2.) QUANTITY")
        print("3.) PRICE")
        x = int(input("Enter serial no. of your choice here = "))
        if x == 1:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
            c = con.cursor()
            name = input("Enter new NAME here = ")
            c.execute("update data set NAME = '{}' where PRODCODE = {};".format(name, r))
            con.commit()
            print("NAME OF PRODUCT UPDATED")
        elif x == 2:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
            c = con.cursor()
            qty = input("Enter new QUANTITY here = ")
            c.execute("update data set QTY = '{}' where PRODCODE = {};".format(qty, r))
            con.commit()
            print("QUANTITY OF PRODUCT UPDATED")
        elif x == 3:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
            c = con.cursor()
            p = input("Enter new PRICE here = ")
            c.execute("update data set PRICE = '{}' where PRODCODE = {};".format(p, r))
            con.commit()
            print("PRICE OF PRODUCT UPDATED")
        ans = input("Do you wish to run more updates?(Y/N)\n")
        if ans.lower()!= 'y':
            c.close()

#TO DELETE RECORDS

def delete_r():
    con = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    c = con.cursor()
    print("YOU HAVE 3 OPTIONS HERE")
    print("1.) TO DELETE ANY ONE PARTICULAR RECORD")
    print("2.) TO DELETE ALL THE RECORDS")
    print("3.) NO RECORD TO BE DELETED")
    ch = int(input("Enter your choice = "))
    if ch == 1:
        s = int(input("Enter serial no. here = "))
        c.execute("delete from data where SNO = {};".format(s))
        con.commit()
        print("~~~**RECORD SUCCESSFULLY DELETED**~~~")
    elif ch == 2:
        c.execute("delete from data;")
        con.commit()
        print("~~~**RECORDS SUCCESSFULLY DELETED**~~~")
    elif ch == 3:
        print("~~~**NO RECORDS DELETED**~~~")
    c.close()

def login():
    print('\n1. SIGN IN (LOGIN)', '2. SIGN UP (REGISTER)', sep='\n')

    r = int(input("ENTER YOUR CHOICE:"))
    if r == 1:
        sign_in()
    if r == 2:
        register()


def sign_in():
    
    # PRINTING THE SIGNIN OPTION AGAIN TO THE USER AFTER REGISTRATION

    print("SIGN IN")
    un = input("ENTER THE USERNAME!!:")
    ps = input("ENTER THE PASSWORD!!:")
    my = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    mycursor = my.cursor()
    mycursor.execute("SELECT password FROM user_data WHERE username='" + un + "'")
    row = mycursor.fetchall()
    for i in row:
        a = list(i)
        if a[0] == str(ps):
            ans = 'y'
            while ans == 'y' or ans == 'Y':
                print("1.) INSERT RECORDS")
                print("2.) DISPLAY RECORDS")
                print("3.) SEARCH RECORDS")
                print("4.) UPDATE RECORDS")
                print("5.) DELETE RECORDS")
                print()
                ch = int(input("ENTER YOUR CHOICE HERE = "))
                if ch == 1:
                    insert()
                elif ch == 2:
                    display()
                elif ch == 3:
                    search()
                elif ch == 4:
                    update()
                elif ch == 5:
                    delete_r()
                else:
                    print("&&&&SORRY YOU HAVE ENTERED WRONG CHOICE&&&&")
                print()
                ans = input(">>>>>>WANT TO RUN AGAIN?(Y/N)<<<<<<\n")
                if ans!= 'y' or ans!= 'Y':
                    print("======THANKS FOR ACCESSING MY PROJECT======")

def register():
    print("PLEASE REGISTER YOURSELF")
    u = input("ENTER YOUR NEW USERNAME:")
    p = input("ENTER YOUR NEW PASSWORD:")

    # ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
    my = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bill")
    mycursor = my.cursor()
    mycursor.execute(f"INSERT INTO user_data VALUES('{u}','{p}')")
    my.commit()

    print("REGISTERED SUCCESSFULLY")

#_main_

print("  █║▌│ █│║▌ ║││█║▌ │║║█║ │║║█║  █║▌│ █│║▌ ║││█║▌ │║║█║ │║║█║  █║▌│ █│║▌ ║││█║▌ │║║█║ │║║█║")
print()
print("##**^^^----WELCOME TO GROCERIES BILLING SYSTEM----^^^**##")
print()
print("###############################################################")
print()
print("~~~~~**LETS START**~~~~\n")
print()
create_database()
create_table()
user_password()
login()
ans = 'y'
while ans == 'y' or ans == 'Y':
    print("1.) INSERT RECORDS")
    print("2.) DISPLAY RECORDS")
    print("3.) SEARCH RECORDS")
    print("4.) UPDATE RECORDS")
    print("5.) DELETE RECORDS")
    print()
    ch = int(input("ENTER YOUR CHOICE HERE = "))
    if ch == 1:
        insert()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        update()
    elif ch == 5:
        delete_r()
    else:
        print("&&&&SORRY YOU HAVE ENTERED WRONG CHOICE&&&&")
    print()
    ans = input(">>>>>>WANT TO RUN AGAIN?(Y/N)<<<<<<\n")
    if ans!= 'y' or ans!= 'Y':
        print("======THANKS FOR ACCESSING MY PROJECT======")









