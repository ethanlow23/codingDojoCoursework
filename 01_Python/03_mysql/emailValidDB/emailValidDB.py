from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnection
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnection(app, 'emailvaliddb')

@app.route('/')
def index():
    return render_template('emailValidDB.html')

@app.route('/email', methods=['POST'])
def email():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address')
        return redirect('/')
    else:
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
        data = {
            'email' : request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    query = 'SELECT * FROM emails'
    email = mysql.query_db(query)
    return render_template('success.html', emails = email)

app.run(debug=True)