from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnection
import re, md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnection(app, 'login_register')

@app.route('/')
def index():
    session.pop('id', None)
    return render_template('login_registration.html')

@app.route('/registration', methods=['POST'])
def register():
    category_count = 0
    if len(request.form['first_name']) < 2 or not request.form['first_name'].isalpha():
        flash('must be at least 2 characters and letters only', 'first')
    else:
        firstName = request.form['first_name']
        category_count += 1
    
    if len(request.form['last_name']) < 2 or not request.form['last_name'].isalpha():
        flash('must be at least 2 characters and letters only', 'last')
    else:
        lastName = request.form['last_name']
        category_count += 1
    
    if not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address', 'emailAddress')
    else:
        emails = request.form['email']
        category_count += 1
    
    if len(request.form['pw_confirm']) < 8:
        flash('must be at least 8 characters', 'pw')
    else:
        pwds = md5.new(request.form['password']).hexdigest()
        category_count += 1
    
    if not md5.new(request.form['password']).hexdigest() == md5.new(request.form['pw_confirm']).hexdigest():
        flash('passwords do not match', 'pwConfirm')
    else:
        category_count += 1
    
    if category_count == 5:
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (:first, :last, :emailAddress, :pw)'
        data = {
            'first': firstName,
            'last': lastName,
            'emailAddress': emails,
            'pw': pwds
        }
        users = mysql.query_db(query, data)
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email_login = request.form['emailLogin']
    pw_login = md5.new(request.form['pwLogin']).hexdigest()

    query = 'SELECT * FROM users WHERE email = :emails AND password = :pw'
    data = {
        'emails': email_login,
        'pw': pw_login
    }
    users = mysql.query_db(query, data)
    if users:
        session['id'] = users[0]['id']
        session['first_name'] = users[0]['first_name']
        session['last_name'] = users[0]['last_name']
        return redirect('/success')
    else:
        flash('wrong email or password', 'login')
        return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)