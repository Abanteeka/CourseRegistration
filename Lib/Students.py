import datetime
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
    while True:
        print("")
        print("{}           {}             {}".format(name, registration, datetime.time))
        print("><><><><><><><><><><><><><><><><><><><><>< OPTIONS ><><><><><><><><><><><><><><><><><><><><><")
        print("1.search course")
        print("2.select course")
        print("3.routine")
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
            print()
        elif user_option == 3:
            print()
        elif user_option == 4:
            break
        else:
            print("Wrong Option!! Try Again")
