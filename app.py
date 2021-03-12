#!/usr/bin/python
from flask import Flask,Response, redirect, url_for, request, session, abort,render_template
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user,current_user 
from flask_security import LoginForm, url_for_security
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_security.forms import RegisterForm

import mysql.connector


from getpass import getpass
from mysql.connector import connect, Error

app = Flask(__name__)
app.config.from_pyfile('config/app.conf', silent=True)
limiter = Limiter(app, key_func=get_remote_address)


mydb = mysql.connector.connect(
 host=app.config.get("DB_HOST"),
 user=app.config.get("DB_USER"),
 password=app.config.get("DB_PASSWORD"),
 database=app.config.get("DB_DATABASE")
)

mycursor = mydb.cursor()

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# config
app.config.update(
    SECRET_KEY = app.config.get("SECRET_KEY")
)

# silly user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "%d" % (self.id)

# create some users with ids 1 to 20
user = User(0)

# some protected url
@app.route('/')
@login_required
def home():
    return render_template('index.html')



@app.route('/flot')
@login_required
def flot():
    return render_template('flot.html')


@app.route('/morris')
@login_required
def morris():
    return render_template('morris.html')
#app.run(debug=True)

#somewhere to login
@app.route("/login", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def login():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        form_qoute=str.maketrans('', '', '\'"\\-')
        username=username.translate(form_qoute)
        password=password.translate(form_qoute)
        mycursor.execute("select * from  users where (email=\""+username+"\" and password=\""+password+"\");")
        res = mycursor.fetchall()
        if(len(res)==1):
            login_user(user)
            return redirect('/') #TODO: test
        else:
            return abort(401)
    else:
            return render_template('login.html')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html')


# handle login failed
@app.errorhandler(401)
def page_not_found(error):
    return Response('<p>Login failed <a href=\"login\">Goto Login</a></p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route('/v1/callback')
def callback():
	pass


@app.route('/v1/process')
def proccess():
	'''if user request prce is now the exact value
	then send it ass sms for user
	'''
	pass

@app.route('/v1/send_sms')
def send_sms():
	'''send sms to user with mobile_number
	name of symbol and time or crossing or passing or reaching price
	'''
	pass


if __name__ =="__main__":
	app.run("0.0.0.0", 80, debug=True)
