# login-->file
import mysql.connector
from datetime import datetime

from Lib import Faculty


def main():
    # login
    pass_w = input("Enter Database Password :")
    try:
        con = mysql.connector.connect(host="localhost", user="root", passwd=pass_w, database="courseregistration")
        if con.is_connected():
            # create database if not there
            cur = con.cursor()

            def passwd_check(username, PASS, Type):
                try:
                    cur.execute("select password from login where usrname={};".format(username))
                    m = cur.fetchall()
                    if PASS == m[0][0]:
                        return True
                    else:
                        return False
                except mysql.connector.Error as error:
                    print("User Not Found")

            a = datetime.now()
            print("%s       %s:%s" % (a.date(), a.hour, a.minute))
            print("Login Successful")
            while True:
                print("===================== OPTIONS =====================")
                print("1. Admin Login")
                print("2. Faculty Login")
                print("3. Students Login")
                print("4. Exit")
                choice = int(input("Enter Your Choice :"))
                if choice == 1:
                    print("1")
                elif choice == 2:
                    u = input("Enter Username :")
                    p = input("Enter Password :")
                    if passwd_check(p, u, "faculty"):
                        Faculty.faculty("Registration", u, pass_w)
                    else:
                        print("try again")
                elif choice == 4:
                    print("Thank You")
                    break
                else:
                    print("Try again Wrong Option")
        else:
            print("Error Occurred Mysql not connected")
    except mysql.connector.Error as error:
        print("Error Occurred Mysql not connected")
        print("Error : {}".format(error))


if __name__ == '__main__':
    main()
