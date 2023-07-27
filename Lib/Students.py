import datetime
import mysql.connector


# Login
# search course
# select course
# access course routine
# change password

def students(registration, name, Passwd):
    con = mysql.connector.connect(host="localhost", user="root", passwd=Passwd, database="courseregistration")
    cur = con.cursor()
    while True:
        print("")
        print("{}           {}             {}".format(name, registration, datetime.time))
        print("1.search course")
        print("2.select course")
        print("3.routine")
        print("4.Logout")

        user_option = int(input("Options: "))
        if user_option == 1:
            course_name = input("Enter Course Name: ")
            qry = "select * from table where course = {};".format(course_name)
            cur.execute(qry)
            sl = cur.fetchall()
            c = 0
            for i in sl:
                for j in i:
                    c = j
        elif user_option == 2:
            print()
        elif user_option == 3:
            print()
        elif user_option == 4:
            break
        else:
            print("Wrong Option!! Try Again")
