from flask import Flask,Response, redirect, url_for, request, session, abort,render_template
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user 

app = Flask(__name__)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# config
app.config.update(
    SECRET_KEY = '123test'
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
#@login_required
def home():
    return Response("Hello f-l World!")


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = 'user'
        password = '123'
        if password == '123' and username=='user':
            login_user(user)
            return redirect('/') #TODO: test
        else:
            return abort(401)
    else:
        html_str= Response(f'''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')
        return render_template('index.html')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(error):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route('/')
def main_page():
	'''tet comment
	'''
	return 'Hellow world'

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
