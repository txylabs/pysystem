from pymysql import *

def openSql():
    try:
        conn = connect(host='localhost', port=3306, user='root', password="123456", database="py_system")
        return conn
    except connect.Error:
        print("数据库连接失败")


def closeSql(conn, cursor):
    conn.close()
    cursor.close()