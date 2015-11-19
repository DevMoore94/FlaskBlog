#!/usr/bin/env python
from flask import Flask, jsonify, request,make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
import MySQLdb
app = Flask(__name__)
#create a temporary users table
users = {"jtramley":"password"}

#MySQL connection information.
#host='localhost',user='jtramley',passwd='ckd9OY5fz',db='jtramley'
hosta='localhost'
usera='bmoore1'
passwda='Q8vdnRru7'
dba='bmoore1'


#setup authentication process
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	#if the username is in the users table, return the password.
	connection = MySQLdb.connect(host=hosta,user=usera,passwd=passwda,db=dba)
	cursor = connection.cursor(MySQLdb.cursors.DictCursor)

	query = "select Password from users where Username='%s'" %(username)

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
		return make_response(jsonify({'error':'Failed!'}),404)

@app.route('/blog', methods=['GET','POST'])
def blog():
	if request.method == 'GET':
		#this is where we return all of the user's blog posts
		return 'under construction'
		auth.username
	if request.method == 'POST':
		#this is where we create a new post

		#for command line:
		# curl -u jtramley:"password" -H "Content-Type: application/json"  -X POST -d '{"username":"jtramley", "title":"my first post", "text":"So this is my first blog "}' http://localhost:5000/blog

		username = request.json.get('username',"")
		title = request.json.get('title',"")
		text = request.json.get('text',"")
		return text

	return 'under construction'

#Return entries by User each page will have 5 entries.
@app.route('/blog/<username>/<int:page>')
def getEntries(username, page):
	
	connection = MySQLdb.connect(host=hosta,user=usera,passwd=passwda,db=dba)
	cursor = connection.cursor(MySQLdb.cursors.DictCursor)
	query = "select * from entries where User='%s'" %(username)

	try:
		cursor.execute(query)
	except:
	# 	Things messed up
		print 'THIS BROKE'

	set = cursor.fetchall()
	entries = []

	i = page-1 * 5
	while(i < page*5-1):
		entries.append(set[i])
		i+=1


	cursor.close()
	connection.close()
	return jsonify({'entry': entries})
	
	
if __name__ == '__main__':
    app.run(port=5001, host='localhost', debug=True)
