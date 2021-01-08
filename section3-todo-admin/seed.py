import os
import pymysql

HOST = os.environ.get('MYSQL_HOST')

connection = pymysql.connect( host = str(HOST), port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
cursor = connection.cursor()

# sql1 = """INSERT INTO users( email, password) VALUES( 'alp', '123');"""
# cursor.execute(sql1)

sql2 = """INSERT INTO lists( uid, lname) VALUES( '38', 'physics');"""
cursor.execute(sql2)

sql3 = """INSERT INTO tasks( lid, text, done) VALUES( '1', 'algebra', 'Y');"""
cursor.execute(sql3)

connection.commit()
cursor.close()
connection.close()
