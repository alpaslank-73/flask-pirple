import pymysql 

def check_pw(username):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()

    #sql ='''SELECT password FROM users WHERE email ='{email}' ORDER BY uid DESC;'''.format(email = email)
    sql = 'SELECT password FROM users WHERE email = email ;'
    cursor.execute(sql)
    password = cursor.fetchone()[0]
    connection.close()
    return password

# def signup(username, password, favorite_color):
#     connection = pymysql.connect( host = 'localhost', port = 3306,
#     user = 'alp', passwd = '123456', db = 'todo' )
#     cursor = connection.cursor()
#     sql = '''
#     cursor.execute("""SELECT password FROM users WHERE username = '{username}';""".format(username = username))
#     exist = cursor.fetchone()

#     if exist is None:
#         cursor.execute("""INSERT INTO users(username, password, favorite_color)VALUES('{username}', '{password}', '{favorite_color}');""".format(username = username, password=password, favorite_color=favorite_color))
#         connection.commit()
#         cursor.close()
#         connection.close()

#     else:
#         return ('User already existed!!!')

#     return 'You have successfully signed up!!!'
