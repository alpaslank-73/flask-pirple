import pymysql 

connection = pymysql.connect( host = 'localhost', port = 3306,
user = 'alp', passwd = '123456', db = 'todo' )
cursor = connection.cursor()
email='a@b.com'
sql = 'SELECT password FROM users WHERE email = email ;'
#sql ="SELECT password FROM users WHERE email = '{email}' ;"
cursor.execute(sql)
password = cursor.fetchone()[0]
print(password)
connection.close()