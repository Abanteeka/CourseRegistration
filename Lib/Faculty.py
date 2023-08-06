import mysql.connector
import hashlib
from datetime import datetime
import pandas as pd
import numpy as np


# access course table
# login


def faculty(registration, name, pass_wd):
    con = mysql.connector.connect(host="localhost", user="root", passwd=pass_wd, database="courseregistration")
    cur = con.cursor()
    a = datetime.now()
    print("%s       %s:%s" % (a.date(), a.hour, a.minute))
    print("{}           {}".format(name, registration))
    while True:
        print("")
        print("><><><><><><><><><><><><><><><><><><><><>< OPTIONS ><><><><><><><><><><><><><><><><><><><><><")
        print("1.search course")
        print("2.routine")
        print("3.Reset Password")
        print("4.Logout")

        user_option = int(input("Options: "))
        if user_option == 1:
            print("---------Course Search----------")
            print("1. Search By Course ID")
            print("2. Search By Course Name")
            print("3. All Course")
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
            elif User_Option == 3:
                cur.execute("select * from course_data;")
                m = cur.fetchall()
                df = pd.DataFrame(m)
                df.rename(columns={0: 'Course Id'}, inplace=True)
                df.rename(columns={1: 'Course Name'}, inplace=True)
                df.rename(columns={2: 'Description'}, inplace=True)
                df.index = np.arange(1, len(df) + 1)
                print(df)
            else:
                print("Invalid Option,try again!!")


        elif user_option == 2:
            Course = input("Enter Course Code :")
            cur.execute("select * from course_data where course_id = '{}';".format(Course))
            m = cur.fetchall()
            if m:
                try:
                    g = False
                    cur.execute(
                        "select A11,A12,A13,A14,A15,A16 from  Course_Registration_data where A11='{}';".format(Course))
                    A = cur.fetchall()
                    if A:
                        g = True
                    else:
                        A = [('', '', '', '', '', '')]
                    cur.execute(
                        "select B11,B12,B13,B14,B15,B16 from  Course_Registration_data where B11='{}';".format(Course))
                    B = cur.fetchall()
                    if B:
                        g = True
                    else:
                        B = [('', '', '', '', '', '')]
                    cur.execute(
                        "select C11,C12,C13,C14,C15,C16 from  Course_Registration_data where C11='{}';".format(Course))
                    C = cur.fetchall()
                    if C:
                        g = True
                    else:
                        C = [('', '', '', '', '', '')]
                    cur.execute(
                        "select D11,D12,D13,D14,D15,D16 from  Course_Registration_data where D11='{}';".format(Course))
                    D = cur.fetchall()
                    if D:
                        g = True
                    else:
                        D = [('', '', '', '', '', '')]
                    cur.execute(
                        "select E11,E12,E13,E14,E15,E16 from  Course_Registration_data where E11='{}';".format(Course))
                    E = cur.fetchall()
                    if E:
                        g = True
                    else:
                        E = [('', '', '', '', '', '')]
                    cur.execute(
                        "select F11,F12,F13,F14,F15,F16 from  Course_Registration_data where F11='{}';".format(Course))
                    F = cur.fetchall()
                    if F:
                        g = True
                    else:
                        F = [('', '', '', '', '', '')]
                    cur.execute(
                        "select G11,G12,G13,G14,G15,G16 from  Course_Registration_data where F11='{}';".format(Course))
                    G = cur.fetchall()
                    if G:
                        g = True
                    else:
                        G = [('', '', '', '', '', '')]
                    if not g:
                        print("Course Not Registered")
                        break
                    Mon = [A[0][0], B[0][0], C[0][0], D[0][0], E[0][0], F[0][0], G[0][0]]
                    Tue = [A[0][1], B[0][1], C[0][1], D[0][1], E[0][1], F[0][1], G[0][1]]
                    Wed = [A[0][2], B[0][2], C[0][2], D[0][2], E[0][2], F[0][2], G[0][2]]
                    Thu = [A[0][3], B[0][3], C[0][3], D[0][3], E[0][3], F[0][3], G[0][3]]
                    Fri = [A[0][4], B[0][4], C[0][4], D[0][4], E[0][4], F[0][4], G[0][4]]
                    Sat = [A[0][5], B[0][5], C[0][5], D[0][5], E[0][5], F[0][5], G[0][5]]

                    print("Course Selected :")
                    print(
                        "\033[3m    {:^7}	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                            "Theory", "Start", "08:30", "10:05", "11:40", "13:15", "14:50", "16:25", "18:00"))
                    print(
                        "         	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}\033[0m".format(
                            "End", "10:00", "11:35", "13:10", "14:45", "16:20", "17:55", "19:30"))
                    print("-" * 121)
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
                    print("-" * 121)
                except mysql.connector.Error as error:
                    print("Course Not Registered")
            else:
                print("Course Not found!!")
        elif user_option == 3:
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

        elif user_option == 4:
            break
        else:
            print("Wrong Option!! Try Again")
