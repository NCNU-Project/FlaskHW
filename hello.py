from flask import Flask, render_template, redirect, request
from datetime import datetime, date

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

@app.route('/birthday', methods=['GET','POST'])
def birthday():
    week_day_dict = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Tuesday",
        4 : "Friday",
        5 : "SaterDay",
        6 : "Sunday",
    }
    yyyy = str(request.values['yyyy'])
    mm = str(request.values['mm'])
    dd = str(request.values['dd'])
    if(len(mm) < 2 ):
        mm = '0'+mm
    if(len(dd) < 2 ):
        dd = '0' + dd
    dateString = "{}/{}/{} is {}".format(yyyy,mm,dd, week_day_dict[datetime(int(request.values['yyyy']),int( request.values['mm']),int(request.values['dd'])).weekday()])
    return dateString

@app.route('/birthdayWeb')
def birthdayWeb():
    return render_template('calender.html')

@app.route('/birthday1', methods = ['POST', 'GET'])
def birthday1():
    week_day_dict = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Tuesday",
        4 : "Friday",
        5 : "SaterDay",
        6 : "Sunday",
    }
    day = date.fromisoformat(request.values['date'])
    return day.strftime('%Y/%m/%d')+' is '+ week_day_dict[day.weekday()]
