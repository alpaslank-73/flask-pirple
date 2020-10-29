import pymysql 

connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
cursor = connection.cursor()

sql1 ='''CREATE TABLE IF NOT EXISTS users (
   uid INT AUTO_INCREMENT NOT NULL,
   user VARCHAR(32) NOT NULL,
   password VARCHAR(16),   
   PRIMARY KEY (uid)
)'''
cursor.execute(sql1)
sql2 ='''CREATE TABLE IF NOT EXISTS lists (
   lid INT AUTO_INCREMENT NOT NULL,
   uid INT NOT NULL,
   lname VARCHAR(16),   
   PRIMARY KEY (lid)
)'''
cursor.execute(sql2)
sql3 ='''CREATE TABLE IF NOT EXISTS tasks (
   tid INT AUTO_INCREMENT NOT NULL,
   lid INT NOT NULL,
   text VARCHAR(160),
   done CHAR(1),   
   PRIMARY KEY (tid)
)'''
cursor.execute(sql3)
# connection.commit()
# cursor.close()
connection.close()