# login-->file
import mysql.connector
# import Lib


def main():
    # login
    pass_w = input("Enter Database Password :")
    con = mysql.connector.connect(host="localhost", user="root", passwd=pass_w, database="courseregistration")
    if con.is_connected():
        cur = con.cursor()

    else:
        print("Error Occurred Mysql not connected")


if __name__ == '__main__':
    main()
