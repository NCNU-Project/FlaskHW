from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

class BirthForm(FlaskForm):
    y_list = []
    m_list = []
    d_list = []
    for i in range(1950,2021):
        y_list.append(i)
    for i in range(1, 13):
        m_list.append(i)
    for i in range(1, 32):
        d_list.append(i)
    
    yyyy = SelectField('year', choices = y_list)
    mm = SelectField('month', choices = m_list)
    dd = SelectField('day', choices = d_list)
    submit = SubmitField('Submit')

class NameForm(FlaskForm):
    height = StringField('What is your height',validators = [DataRequired()])
    weight = StringField('What is your weight',validators = [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['POST', 'GET'])
def index():
    if(request.method == 'GET'):
       form = NameForm()
       return render_template('ch4_web_form.html', form = form)
    else:
        height = int(request.values['height'])
        weight = int(request.values['weight'])

        if(height < 3):
            height /= 100
        return "your BMI is {}".format(weight / height / height)

@app.route('/birthday', methods=['GET', 'POST'])
def birthday():
    if(request.method == 'GET'):
        form = BirthForm()
        return render_template('ch4_birth_form.html', form = form)
    else:
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
