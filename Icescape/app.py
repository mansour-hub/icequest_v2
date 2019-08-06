from user_db import *
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'icescape.bj@gmail.com',
    MAIL_PASSWORD = 'icescape20',
))

mail = Mail(app)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        nationality = request.form['nationality']
        date = request.form['date']
        phone = request.form['phone']
        email = request.form['email']

        add_user(name, surname, phone, date, email, nationality)

        msg = Message("Icescape Room Registration",
                      sender="icescape.bj@gmail.com",
                      recipients=[request.form['email']])
        msg.body = "text"
        mail.send(msg)
       	
       	submitted = True

        return render_template("index.html", submitted = submitted)
    else:        
        return render_template("index.html")


@app.route('/admin', methods = ['GET', 'POST'])
def admin():
	users = query_by_date('11/11/2020')
	if request.method == 'POST':
		team = mix_and_match("11/11/2020")
		
		for user in team:
			msg = Message("Icescape Room Date",
	                      sender="icescape.bj@gmail.com",
	                      recipients=[user.email])
			msg.body = "You are in the game"
			mail.send(msg)
		
		return render_template("admin.html", users = users, team = team)
	return render_template('admin.html', users = users)

if __name__ == '__main__':
	app.run(debug=True)
