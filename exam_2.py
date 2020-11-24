from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = '1234'

class q1Form(FlaskForm):
    data = [
            (0, "非常符合"),
            (1, "比較符合"),
            (2, "不太確定"),
            (3, "比較不符合"),
            (4, "非常不符合")
            ]

    q1 = RadioField('1. 我在講話的時候，有很多素材和詞彙可講。', choices = data)
    q2 = RadioField('2. 我講話簡潔明瞭，重點突出。', choices = data)
    q3 = RadioField('3. 我善於與和我性格不同的人溝通。', choices = data)
    q4 = RadioField('4. 我對連續不斷的交談感到很容易。', choices = data)
    q5 = RadioField('5. 我可以輕易地向別人描述一件事情。', choices = data)
    q6 = RadioField('6. 跨部門溝通我而言是一件很容易的事情。', choices = data)
    q7 = RadioField('7. 我喜歡和別人聊天。', choices = data)
    q8 = RadioField('8. 和重要的人物（例如上司）談話時，我感到很自然、放鬆。', choices = data)
    q9 = RadioField('9. 我在當眾講話時思維清晰、連貫。', choices = data)
    q10 = RadioField('10. 每當面對即興談話，我可以隨時取得素材進行談話。', choices = data)
    q11 = RadioField('11. 我喜歡在大庭廣眾之下講話。', choices = data)
    q12 = RadioField('12. 我善於跟內向的朋友輕鬆自如地談論自己的情況。', choices = data)
    q13 = RadioField('13. 我善於說服人，儘管有時我覺得自己毫無道理。', choices = data)
    q14 = RadioField('14, 我善於讚美別人，覺得讚美別人是一件很開心的事情。', choices = data)
    q15 = RadioField('15. 講一個完整的故事對我來說很容易。', choices = data)
    submit = SubmitField('測試結果分析')

@app.route('/q2', methods = ['GET', 'POST'])
def q2():
    if(request.method == 'GET'):
        form = q1Form()
        return render_template('q2.html', form = form)
    else:
        dict = {
            0:7,
            1:5,
            2:3,
            3:1,
            4:0
        }

        point = 0
        req = request.values.to_dict()
        print(req)
        for key, value in req.items():
            if(key != 'csrf_token' and key != 'submit'):
                point += dict[int(value)]
                print(value)
        return render_template('q2_1.html', point = point) 
