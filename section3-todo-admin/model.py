import pymysql 

def getuid(email):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = "SELECT `uid` FROM `users` WHERE `email`=%s"
    cursor.execute(sql, (email,))
    uid = cursor.fetchone()
    # print(uid, 'aloo1')
    if uid is None:
        #print('No such user')
        return False
    else:
        #password = cursor.fetchone()[0]
        uid = uid[0]
        # print(uid, 'aloo2')
        return uid
    connection.close()

def getlid(lname):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = "SELECT `lid` FROM `lists` WHERE `lname`=%s"
    cursor.execute(sql, (lname,))
    lid = cursor.fetchone()
    if lid is None:
        #print('No such user')
        return False
    else:
        #password = cursor.fetchone()[0]
        lid = lid[0]
        return lid
    connection.close()

def get_lid_from_tid(tid):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = "SELECT `lid` FROM `tasks` WHERE `tid`=%s"
    cursor.execute(sql, (tid,))
    lid = cursor.fetchone()
    if lid is None:
        #print('No such user')
        return False
    else:
        #password = cursor.fetchone()[0]
        lid = lid[0]
        return lid
    connection.close()

def getlname(lid):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = "SELECT `lname` FROM `lists` WHERE `lid`=%s"
    cursor.execute(sql, (lid,))
    lname = cursor.fetchone()
    if lname is None:
        #print('No such list')
        return False
    else:
        lname = lname[0]
        return lname
    connection.close()

def check_users():
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = 'SELECT email FROM users ORDER BY uid DESC;'
    cursor.execute(sql)
    db_users = cursor.fetchall()
    users = []
    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)
    connection.commit()
    cursor.close()
    connection.close()
    return users

def check_pw(email):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = "SELECT `password` FROM `users` WHERE `email`=%s"
    cursor.execute(sql, (email,))
    password = cursor.fetchone()
    #print(password)
    if password is None:
        #print('No such user')
        return False
    else:
        #password = cursor.fetchone()[0]
        password = password[0]
        # print(password)
        return password
    connection.close()

def signup(email, password):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql1 = "SELECT `password` FROM `users` WHERE `email`=%s"
    cursor.execute(sql1, (email,))
    exist = cursor.fetchone()
    if exist is None:
        sql2 = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql2, (email, password))
        connection.commit()
        cursor.close
        connection.close
        # print('You have succesfully signed up!')
    else:
        # print('User already exists!')
        cursor.close
        connection.close()

def addlist(uid,lname):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql1 = "SELECT `uid` FROM `lists` WHERE `lname`=%s"
    cursor.execute(sql1, (lname,))
    exist = cursor.fetchone()
    if exist is None:
        sql2 = "INSERT INTO `lists` (`uid`, `lname`) VALUES (%s, %s)"
        cursor.execute(sql2, (uid, lname))
        connection.commit()
        cursor.close
        connection.close
        # print('List added!')
    else:
        # print('List already exists!')
        cursor.close
        connection.close()

def list_users_lists(email):
    uid = getuid(email)
    #print(uid)
    list = []
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql = "SELECT `lid`, `lname` FROM `lists` WHERE `uid`=%s"
    cursor.execute(sql, (uid,))
    list = cursor.fetchall()
    print(list)
    if list is None:
        # print('No such user')
        list = []
        return list
    else:
        # print(list)
        return list
    connection.close()

def tasklist(lid):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    # sql = "SELECT `text`, `done` FROM `tasks` WHERE `lid`=%s"
    sql = "SELECT `tid`, `text`, `done` FROM `tasks` WHERE `lid`=%s"
    cursor.execute(sql, (lid,))
    tasklist = []
    tasklist = cursor.fetchall()
    #print(tasklist, 'tasklist')
    if tasklist is None:
        tasklist = []
        return tasklist
        #return False
    else:
        # print(tasklist)
        return tasklist
    connection.close()

def dellist(lid): 
    # first delete all tasks belonging to list
    # lid = getlid(lname)
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql1 = "DELETE  FROM `tasks` WHERE `lid`=%s"
    cursor.execute(sql1, (lid,))
    sql2 = "DELETE  FROM `lists` WHERE `lid`=%s"
    cursor.execute(sql2, (lid,))
    connection.commit()
    cursor.close
    connection.close

def addtask(lid, text):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql1 = "SELECT `tid` FROM `tasks` WHERE `text`=%s"
    cursor.execute(sql1, text)
    #print('ALPAS', text, type(text), 'LAN', text.isspace())
    exist = cursor.fetchone()
    if exist is None:
        sql2 = "INSERT INTO `tasks` (`lid`, `text`, `done`) VALUES (%s, %s, %s)"
        cursor.execute(sql2, (lid, text, 'N'))
        connection.commit()
        cursor.close
        connection.close
    else:
        #print('Task already exists!')
        cursor.close
        connection.close()

def deltask(tid):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql1 = "DELETE  FROM `tasks` WHERE `tid`=%s"
    cursor.execute(sql1, tid)
    connection.commit()
    cursor.close
    connection.close()

def update_task(tid):
    connection = pymysql.connect( host = 'localhost', port = 3306,
    user = 'alp', passwd = '123456', db = 'todo' )
    cursor = connection.cursor()
    sql1 = "SELECT `done` FROM `tasks` WHERE `tid`=%s"
    cursor.execute(sql1, tid)
    task_status = cursor.fetchone()[0]
    print(task_status, 'SOOOON1', tid)
    if task_status == 'Y':
        task_status = 'N'
    else:
        task_status = 'Y'
    print(task_status, 'SOOOON2', tid)
    sql2 = 'UPDATE tasks SET done = %s WHERE tid = %s'
    cursor.execute(sql2, (task_status, tid))
    connection.commit()
    cursor.close
    connection.close()
