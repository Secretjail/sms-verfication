from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
	'''tet comment
	'''
	return 'Hellow world'