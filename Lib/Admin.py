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
        print("5.Show Course")
        print("6.Change Password")
        print("7.Logout")

        user_option = int(input("Options: "))
        if user_option == 1:
            student_name = input("Enter Student Name : ")
            Admission_year = input("Enter Admission Year : ")
            #course = input
            #-1 from last roll no. || "select registerno. from {} where registerno is like "{}{}%"".format()
            # course = {"CSE CYBER SECURITY":"BCY","":""}
            while True : #options 1 cse core 2 cyber
                print("---------Select Course----------")
                print("1.CSE Core")
                print("2.CSE Cyber Security and Digital Forensics")
                print("3.CSE Aiml")
                print("4.CSE Gaming")
                print("5.CSE Health Informatics")

                User_Input1 = int(input("Enter Your Course"))


            qry = "select * from table where course = {};".format(student_name)
            cur.execute(qry)
            sl1 = cur.fetchall()
            for i in sl1:
                for j in i:
                    c = j
        elif user_option == 2:
            print("Routine :")
        elif user_option == 7:
            break
        else:
            print("Wrong Option!! Try Again")


