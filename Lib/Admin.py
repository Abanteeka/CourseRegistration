# add students--> give password to change by themselves
# delete student reset password
# add/delete course
# access course section
# sha256 add to database password
import random
import hashlib
import pandas as pd
import numpy as np
import mysql.connector
from datetime import datetime


def admin(registration, name, PASSWD):
    con = mysql.connector.connect(host="localhost", user="root", passwd=PASSWD, database="courseregistration")
    cur = con.cursor()
    a = datetime.now()
    print(
        "%s                 %s      %s                    %s:%s" % (a.date(), registration, name, a.hour, a.minute))

    def generatePassRandom():
        l1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        w = ""
        i = 0
        while i < 5:
            w = w + random.choice(l1)
            i += 1
        return w

    while True:
        print("><><><><><><><><><><><><><><><><><><><><>< OPTIONS ><><><><><><><><><><><><><><><><><><><><><")
        print("1.Add Student")  # in working state
        print("2.Add Faculty")   # in working state
        print("3.Delete Student")  # in working state
        print("4.Delete Faculty")  # in working state
        print("5.Add Course")  # in working state
        print("6.Show Course")  # in working state
        print("7.Delete Course")  # in working state
        print("8.Reset Password")  # in working state
        print("9.Show Student Lists")  # in working state
        print("10.Show Faculty Lists")  # in working state
        print("11.Assign Course")
        print("12.Logout")

        user_option = int(input("Options: "))

        # Add Student
        if user_option == 1:
            student_name = input("Enter Student Name : ")
            Admission_year = input("Enter Admission Year : ")
            Email = input("Enter Email Id : ")
            course = " "

            print()
            print("---------Select Course----------")
            print("1.CSE Core")
            print("2.CSE Cyber Security and Digital Forensics")
            print("3.CSE Aiml")
            print("4.CSE Gaming")
            print("5.CSE Health Informatics")

            User_Input1 = int(input("Enter Your Choice :"))
            if User_Input1 == 1:
                course = "BCE"
            elif User_Input1 == 2:
                course = "BCY"
            elif User_Input1 == 3:
                course = "BAI"
            elif User_Input1 == 4:
                course = "BCG"
            elif User_Input1 == 5:
                course = "BHI"
            else:
                print("invalid Option")

            # generate reg. no.
            a = str(Admission_year)
            w = str(a[2]) + str(a[3]) + str(course)
            qry1 = "select studentID from student where studentID like '{}%';".format(w)
            cur.execute(qry1)
            rn = cur.fetchall()
            # generate 21BCE10000 if !rn
            if rn:
                rn1 = rn[len(rn) - 1][0]
            else:
                rn1 = w + "10000"
            s1 = ""
            for i in range(5, 10):
                s1 = s1 + rn1[i]
            k = int(s1)
            k = k + 1
            k = str(k)
            for j in range(0, 5 - len(k)):
                k = '0' + k
            w = w + k
            qry2 = " insert into student values('{}','{}','{}');".format(w, student_name, Email)
            cur.execute(qry2)
            new_pass = generatePassRandom()
            cur.execute("select MAX(slno) from login;")
            g = cur.fetchall()
            cur.execute("insert into login values('{}','{}','{}','{}')".format(g[0][0], w, hashlib.sha256(
                new_pass.encode('utf-8')).hexdigest(), 'S'))
            print("Student Added Successfully")
            print("Registration No. : {}".format(w))
            print("Password : {}".format(new_pass))
            con.commit()

        #Add faculty
        elif user_option == 2:
            faculty_name = input("Enter Faculty Name : ")
            hiring_year = input("Enter Hiring Year : ")
            email = input("Enter Email Id : ")
            course = " "
            print()
            print("---------Faculty Specialization----------")
            print("1.CSE Core")
            print("2.CSE Cyber Security and Digital Forensics")
            print("3.CSE Aiml")
            print("4.CSE Gaming")
            print("5.CSE Health Informatics")

            User_Input1 = int(input("Enter Your Choice :"))
            if User_Input1 == 1:
                course = "FCE"
            elif User_Input1 == 2:
                course = "FCY"
            elif User_Input1 == 3:
                course = "FAI"
            elif User_Input1 == 4:
                course = "FCG"
            elif User_Input1 == 5:
                course = "FHI"
            else:
                print("invalid Option")

            # generate reg. no.
            a = str(hiring_year)
            w = str(a[2]) + str(a[3]) + str(course)
            qry1 = "select facultyID from faculty where facultyID like '{}%';".format(w)
            cur.execute(qry1)
            rn = cur.fetchall()
            # generate 21FCY10000 if !rn
            if rn:
                rn1 = rn[len(rn) - 1][0]
            else:
                rn1 = w + "10000"
            s1 = ""
            for i in range(5, 10):
                s1 = s1 + rn1[i]
            k = int(s1)
            k = k + 1
            k = str(k)
            for j in range(0, 5 - len(k)):
                k = '0' + k
            w = w + k
            qry2 = " insert into faculty values('{}','{}','{}');".format(w, faculty_name, email)
            cur.execute(qry2)
            new_pass = generatePassRandom()
            cur.execute("select MAX(slno) from login;")
            g = cur.fetchall()
            cur.execute("insert into login values('{}','{}','{}','{}')".format(g[0][0], w, hashlib.sha256(
                new_pass.encode('utf-8')).hexdigest(), 'F'))
            print("Faculty Added Successfully")
            print("Registration No. : {}".format(w))
            print("Password : {}".format(new_pass))
            con.commit()
        #Delete Student
        elif user_option == 3:
            a = input("Enter Reg :")
            cur.execute("select * from student where studentID ='{}';".format(a))
            m = cur.fetchall()
            if m:
                k = input("Do You want [Y/N] : ")
                if k == 'y':
                    cur.execute("delete from student where studentID = '{}'".format(a))
                    # students , login
                    cur.execute("delete from login where usrname = '{}'".format(a))
                    con.commit()
                    print("deleted successful")
                else:
                    print("Thank You")
                    break
            else:
                print("User Not Found")

        #Delete Faculty
        elif user_option == 4:
            a = input("Enter Reg :")
            cur.execute("select * from faculty where facultyID ='{}';".format(a))
            m = cur.fetchall()
            if m:
                k = input("Do You want [y/N] : ")
                if k == 'Y':
                    cur.execute("delete from faculty where facultyID = '{}'".format(a))
                    # students , login
                    cur.execute("delete from login where usrname = '{}'".format(a))
                    con.commit()
                    print("delete successful")
                else:
                    print("Thank You")
                    break
            else:
                print("User Not Found")
        #Add Course
        elif user_option == 5:
            ID = input("Enter Course Code :")
            Name = input("Enter Course Name :")
            Description = input("Enter Description :")
            m = input("Confirm Upload?[Y/N] : ")
            if m == 'Y' or m == 'y' or m == 'yes' or m == 'Yes' or m == 'YES':
                cur.execute("insert into course_data values('{}','{}','{}');".format(ID, Name, Description))
                con.commit()
                print("Data update Successful")
            else:
                print("Try Again")

        # Show Course
        elif user_option == 6:
            print("---------Course Search----------")
            print("1. Search By Course ID")
            print("2. Search By Course Name")
            User_Option = int(input("Enter Your Choice :"))
            if User_Option == 1:
                course_code = input("Enter course code : ")
                cur.execute("select * from course_data where course_id = '{}';".format(course_code))
                m = cur.fetchall()
                df = pd.DataFrame(m)
                df.rename(columns={0: 'Course Id'}, inplace=True)
                df.rename(columns={1: 'Course Name'}, inplace=True)
                df.rename(columns={2: 'Description'}, inplace=True)
                df.index = np.arange(1, len(df) + 1)
                print(df)
            elif User_Option == 2:
                Cname = input("Enter Course Name : ")
                cur.execute("select * from course_data where course_name = '{}';".format(Cname))
                m = cur.fetchall()
                df = pd.DataFrame(m)
                df.rename(columns={0: 'Course Id'}, inplace=True)
                df.rename(columns={1: 'Course Name'}, inplace=True)
                df.rename(columns={2: 'Description'}, inplace=True)
                df.index = np.arange(1, len(df) + 1)
                print(df)

        # Delete course
        elif user_option == 7:
            course_code = input("Enter course code : ")
            cur.execute("select * from course_data where course_id ='{}';".format(course_code))
            m = cur.fetchall()
            if m:
                k = input("Do You want [y/N]")
                if k == 'Y':
                    cur.execute("delete from course_data where course_id = '{}'".format(course_code))
                    con.commit()
                    print("delete successful")
                else:
                    print("Thank You")
                    break
            else:
                print("Course Not Found")

        #Reset Password
        elif user_option == 8:
            while True:
                print("1.Admin Password")
                print("2.Student Password")
                print("3.Faculty Password")
                print("4.Cancel")
                m = int(input("Enter Your Choice :"))
                if m == 1:
                    k = input("Enter Old password :")
                    cur.execute("select password from login where usrname='{}';".format(name))
                    g = cur.fetchall()
                    if hashlib.sha256(k.encode('utf-8')).hexdigest() == g[0][0]:
                        n1 = input("Enter New Password :")
                        n2 = input("Re-Enter Password :")
                        if n1 == n2:
                            cur.execute("update login set password='{}' where usrname='{}';".format(
                                hashlib.sha256(n1.encode('utf-8')).hexdigest(), name))
                            print("Password Update Successful")
                            con.commit()
                        else:
                            print("Password Not matched. Try again!!")
                    else:
                        print("Wrong Password")
                elif m == 2:
                    k = input("Enter Registration No. of the Student:")
                    x = generatePassRandom()
                    cur.execute("update login set password='{}' where usrname='{}';".format(
                        hashlib.sha256(x.encode('utf-8')).hexdigest(), k))
                    con.commit()
                    print("Password Reset Successful")
                    print("New Password is : {}".format(x))
                    print("Thank You")
                    con.commit()
                elif m == 3:
                    k = input("Enter Registration No. of the Faculty : ")
                    x = generatePassRandom()
                    cur.execute("update login set password='{}' where usrname='{}';".format(
                        hashlib.sha256(x.encode('utf-8')).hexdigest(), k))
                    con.commit()
                    print("Password Reset Successful")
                    print("New Password is : {}".format(x))
                    print("Thank You")
                elif m == 4:
                    break
                else:
                    print("Wrong Option Try Again")

        #show student list
        elif user_option == 9:
            print("---------Student Search----------")
            print("1. Search By Student ID")
            print("2. Search By Admission Year")
            print("3. Search By Course Specialization")
            User_Option = int(input("Enter Your Choice : "))
            if User_Option == 1:
                Id = input("Enter Student's Registration Number : ")
                cur.execute("select * from student where studentID = '{}';".format(Id))
                m = cur.fetchall()
                if m:
                    df = pd.DataFrame(m)
                    df.rename(columns={0: 'Registration Number'}, inplace=True)
                    df.rename(columns={1: 'Name'}, inplace=True)
                    df.rename(columns={2: 'Email ID'}, inplace=True)
                    df.index = np.arange(1, len(df) + 1)
                    print(df)
                else:
                    print("No Faculty Is Available")

            elif User_Option == 2:
                J = input("Enter Admission Year : ")
                cur.execute("select * from student where studentID like '{}%';".format(J[2]+J[3]))
                m = cur.fetchall()
                if m:
                    df = pd.DataFrame(m)
                    df.rename(columns={0: 'Registration Number'}, inplace=True)
                    df.rename(columns={1: 'Name'}, inplace=True)
                    df.rename(columns={2: 'Email ID'}, inplace=True)
                    df.index = np.arange(1, len(df) + 1)
                    print(df)
                else:
                    print("No Student Is Available")
                        # if given registration year is not available
            elif User_Option == 3:
                print("---------Student Specialization----------")
                print("1.CSE Core")
                print("2.CSE Cyber Security and Digital Forensics")
                print("3.CSE Aiml")
                print("4.CSE Gaming")
                print("5.CSE Health Informatics")
                category = " "
                User_Input1 = int(input("Enter Your Choice :"))
                if User_Input1 == 1:
                    category = "BCE"
                elif User_Input1 == 2:
                    category = "BCY"
                elif User_Input1 == 3:
                    category = "BAI"
                elif User_Input1 == 4:
                    category = "BCG"
                elif User_Input1 == 5:
                    category = "BHI"
                else:
                    print("invalid Option")
                    category = "no"
                if category == "no":
                    print("wrong option")
                else:
                    cur.execute("select * from student where studentID like '%{}%';".format(category))
                    m = cur.fetchall()
                    if m:
                        df = pd.DataFrame(m)
                        df.rename(columns={0: 'Registration Number'}, inplace=True)
                        df.rename(columns={1: 'Name'}, inplace=True)
                        df.rename(columns={2: 'Email ID'}, inplace=True)
                        df.index = np.arange(1, len(df) + 1)
                        print(df)
                    else:
                        print("No student is found in this course")

        #Show Faculty Lists
        elif user_option == 10:
            print("---------Faculty Search----------")
            print("1. Search By Faculty ID")
            print("2. Search By Joining Year")
            print("3. Search By Course Specialization")
            User_Option = int(input("Enter Your Choice : "))
            if User_Option == 1:
                Id = input("Enter Faculty's Registration Number : ")
                cur.execute("select * from faculty where facultyID = '{}';".format(Id))
                m = cur.fetchall()
                if m:
                    df = pd.DataFrame(m)
                    df.rename(columns={0: 'Registration Number'}, inplace=True)
                    df.rename(columns={1: 'Name'}, inplace=True)
                    df.rename(columns={2: 'Email ID'}, inplace=True)
                    df.index = np.arange(1, len(df) + 1)
                    print(df)
                else:
                    print("No Faculty Is Available")

            elif User_Option == 2:
                J = input("Enter Joining Year : ")
                cur.execute("select * from faculty where facultyID like '{}%';".format(J[2]+J[3]))
                m = cur.fetchall()
                if m:
                    df = pd.DataFrame(m)
                    df.rename(columns={0: 'Registration Number'}, inplace=True)
                    df.rename(columns={1: 'Name'}, inplace=True)
                    df.rename(columns={2: 'Email ID'}, inplace=True)
                    df.index = np.arange(1, len(df) + 1)
                    print(df)
                else:
                    print("No Faculty Is Available")

            elif User_Option == 3:
                print("---------Faculty Specialization----------")
                print("1.CSE Core")
                print("2.CSE Cyber Security and Digital Forensics")
                print("3.CSE Aiml")
                print("4.CSE Gaming")
                print("5.CSE Health Informatics")
                category = " "
                User_Input1 = int(input("Enter Your Choice : "))
                if User_Input1 == 1:
                    category = "FCE"
                elif User_Input1 == 2:
                    category = "FCY"
                elif User_Input1 == 3:
                    category = "FAI"
                elif User_Input1 == 4:
                    category = "FCG"
                elif User_Input1 == 5:
                    category = "FHI"
                else:
                    print("invalid Option")
                    category = "no"
                if category == "no":
                    print("wrong option")
                else:
                    cur.execute("select * from faculty where facultyID like '%{}%';".format(category))
                    m = cur.fetchall()
                    if m:
                        df = pd.DataFrame(m)
                        df.rename(columns={0: 'Registration Number'}, inplace=True)
                        df.rename(columns={1: 'Name'}, inplace=True)
                        df.rename(columns={2: 'Email ID'}, inplace=True)
                        df.index = np.arange(1, len(df) + 1)
                        print(df)
                    else:
                        print("No Course found")
        #Assign Course
        elif user_option == 11:
            print()
        #logout
        elif user_option == 12:
            break
        else:
            print("Wrong Option!! Try Again")
