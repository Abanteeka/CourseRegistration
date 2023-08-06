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
    while True:
        print("")
        print("%s       %s:%s" % (a.date(), a.hour, a.minute))
        print("{}           {}".format(name, registration))
        print("1.search course")
        print("2.routine")
        print("3.Reset Password")
        print("4.Logout")

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
            print("Routine :")
            # slot from student
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
