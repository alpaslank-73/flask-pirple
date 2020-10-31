from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        text1 = 'This web application lets you keep track of your things to do.'
        text2 = 'In order to use the app you need to be a registered user.'
        text3 = 'After signing in you can begin using the application.'
        return render_template('index.html', message1=text1, message2=text2, message3=text3)
    else:
        email = request.form['email']
        password = request.form['password']
        db_password = model.check_pw(email)

        if password == db_password:
            #message = model.show_color(username)
            #return render_template('todo.html', message = message)
            return render_template('todo.html')
        else:
            error_message = 'Wrong email or password'
            return render_template('index.html', err_message = error_message)

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/terms', methods = ['GET'])
def terms():
    return render_template('terms.html')

@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/todo', methods = ['GET'])
def todo():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)
