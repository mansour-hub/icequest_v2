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
        msg.body = "test"
        mail.send(msg)
       	
       	submitted = True

        return render_template("index.html", submitted = submitted)
    else:        
        return render_template("index.html")


@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
	app.run(debug=True)
