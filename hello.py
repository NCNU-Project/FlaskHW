from flask import Flask, render_template, redirect, request
from datetime import datetime

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

@app.route('/url')
def url():
    urls=[
    ('bbc', 'https://bbc.com'),
    ('cnn', 'https://cnn.com'),
    ('NCNU', 'https://www.doc.ncnu.edu.tw/ncnu/'),
    ]
    return render_template('url.html', urls=urls)

@app.route('/redirect/<path:url>')
def new_url(url):
    ip = request.remote_addr
    f = open('server_log.txt', 'a')
    f.write("%s [%s] %s\n" % (ip, datetime.now(), url)) 
    return redirect(url)
