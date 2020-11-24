from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

class accountForm(FlaskForm):
    username = StringField('username: ', validators = [DataRequired()])
    passwd = PasswordField('password: ', validators = [DataRequired()])
    submit = SubmitField('Submit')

class changePasswdForm(FlaskForm):
    username = StringField('username: ', validators = [DataRequired()])
    oldPasswd = PasswordField('old passwd; ', validators = [DataRequired()])
    newPasswd = PasswordField('new password: ', validators = [DataRequired()])
    doubleNewPasswd = PasswordField('repect new password: ', validators = [DataRequired()])
    submit = SubmitField('submit')

@app.route('/', methods = ['GET','POST'])
def login():
    if(request.method == 'GET'):
        form = accountForm()
        return render_template('passwd.html', form = form)
    else:
        f = open('account.log', 'r')
        line = f.readline()
        dict = {}
        
        while line:
            acc_li = line.split(',')
            dict[acc_li[0]] = acc_li[1]
            line = f.readline()

        if(dict.__contains__(request.values['username']) and dict[request.values['username']] == request.values['passwd'] + '\n'):
            return render_template('self.html')
        else:
            return "You should not pass!!!"
           
@app.route('/changepasswd', methods = ['GET', 'POST'])
def changepasswd():
    if(request.method == 'POST'):
        fr = open('account.log', 'r')
        
        dict = {}
        line = fr.readline()
        while line:
            acc_li = line.split(',')
            dict[acc_li[0]] = acc_li[1]
            line = fr.readline()
        if(dict.__contains__(request.values['username']) and request.values['oldPasswd'] + '\n' == dict[request.values['username']]):
            if(request.values['newPasswd'] == request.values['doubleNewPasswd']):
                dict[request.values['username']] = request.values['newPasswd'] + '\n'
                
                fw = open('account.log', 'w')
                for item in dict.items():
                    fw.write(item[0] + ',' + item[1])
                return "change successfuly"
            else:
                return "new password and password are distinect"
        else:
            return "wrong password"
    else:
        form = changePasswdForm()
        return render_template('changePasswd.html', form = form)
