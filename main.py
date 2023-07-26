# login-->file
import mysql.connector
from datetime import datetime


# import Lib


def main():
    # login
    pass_w = input("Enter Database Password :")
    try:
        con = mysql.connector.connect(host="localhost", user="root", passwd=pass_w, database="courseregistration")
        if con.is_connected():
            cur = con.cursor()
            a = datetime.now()
            print("%s       %s:%s" % (a.date(), a.hour, a.minute))
            print("Login Successful")
            while True:
                print("===================== OPTIONS =====================")
                choice = int(input("Enter Your Choice :"))
                if choice == 1:
                    print("1")
                elif choice == 4:
                    break
                else:
                    print("Try again Wrong Option")
    except mysql.connector.Error as error:
        print("Error Occurred Mysql not connected")
    else:
        print("Error Occurred Mysql not connected")


if __name__ == '__main__':
    main()
