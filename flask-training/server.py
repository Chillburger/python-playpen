from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): 
	return "Index Page! <p>test paragraph</p>"

@app.route('/hello')
def hello_world():
	return "<b>hello world</b>"

if __name__ == "__main__": 
	app.run(host='0.0.0.0')


