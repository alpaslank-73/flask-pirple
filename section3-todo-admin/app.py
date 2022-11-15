from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)

app.secret_key = 'jumpjacks'
email = ''
user = model.check_users()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        text1 = 'This web-test1 application lets you keep track of your things to do.<br><br>'
        text2 = 'In order to use the app you need to be a registered user.<br><br>'
        text3 = 'After signing in you can begin using the application.<br><br>'
        return render_template('index.html', message1=text1, message2=text2, message3=text3)
    else:
        session.pop('email', None)
        areyouuser = request.form['email']
        pwd = model.check_pw(areyouuser)
        if request.form['password'] == pwd:
            session['email'] = request.form['email']        
            return redirect(url_for('lists'))
    if 'email' in session:
        g.user=session['email']
        return redirect(url_for('lists'))
    error_message = 'Wrong email or password <br><br>'
    return render_template('index.html', err_message = error_message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('email', None)
        areyouuser = request.form['email']
        pwd = model.check_pw(areyouuser)
        if request.form['password'] == pwd:
            session['email'] = request.form['email']
            return redirect(url_for('lists'))
    return render_template('index.html')

@app.before_request
def before_request():
    g.email = None
    if 'email' in session:
        g.email = session['email']

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', message = 'We are supersonic')

@app.route('/terms', methods = ['GET'])
def terms():
    return render_template('terms.html', message = 'He are our terms of use')

@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html', message = 'Very private')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html', message = 'Please sign up')
    else:
        email = request.form["email"]
        password = request.form["password"]
        model.signup(email, password)
        #message = model.signup(email, password)
        return render_template('signup.html', message = 'Thanks for signing up. <a href="/login">Click to log in</a>')

@app.route('/lists')
def lists():
    email = session['email']
    lists = model.list_users_lists(email)
    print(lists, 'KAPLAN')
    return render_template('new_lists.html', lists=lists, message = email)

@app.route("/dellist/<string:lid>")
def dellist(lid):
    #lname = request.args.get('list')
    # print(lname,'ALPASLAN lname')
    model.dellist(lid)
    #print(lname,'sdfsd fsdf aALOOOOOOOOOOOO **0*0*0*00999 ')
    # db.session.delete(todo)
    # db.session.commit()
    return redirect(url_for("lists"))

@app.route('/tasks')
def tasks():
    # dene1 = request.data
    lname = request.args.get('list')
    #print(lname, 'lname')
    lid = model.getlid(lname)
    # print(lname, lid, 'lid')
    tasks = model.tasklist(lid)
    #print(tasks, 'tasks - alp')
    # return render_template('tasks.html', tasks=tasks)
    return render_template('new_tasks.html', tasks=tasks, lid=lid)

@app.route('/addlist', methods = ['POST'])
def addlist():
    email = session['email']
    uid = model.getuid(email)
    lname = request.form["lname"]
    model.addlist(uid,lname)
    #return render_template('lists.html', message='List added')
    return redirect(url_for('lists'))
    
@app.route('/addtask', methods = ['POST'])
def addtask():
    #task = request.form["lname_degil_baska_bisi_tabi"]
    task = request.form.get("text")
    lid  = request.args.get('list')
    lname = model.getlname(lid)
    # print(task, lid, lname, 'Alp ***')
    model.addtask(lid, task)
    # return redirect(url_for('/tasks'))
    myurl = '/tasks?list=' + lname
    #print(myurl)
    return redirect(myurl)

@app.route("/deltask/<string:tid>")
def deltask(tid):
    lid = model.get_lid_from_tid(tid)
    lname = model.getlname(lid)
    #lname = request.args.get('list')
    model.deltask(tid)
    #print(lname,'sdfsd fsdf aALOOOOOOOOOOOO **0*0*0*00999 ')
    # db.session.delete(todo)
    # db.session.commit()
    # return redirect(url_for("tasks"))
    myurl = '/tasks?list=' + lname
    #print(myurl)
    return redirect(myurl)

@app.route("/updatetask/<string:tid>")
def updatetask(tid):
    lid = model.get_lid_from_tid(tid)
    lname = model.getlname(lid)
    model.update_task(tid)
    #todo.complete = not todo.complete
    myurl = '/tasks?list=' + lname
    #print(myurl)
    return redirect(myurl)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
