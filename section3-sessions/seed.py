import pymysql 

connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
cursor = connection.cursor()

sql1 = """INSERT INTO users( email, password) VALUES( 'a@b.com', '123');"""
cursor.execute(sql1)

connection.commit()
cursor.close()
connection.close()