from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = '1234'
class q1Form(FlaskForm):
    data = [
        [
            (0, "做一件事情下決心快，行動快，雷厲風行。"),
            (1, "喜歡做有趣的事情，為人充滿樂趣與幽默感。"),
            (2, "在任何衝突中都不易受干擾，保持冷靜。"),
            (3, "做事有節奏，完成一件事後才接受新事。")
        ],[
            (0, "行為外露，總給人一種強烈的想贏的欲望。"),
            (1, "喜歡展現自我，透過自我魅力來讓別人接受自己。"),
            (2, "關心別人的感覺與需要，易於接受他人的觀點，不堅持己見。"),
            (3, "喜歡控制自己的內心情感，幾乎不向外人展露。")
        ],[
            (0, "反應快,思維敏捷"),
            (1, "充滿激情、動力與興奮。"),
            (2, "約束自我情感，心態平和。"),
            (3, "安靜嚴肅，面無表情。") 
        ],[    
            (0, "對自己的能力很有自信，且經常向別人展示。"),
            (1, "不喜歡計畫，喜歡運用語言、人格魅力，鼓勵推動別人參與。"),
            (2, "容忍自己和別人的錯誤，冷靜且包容心強。"),
            (3, "事前喜歡做詳盡計畫，然後按計畫進行。")
        ],[    
            (0, "做事自信，幾乎不會猶豫。"),
            (1, "隨性，不喜歡條例規定，不喜歡受約束。"),
            (2, "容易沒有主見，做事容易猶豫不決。"),
            (3, "有原則，不易妥協。")
        ],[    
            (0, "天生的領導者，無論在什麼事情上都喜歡主導。"),
            (1, "喜歡到處走走，充滿生機，精力充沛。"),
            (2, "不願意主導，喜歡被領導。"),
            (3, "喜歡一個人獨處。")
        ],[    
            (0, "強勢，讓人覺得不能改變。"),
            (1, "滔滔不絕的發言者，不是好聽眾，不會留意別人也在講話。"),
            (2, "易相處，易讓人接近。"),
            (3, "很少說話，除非工作需要。")
        ],[    
            (0, "不能忍受別人動作慢，效率低。"),
            (1, "喜歡吸引人，喜歡成為焦點。"),
            (2, "穩定，工作節奏慢，說話慢。"),
            (3, "總是避免自己成為注意力的中心。")
        ],[    
            (0, "自我評價高，認為自己是最佳人選。"),
            (1, "容許別人（包括孩子）做他喜歡做的事，為的是討好別人，讓人喜歡。"),
            (2, "性格中庸，無高低情緒，很少表露感情。"),
            (3, "儘管期待好結果，但往往先看到事物的不利之處。")
        ],[    
            (0, "成就動機強，並為此而不斷工作。"),
            (1, "性格開朗，說話聲與笑聲總是能吸引別人注意。"),
            (2, "行動慢，不喜歡行動，安於現狀。"),
            (3, "孤獨離群，感到需要大量時間獨處。")
        ],[    
            (0, "為人坦誠，內心毫不保留，坦率發言。"),
            (1, "為人樂觀開朗，相信任何事都會好轉。"),
            (2, "願意改變，只要別人意見合理，就會接受。"),
            (3, "會保留自己的意見，不輕易向別人表達。")
        ],[   
            (0, "敢於冒險，敢於承擔責任。"),
            (1, "喜歡帶給別人歡樂，令人喜歡，容易相處。"),
            (2, "彬彬有禮，待人得體有耐心。"),
            (3, "做事井然有序，清晰有條理。")
        ],[    
            (0, "獨立能力強，自我支持，自我鼓勵。"),
            (1, "需要旁人認同、讚賞，如同演藝家需要觀眾的掌聲、笑聲。"),
            (2, "避免矛盾，所以從不說也不做引起他人不滿與反感的事。"),
            (3, "喜歡以自己認定的標準來衡量事情。")
        ],[    
            (0, "決心依自己的意願行事，不易被說服。"),
            (1, "喜歡開玩笑，忘情地表達自己的情感、喜好。"),
            (2, "容易被說服，被領導。"),
            (3, "喜歡深刻的談話，不喜歡膚淺的聊天或喜好。")
        ],[   
            (0, "工作狂，努力推動工作，喜歡領導別人。"),
            (1, "喜好吵鬧的環境，出席各種宴會，結交各種朋友。"),
            (2, "喜歡安穩，不喜歡過於忙碌的工作和生活。"),
            (3, "偏安靜，不喜歡嘈雜。")
        ]
    ]

    q1 = RadioField('01', choices = data[0])
    q2 = RadioField('02', choices = data[1])
    q3 = RadioField('03', choices = data[2])
    q4 = RadioField('04', choices = data[3])
    q5 = RadioField('05', choices = data[4])
    q6 = RadioField('06', choices = data[5])
    q7 = RadioField('07', choices = data[6])
    q8 = RadioField('08', choices = data[7])
    q9 = RadioField('09', choices = data[8])
    q10 = RadioField('10', choices = data[9])
    q11 = RadioField('11', choices = data[10])
    q12 = RadioField('12', choices = data[11])
    q13 = RadioField('13', choices = data[12])
    q14 = RadioField('14', choices = data[13])
    q15 = RadioField('15', choices = data[14])
    submit = SubmitField('Submit')

@app.route('/q1', methods = ['GET', 'POST'])
def q1():
    if(request.method == 'GET'):
        form = q1Form()
        return render_template('q1.html', form=form)
    else:
        dict = {
            0: 0,
            1: 0,
            2: 0,
            3: 0
        }

        req = request.values.to_dict()
        maxv = 0
        for key, value in req.items():
            if(key != 'submit' and key != 'csrf_token'):
                dict[int(value)]+=1 
        
        for key, value in dict.items():
            if(value > maxv):
                maxv = value
        
        retS = '<table border="">'
        retS += "<tbody>"
        retS += "<tr><th>性格</th><th>題數</th></tr>"
        if(dict[0] == maxv):
            retS += '<tr style="background-color: pink">'
        else:
            retS += '<tr>'
        retS += "<td>Power 力量型</td>"
        retS += "<td>{}</td>".format(dict[0])
        retS += "</tr>"
        
        if(dict[1] == maxv):
            retS += '<tr style="background-color: pink">'
        else:
            retS += '<tr>'
        retS += "<td>Popular 社交型</td>"
        retS += "<td>{}</td>".format(dict[1])
        retS += "</tr>"
        
        if(dict[2] == maxv):
            retS += '<tr style="background-color: pink">'
        else:
            retS += '<tr>'
        retS += "<td>Peace 和平型</td>"
        retS += "<td>{}</td>".format(dict[2])
        retS += "</tr>"

        if(dict[3] == maxv):
            retS += '<tr style="background-color: pink">'
        else:
            retS += '<tr>'
        retS += "<td>Perfect 完美型</td>"
        retS += "<td>{}</td>".format(dict[3])
        retS += "</tr>"
        retS += "</tbody></table>"
        if(len(req) != 17):
            retS += '<p>總題數應為{}，但你只答了 {}題。</p>'.format(15, len(req) - 2)
        retS += '<p>大多數的人四種性格都有。而題數最高的那個，是你的主導性格。</p>'
        return retS 
