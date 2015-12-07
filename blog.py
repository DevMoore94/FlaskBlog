#!/usr/bin/env python
from flask import Flask, jsonify, request,make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
import MySQLdb
from flask.ext.cors import CORS
app = Flask(__name__)
CORS(app)
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
	cursor = connection.cursor()
	query = "select Password from users where Username='%s'" %(username)
	#query = "getPassword('%s')" %(username)

	try:
		cursor.execute(query)
	except:
	 	#Things messed up
		return make_response(jsonify({'error':'Failed!'}),404)
	
	returned = cursor.fetchone()
	#if the username was wrong
	if (cursor.rowcount == 0):
		return None 
	if returned[0] == '':
		return None
	return returned[0]



@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Bad username or password.'}),403)

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

@app.route('/blog', methods=['POST','DELETE'])
@auth.login_required
def blog():
	if request.method == 'POST':
		#for command line:
		# curl -u jtramley:"password" -H "Content-Type: application/json"  -X POST -d '{"username":"jtramley", "title":"my first post", "content":"So this is my first blog "}' http://localhost:5000/blog
		
		username = auth.username()
		title = request.json.get('title',"")
		print 'got title'
		content = request.json.get('content',"")
		print 'gpt content'
		query = "insert into entries values(DEFAULT,'%s','%s','%s',DEFAULT)" %(title,content,username)
		print 'request parsed'
		connection = MySQLdb.connect(host=hosta,user=usera,passwd=passwda,db=dba, use_unicode=True, charset='utf8')
		cursor = connection.cursor()
		print 'connection created'
		try:
			cursor.execute(query)
			print 'executed query'
		except:
		# 	Things messed up
			return make_response(jsonify({"error":"Database Connection failure"}),500)

		cursor.close()
		connection.close()

		return make_response(jsonify({'error':'Success!'}),201)
	
	if request.method == 'DELETE':
		username = auth.username()
		entryID = request.json.get('entryID',"")

		connection = MySQLdb.connect(host=hosta,user=usera,passwd=passwda,db=dba, use_unicode=True, charset='utf8')
		cursor = connection.cursor()

		query = "select * from entries where EntryID='%s' and User='%s'" %(entryID,username)

		try: 
			cursor.execute(query)
		except:
			return make_response(jsonify({"error":"Database Connection failure"}),500)

		if (cursor.rowcount != 0):
			query = "delete from entries where EntryID='%s' and User='%s'" %(entryID,username)
			try: 
				cursor.execute(query)
			except:
				return make_response(jsonify({"error":"Database Connection failure"}),500)
			
			cursor.close()
			connection.close()
			return make_response(jsonify({'error':'Success!'}),201)
		else:
			return make_response(jsonify({'error':'Failed!'}),403)

#Return entries by User each page will have 5 entries.
@app.route('/blog/<username>/<int:page>')
def getEntries(username, page):
	
	connection = MySQLdb.connect(host=hosta,user=usera,passwd=passwda,db=dba)
	cursor = connection.cursor(MySQLdb.cursors.DictCursor)
	query = "call getEntryByUser('%s')" %(username)

	try:
		cursor.execute(query)
	except:
	# 	Things messed up
		return make_response(jsonify({"error":"Database Connection failure"}),500)
		
	set = cursor.fetchall()
	
	entries = []
	
	i = (page-1) * 5
	while(i < page*5 and i < len(set)):
		
		entries.append(set[i])
		i+=1


	cursor.close()
	connection.close()
	return jsonify({'entry': entries})

if __name__ == '__main__':
    app.run(host='info3103.cs.unb.ca', port=1319, debug=True)

