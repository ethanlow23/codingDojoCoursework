from flask import Flask, render_template, redirect, request, session, url_for
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnection(app, 'users')

@app.route('/users')
def index():
    query = 'SELECT * FROM users'
    users = mysql.query_db(query)
    return render_template('users.html', users = users)

@app.route('/users/new')
def new():
    return render_template('users_add.html')

@app.route('/users/<id>/edit')
def edit(id):
    return render_template('users_edit.html', id = id)

@app.route('/users/<id>')
def show(id):
    query = 'SELECT * FROM users WHERE id = :id'
    data = {
        'id': id
    }
    users = mysql.query_db(query, data)
    return render_template('users_show.html', users = users)

@app.route('/users/create', methods=['POST'])
def create():
    query = 'INSERT INTO users (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    newId = mysql.query_db(query, data)
    print newId
    return redirect('/users/' + str(newId))

@app.route('/users/<id>/destroy')
def destroy(id):
    query = 'DELETE FROM users WHERE id = :id'
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>', methods=['POST'])
def update(id):
    query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)
    query2 = 'SELECT * FROM users WHERE id = :id'
    data = {
        'id': id
    }
    new_id = mysql.query_db(query2, data)
    print new_id
    return redirect('/users/' + str())

app.run(debug=True)