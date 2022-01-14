from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')

def dojo():
    return "Dojo!"

@app.route('/hello/<string:name>')

def hello(name):
    return f"Hi {name}"

@app.route('/hello/<string:name>/<int:num>')

def hello_num(name, num):
    return f"Hello {name * num}"


if __name__=="__main__":
    app.run(debug=True)
