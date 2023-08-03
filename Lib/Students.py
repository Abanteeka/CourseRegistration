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
        print("3.Reset Routine")
        print("4.Show routine")
        print("5.Reset Password")
        print("6.Logout")
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
            def Course_print():
                cur.execute("Select * from course_data;")
                m = cur.fetchall()
                df = pd.DataFrame(m)
                df.rename(columns={0: 'Course Id'}, inplace=True)
                df.rename(columns={1: 'Course Name'}, inplace=True)
                df.rename(columns={2: 'Description'}, inplace=True)
                df.index = np.arange(1, len(df) + 1)
                print(df)

            while True:
                print("1. Course List")
                print("2. Select Course")
                print("3. Exit")
                k = int(input("Enter Your Choice : "))
                if k == 1:
                    Course_print()
                elif k == 2:
                    cur.execute("select * from Course_Registration_data where regno='{}';".format(registration))
                    h = cur.fetchall()
                    if h:
                        print("Already Course Set!!")
                        print("If you wish to change please reset the time table")
                        print("Thank You")
                        break
                    Mon = ["A11", "B11", "C11", "D11", "E11", "F11", "G11"]
                    Tue = ["A12", "B12", "C12", "D12", "E12", "F12", "G12"]
                    Wed = ["A13", "B13", "C13", "D13", "E13", "F13", "G13"]
                    Thu = ["A14", "B14", "C14", "D14", "E14", "F14", "G14"]
                    Fri = ["A15", "B15", "C15", "D15", "E15", "F15", "G15"]
                    Sat = ["A16", "B16", "C16", "D16", "E16", "F16", "G16"]
                    unused_slot = ["A1", "B1", "C1", "D1", "E1", "F1", "G1"]

                    def Print_time_table():
                        print("Course Selected :")
                        print(
                            "    {:^7}	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                                "Theory", "Start", "08:30", "10:05", "11:40", "13:15", "14:50", "16:25", "18:00"))
                        print(
                            "         	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
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

                    def Make_Blank(l):
                        L = ["A11", "B11", "C11", "D11", "E11", "F11", "G11", "A12", "B12", "C12", "D12", "E12", "F12",
                             "G12", "A13", "B13", "C13", "D13", "E13", "F13", "G13", "A14", "B14", "C14", "D14", "E14",
                             "F14", "G14", "A15", "B15", "C15", "D15", "E15", "F15", "G15", "A16", "B16", "C16", "D16",
                             "E16", "F16", "G16"]

                        for i in range(0, len(l)):
                            if l[i] in L:
                                l[i] = " "

                    def Registration_final(Mon, Tue, Wed, Thu, Fri, Sat):
                        Make_Blank(Mon)
                        Make_Blank(Tue)
                        Make_Blank(Wed)
                        Make_Blank(Thu)
                        Make_Blank(Fri)
                        Make_Blank(Sat)
                        cur.execute(
                            "insert into Course_Registration_data values('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
                                registration, Mon[0], Tue[0], Wed[0], Thu[0], Fri[0], Sat[0], Mon[1], Tue[1], Wed[1],
                                Thu[1], Fri[1],
                                Sat[1], Mon[2], Tue[2], Wed[2], Thu[2], Fri[2], Sat[2], Mon[3], Tue[3], Wed[3], Thu[3],
                                Fri[3], Sat[3], Mon[4], Tue[4], Wed[4], Thu[4], Fri[4], Sat[4], Mon[5], Tue[5], Wed[5],
                                Thu[5], Fri[5], Sat[5], Mon[6], Tue[6], Wed[6], Thu[6], Fri[6], Sat[6]))
                        con.commit()
                        print()
                        print("Registration Successful")
                        print()

                    l = []
                    while True:
                        Print_time_table()
                        while True:
                            cl = input("Show Course List? [y/N]")
                            if cl == 'y' or cl == 'Y':
                                Course_print()
                            course_code = input("Enter The Course Code : ")
                            cur.execute("select * from course_data where course_id ='{}';".format(course_code))
                            g = cur.fetchall()
                            if g:
                                if course_code in l:
                                    print("Course Register!!")
                                    print("Try Another Course")
                                    break
                                else:
                                    l.append(course_code)
                                    print("Available Slots :")
                                    for i in range(0, len(unused_slot)):
                                        print("| {} |".format(unused_slot[i]), end='')
                                    print()
                                    slot = input("Enter The Slot : ")
                                    if slot in unused_slot:
                                        index = unused_slot.index(slot)
                                        Mon[index] = Tue[index] = Wed[index] = Thu[index] = Fri[index] = Sat[
                                            index] = course_code
                                        unused_slot.remove(slot)
                                        print("Slot Added")
                                    else:
                                        print("Slot Filled Up!!")
                                        print("Try Another")
                                    if len(unused_slot) == 0:
                                        print("All Slots are filled")
                                        break
                                    Print_time_table()
                                    x = input("Do you want to add more Course ?[Y/n] : ")
                                    if x == 'N' or x == 'n':
                                        break
                            else:
                                print("Course Not Found")
                                h = input("Do you want to exit? [y/N] :")
                                if h == 'y' or h == 'Y':
                                    break
                                print("Try Again!!")
                        Print_time_table()
                        y = input("Confirm Course ?[Y/n] : ")
                        if y == 'N' or y == 'n':
                            print("Re-Try")
                            break
                        else:
                            # save the commit
                            Registration_final(Mon, Tue, Wed, Thu, Fri, Sat)
                            break
                elif k == 3:
                    break
                else:
                    print("Invalid Option!! Try Again")

        elif user_option == 3:
            try:
                cur.execute("select * from Course_Registration_data where regno='{}';".format(registration))
                h = cur.fetchall()
                if h:
                    m = input("Confirm Reset Time Table?[y/N]")
                    if m == 'Y' or m == 'y':
                        cur.execute("delete from Course_Registration_data where regno='{}';".format(registration))
                        con.commit()
                        print("Reset Successful")
                    else:
                        print("Thank You")
                else:
                    print("No record Found")
            except mysql.connector.Error as error:
                print("Course Not Registered")
        elif user_option == 4:
            # print Routine
            try:
                cur.execute("select * from Course_Registration_data where regno='{}';".format(registration))
                h = cur.fetchall()
                if not h:
                    print("Course Not Registered")
                    break
                Mon = [h[0][1], h[0][7], h[0][13], h[0][19], h[0][25], h[0][31], h[0][37]]
                Tue = [h[0][2], h[0][8], h[0][14], h[0][20], h[0][26], h[0][32], h[0][38]]
                Wed = [h[0][3], h[0][9], h[0][15], h[0][21], h[0][27], h[0][33], h[0][39]]
                Thu = [h[0][4], h[0][10], h[0][16], h[0][22], h[0][28], h[0][34], h[0][40]]
                Fri = [h[0][5], h[0][11], h[0][17], h[0][23], h[0][29], h[0][35], h[0][41]]
                Sat = [h[0][6], h[0][12], h[0][18], h[0][24], h[0][30], h[0][36], h[0][42]]

                print("Course Selected :")
                print(
                    "    {:^7}	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
                        "Theory", "Start", "08:30", "10:05", "11:40", "13:15", "14:50", "16:25", "18:00"))
                print(
                    "         	{:7}{:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}	      {:^7}".format(
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
        elif user_option == 5:
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
        elif user_option == 6:
            break
        else:
            print("Wrong Option!! Try Again")
