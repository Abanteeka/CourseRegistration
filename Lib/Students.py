import datetime
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="1340",database="bookstore")
cur=con.cursor()


# Login
# search course
# select course
# access course routine
# change password

def studentsession(registration):
    while 1:
        print("")
        print("1.search course")
        print("2.select course")
        print("3.routine")
def students():
    print("")
    print("Student Login")
    print("")
    registration = input(str("Username: "))
    password = input(str("password: "))
    s1 = (registration,password)
    cur.execute("""select * from student;""")
    r = cur.fetchall()
    if cur.rowcount <= 0:
        print("Invalid Login Details")
    else:
        studentsession(registration)
    # while True:
    #     # manu
    #     print("{}           {}             {}".format(name, registration, datetime.time))
    #     break
