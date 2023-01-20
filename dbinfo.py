import pymysql


def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="payroll"
)


