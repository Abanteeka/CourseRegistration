from datetime import datetime
import hashlib
import mysql.connector
import pandas as pd
import numpy as np


# Login
# search course
# select course
# access course routine
# change password


def students(registration, name, Passwd):
    con = mysql.connector.connect(host="localhost", user="root", passwd=Passwd, database="courseregistration")
    cur = con.cursor()
    a = datetime.now()
    print("%s       %s:%s" % (a.date(), a.hour, a.minute))
    print("{}           {}".format(name, registration))
    while True:
        print()
        print("><><><><><><><><><><><><><><><><><><><><>< OPTIONS ><><><><><><><><><><><><><><><><><><><><><")
        print("1.search course")
        print("2.select course")
        print("3.routine")
        print("4.Reset Password")
        print("5.Logout")
        print()
        user_option = int(input("Options: "))
        if user_option == 1:
            course_code = input("Enter Course Code: ")
            cur.execute("select * from course_data where course_id = '{}';".format(course_code))
            m = cur.fetchall()
            df = pd.DataFrame(m)
            df.rename(columns={0: 'Course Id'}, inplace=True)
            df.rename(columns={1: 'Course Name'}, inplace=True)
            df.rename(columns={2: 'Description'}, inplace=True)
            df.index = np.arange(1, len(df) + 1)
            print(df)

        elif user_option == 2:
            while True:
                print("1. Course List")
                print("2. Select Course")
                print("3. Exit")
                k = int(input("Enter Your Choice : "))
                if k == 1:
                    cur.execute("Select * from course_data;")
                    m = cur.fetchall()
                    df = pd.DataFrame(m)
                    df.rename(columns={0: 'Course Id'}, inplace=True)
                    df.rename(columns={1: 'Course Name'}, inplace=True)
                    df.rename(columns={2: 'Description'}, inplace=True)
                    df.index = np.arange(1, len(df) + 1)
                    print(df)
                elif k == 2:
                    Mon = ["A11", "B11", "C11", "A21", "A17", "C21", "D21"]
                    Tue = ["A12", "B12", "C12", "A22", "B17", "C22", "D22"]
                    Wed = ["A13", "B13", "C13", "A23", "C17", "C23", "D23"]
                    Thu = ["A14", "B14", "C14", "A24", "A27", "C24", "D24"]
                    Fri = ["A15", "B15", "C15", "A25", "C27", "C25", "D25"]
                    Sat = ["A16", "B16", "C16", "A26", "D27", "C26", "D26"]
                    while True:
                        print("Course Selected :")
                        print("    {:^7}	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                            "Theory", "Start", "08:30", "10:05", "11:40", "13:15", "14:50", "16:25", "18:00"))
                        print("         	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                            "End", "10:00", "11:35", "13:10", "14:45", "16:20", "17:55", "19:30"))
                        print("-"*121)
                        print(
                            "MON	Theory	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                Mon[0], Mon[1], Mon[2], Mon[3], Mon[4], Mon[5], Mon[6]))
                        print(
                            "TUE	Theory	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                Tue[0], Tue[1], Tue[2], Tue[3], Tue[4], Tue[5], Tue[6]))
                        print(
                            "WED	Theory	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                Wed[0], Wed[1], Wed[2], Wed[3], Wed[4], Wed[5], Wed[6]))
                        print(
                            "THU	Theory	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                Thu[0], Thu[1], Thu[2], Thu[3], Thu[4], Thu[5], Thu[6]))
                        print(
                            "FRI	Theory	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                Fri[0], Fri[1], Fri[2], Fri[3], Fri[4], Fri[5], Fri[6]))
                        print(
                            "SAT	Theory	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                Sat[0], Sat[1], Sat[2], Sat[3], Sat[4], Sat[5], Sat[6]))
                        while True:
                            course_code = input("Enter The Course Code : ")
                            slot = input("Enter The Slot : ")

                            x = input("Do you want to add more Course ?[Y/n] : ")
                            if x == 'N' or x == 'n':
                                break
                        y = input("Confirm Course ?[Y/n] : ")
                        if x == 'N' or x == 'n':
                            print("Re-Try")
                            break
                        else:
                            # save the commit
                            break
                elif k == 3:
                    break
                else:
                    print("Invalid Option!! Try Again")

        elif user_option == 3:
            print()
        elif user_option == 4:
            print("<----------------Reset Password----------------->")
            Old_pass = input("Enter Old Password :")
            cur.execute("select password from login where usrname='{}';".format(registration))
            m = cur.fetchall()
            if hashlib.sha256(Old_pass.encode('utf-8')).hexdigest() == m[0][0]:
                new_pass = input("Enter New Password : ")
                check_pass = input("Re-Enter Password : ")
                if new_pass == check_pass:
                    cur.execute("update login set password='{}' where usrname='{}';".format(
                        hashlib.sha256(new_pass.encode('utf-8')).hexdigest(), registration))
                    con.commit()
                    print("Password Change Successful")
                    break
                else:
                    print("Password Not match")
            else:
                print("Wrong Password")
        elif user_option == 5:
            break
        else:
            print("Wrong Option!! Try Again")
