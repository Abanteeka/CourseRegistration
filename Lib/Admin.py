# add students--> give password to change by themselves
# delete student reset password
# add/delete course
# access course section
# sha256 add to database password

import mysql.connector


def admin(registration, name, PASSWD):
    con = mysql.connector.connect(host="localhost", user="root", passwd=PASSWD, database="courseregistration")
    cur = con.cursor()
    while True:
        print("")
        print("{}           {}             {}".format(name, registration, "date"))
        print("1.Add Student")
        print("2.Delete Student")
        print("3.Add Course")
        print("4.Delete Course")
        print("5.Course Section")
        #print("3.Logout")

        user_option = int(input("Options: "))
        if user_option == 1:
            course_name = input("Enter Course Name: ")
            qry = "select * from table where course = {};".format(course_name)
            cur.execute(qry)
            sl1 = cur.fetchall()
            for i in sl1:
                for j in i:
                    c = j
        elif user_option == 2:
            print("Routine :")
        elif user_option == 3:
            break
        else:
            print("Wrong Option!! Try Again")


