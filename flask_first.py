from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return ('<body><h1>Hello World</h1></body>')

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

if __name__ == '__main__':
    app.run(port = 5000, debug= True)