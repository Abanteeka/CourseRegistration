import mysql.connector


<<<<<<< HEAD
# acess course table
# login

def faculty(registration, name):
    con = mysql.connector.connect(host="localhost", user="root", passwd="1340", database="courseregistration")
=======
# access course table
# login

def faculty(registration, name):
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="courseregistration")
>>>>>>> b46dcbdd99ed6548be9d5e53f16397c6a6e8b532
    cur = con.cursor()
    while True:
        print("")
        print("{}           {}             {}".format(name, registration, "date"))
        print("1.search course")
        print("2.routine")
        print("3.Logout")

        user_option = int(input("Options: "))
        if user_option == 1:
            course_name = input("Enter Course Name: ")
            qry = "select * from table where course = {};".format(course_name)
            cur.execute(qry)
            sl1 = cur.fetchall()
            c = 0
            for i in sl1:
                for j in i:
                    c = j
        elif user_option == 2:
            print("Routine :")
        elif user_option == 3:
            break
        else:
            print("Wrong Option!! Try Again")


faculty("abc", "abc")
