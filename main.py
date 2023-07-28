# login-->file
import hashlib
import mysql.connector
from datetime import datetime

from Lib import Admin
from Lib import Students
from Lib import Faculty


def Symbol():
    print("\033[0;96m░█████╗░░█████╗░██╗░░░██╗██████╗░░██████╗███████╗")
    print("██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔════╝")
    print("██║░░╚═╝██║░░██║██║░░░██║██████╔╝╚█████╗░█████╗░░")
    print("██║░░██╗██║░░██║██║░░░██║██╔══██╗░╚═══██╗██╔══╝░░")
    print("╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██████╔╝███████╗")
    print("░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝")

    print("██████╗░███████╗░██████╗░██╗░██████╗████████╗██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗")
    print("██╔══██╗██╔════╝██╔════╝░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║")
    print("██████╔╝█████╗░░██║░░██╗░██║╚█████╗░░░░██║░░░██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║")
    print("██╔══██╗██╔══╝░░██║░░╚██╗██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║")
    print("██║░░██║███████╗╚██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║")
    print("╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝")


def main():
    # login
    pass_w = input("Enter Database Password :")
    try:
        con = mysql.connector.connect(host="localhost", user="root", passwd=pass_w, database="courseregistration")
        if con.is_connected():
            # create database if not there
            cur = con.cursor()

            def passwd_check(PASS, username):
                try:
                    cur.execute("select password from login where usrname='{}';".format(str(username)))
                    m = cur.fetchall()
                    x = hashlib.sha256(PASS.encode('utf-8')).hexdigest()
                    if m:
                        if x == m[0][0]:
                            print("Login Successful")
                            return True
                        else:
                            print("Password Incorrect")
                            return False
                    else:
                        print("Username Not Found")
                        return False
                except mysql.connector.Error as error:
                    print("User Not Found")

            a = datetime.now()
            Symbol()
            print()
            print("%s                                           %s:%s\033[0m" % (a.date(), a.hour, a.minute))
            print()
            print("\033[0;32mLogin Successful\033[0m")
            print()
            while True:
                print("><><><><><><><><><><><><><><><><><><><><>< OPTIONS ><><><><><><><><><><><><><><><><><><><><><")
                print()
                print("1. Admin Login")
                print("2. Students Login")
                print("3. Faculty Login")
                print("4. Exit")
                print()
                choice = int(input("Enter Your Choice :"))
                print()
                if choice == 1:
                    u = input("Enter Username :")
                    # dont show the password
                    p = input("Enter Password :")
                    if passwd_check(p, u):
                        cur.execute("select privilage from login where usrname='{}';".format(str(u)))
                        m = cur.fetchall()
                        if m[0][0] == 'A':
                            Admin.admin("Admin", u, pass_w)
                        else:
                            print("You are not Admin Try Suitable option")
                    else:
                        print("try again")
                elif choice == 2:
                    u = input("Enter Registration Number :")
                    p = input("Enter Password :")
                    if passwd_check(p, u):
                        cur.execute("select privilage from login where usrname='{}';".format(str(u)))
                        m = cur.fetchall()
                        if m[0][0] == 'S':
                            cur.execute("select name from student where studentID='{}';".format(str(u)))
                            m = cur.fetchall()
                            if m:
                                Students.students(u, m[0][0], pass_w)
                            else:
                                print("Name Not Found")
                        else:
                            print("You are not Student Try Suitable option")
                    else:
                        print("try again")
                elif choice == 3:
                    u = input("Enter Registration Number :")
                    p = input("Enter Password :")
                    if passwd_check(p, u):
                        cur.execute("select privilage from login where usrname='{}';".format(str(u)))
                        m = cur.fetchall()
                        if m[0][0] == 'F':
                            cur.execute("select name from faculty where facultyID='{}';".format(str(u)))
                            m = cur.fetchall()
                            if m:
                                Faculty.faculty(u, m[0][0], pass_w)
                            else:
                                print("Name Not Found")
                        else:
                            print("You are not Faculty Try Suitable option")
                    else:
                        print("try again")
                elif choice == 4:
                    con.close()
                    print("\033[0;34m><><><><><><><><><><><><><><><><><><><><>< Thank You ><><><><><><><><><><><><><><><><><><><><\033[0m")
                    break
                else:
                    print("Try again Wrong Option")
        else:
            print("Error Occurred Mysql not connected")
    except mysql.connector.Error as error:
        print("\033[0;91mError Occurred Mysql not connected\033[0m")
        print("\033[0;91mError : {}\033[0m".format(error))


if __name__ == '__main__':
    main()
