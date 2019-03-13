from flask import Flask, render_template, redirect, request, session
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = 'secretKey'
mysql = MySQLConnection(app, 'friends')

@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    session['friends'] = mysql.query_db(query)
    return render_template('friends.html')

@app.route('/friends', methods=['POST'])
def friends():
    query = 'INSERT INTO friends (name, age) VALUES (:name, :age)'
    data = {
        'name' : request.form['name'],
        'age' : request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)