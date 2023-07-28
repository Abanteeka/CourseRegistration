# add students--> give password to change by themselves
# delete student reset password
# add/delete course
# access course section
# sha256 add to database password

import pandas as pd
import numpy as np
import mysql.connector
from datetime import datetime


def admin(registration, name, PASSWD):
    con = mysql.connector.connect(host="localhost", user="root", passwd=PASSWD, database="courseregistration")
    cur = con.cursor()
    a = datetime.now()
    while True:
        print("")
        print("%s                 %s      %s                    %s:%s" % (a.date(), registration, name, a.hour, a.minute))
        print("><><><><><><><><><><><><><><><><><><><><>< OPTIONS ><><><><><><><><><><><><><><><><><><><><><")
        print("1.Add Student")
        print("2.Delete Student")
        print("3.Add Course")
        print("4.Delete Course")
        print("5.Show Course")
        print("6.Change Password")
        print("7.Show Student Lists")
        print("8.Show Faculty Lists")
        print("9.Assign Course")
        print("10.Logout")

        user_option = int(input("Options: "))

        if user_option == 1:
            student_name = input("Enter Student Name : ")
            Admission_year = input("Enter Admission Year : ")
            Email = input("Enter Email Id : ")
            #course = input
            #-1 from last roll no. || "select registerno. from {} where registerno is like "{}{}%"".format()
            # course = {"CSE CYBER SECURITY":"BCY","":""}
            course = " "

            print("---------Select Course----------")
            print("1.CSE Core")
            print("2.CSE Cyber Security and Digital Forensics")
            print("3.CSE Aiml")
            print("4.CSE Gaming")
            print("5.CSE Health Informatics")

            User_Input1 = int(input("Enter Your Course"))
            if User_Input1==1:
                course = "BCE"
            elif User_Input1==2:
                course = "BCY"
            elif User_Input1==3:
                course = "BAI"
            elif User_Input1==4:
                course = "BCG"
            elif User_Input1==5:
                course = "BHI"
            else:
                print("invalid Option")
            qry = "select * from table where student_name = {};".format(student_name)
            cur.execute(qry)
            sl1 = cur.fetchall()
            for i in sl1:
                for j in i:
                    c = j
        elif user_option == 2:
            print("Routine :")
        elif user_option == 3:
            ID = input("Enter Course Code :")
            Name = input("Enter Course Code :")
            Description = input("Enter Description :")
            m = input("Confirm Upload?[Y/N] :")
            if m == 'Y' or m == 'y' or m == 'yes' or m == 'Yes' or m == 'YES':
                cur.execute("insert into course_data values('{}','{}','{}');".format(ID,Name,Description))
                con.commit()
                print("Data update Successful")
            else:
                print("Try Again")
        elif user_option == 7:
            cur.execute("select * from student;")
            m = cur.fetchall()
            df = pd.DataFrame(m)
            df.rename(columns={0: 'Registration Number'}, inplace=True)
            df.rename(columns={1: 'Name'}, inplace=True)
            df.rename(columns={2: 'Email ID'}, inplace=True)
            df.rename(columns={3: 'Password'}, inplace=True) # delete the coloum
            df.index = np.arange(1, len(df) + 1)
            print(df)

        elif user_option == 10:
            break
        else:
            print("Wrong Option!! Try Again")


