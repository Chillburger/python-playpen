from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): 
	return "Index Page! <p>test paragraph</p>"

@app.route('/hello')
def hello_world():
	return "<b>hello world</b>"

@app.route('/user/<username>')
def user(username):
	return "hello ,%s" % username

@app.route('/entityid/<int:id>')
def entity(id):
	return "Post: %d" % id

@app.route('/entityid/<invalid>')
def entity_invalid(invalid):	
	return "Please use a proper integer for the id"

if __name__ == "__main__": 
	app.run(host='0.0.0.0')


