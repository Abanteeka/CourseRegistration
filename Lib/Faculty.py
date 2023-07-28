import mysql.connector
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
        print("3.Logout")

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
        elif user_option == 3:
            break
        else:
            print("Wrong Option!! Try Again")
