from flask import Flask
app = Flask(__name__)


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
