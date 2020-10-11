from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/mul/<int:n>')
def mul(n):
    return render_template('mul.html', n=range(1,n+1))
