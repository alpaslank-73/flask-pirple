import pymysql 

connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
cursor = connection.cursor()

sql ='''CREATE TABLE IF NOT EXISTS users (
   id INT AUTO_INCREMENT NOT NULL,
   user VARCHAR(32) NOT NULL,
   password CHAR(32),   
   PRIMARY KEY (id)
)'''
cursor.execute(sql)


# connection.commit()
# cursor.close()
connection.close()