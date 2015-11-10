#!/usr/bin/env python
from flask import Flask, jsonify, request,make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
app = Flask(__name__)
#create a temporary users table
users = {"jtramley":"password"}

#setup authentication process
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	#if the username is in the users table, return the password.
	if username in users:
		return users.get(username)
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Bad username or passowrd.'}),403)

# Some error handlers

@app.errorhandler(400)
def not_found(error):
        return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/login', methods=['GET','POST'])
@auth.login_required
def login():

	if request.method == 'POST':
		return make_response(jsonify({'error':'Success!'}),201)
	else:
		return '<ContentType: text/html> <!DOCTYPE html><html> <head> <title>FlaskBlog Login Page</title> </head> <body> <h1> Login </h1> <p>Under Construction</p></body></html>'

@app.route('/blog', methods=['GET','POST'])
def blog():
	if request.method == 'GET':
		#this is where we return all of the user's blog posts
		return 'under construction'
	if request.method == 'POST':
		#this is where we create a new post

		#for command line:
		# curl -u jtramley:"password" -H "Content-Type: application/json"  -X POST -d '{"username":"jtramley", "title":"my first post", "text":"So this is my first blog "}' http://srv:5000/blog

		username = request.json.get('username',"")
		title = request.json.get('title',"")
		text = request.json.get('text',"")
		return text

	return 'under construction'
if __name__ == '__main__':
    app.run(port=5000, host='192.168.2.23')
