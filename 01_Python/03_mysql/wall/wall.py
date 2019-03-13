from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnection
import re, md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnection(app, 'the_wall')

@app.route('/')
def index():
    return render_template('wall_login.html')

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
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :emailAddress, :pw, NOW(), NOW())'
        data = {
            'first': firstName,
            'last': lastName,
            'emailAddress': emails,
            'pw': pwds
        }
        users = mysql.query_db(query, data)
        return redirect('/wall')
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
        return redirect('/wall')
    else:
        flash('wrong email or password', 'login')
        return redirect('/')

@app.route('/wall')
def wall():
    query_msg = 'SELECT * FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.updated_at DESC'
    session['msg'] = mysql.query_db(query_msg)
    query_comment = 'SELECT * FROM comments INNER JOIN messages ON messages.id = comments.message_id INNER JOIN users ON users.id = comments.user_id ORDER BY comments.updated_at ASC'
    session['comment'] = mysql.query_db(query_comment)
    return render_template('wall.html')

@app.route('/messages', methods=['POST'])
def messages():
    query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())'
    data = {
        'user_id': session['id'],
        'message': request.form['message']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments', methods=['POST'])
def comments():
    query = 'INSERT INTO comments (message_id, user_id, comment, updated_at) VALUES (:message_id, :user_id, :comment, NOW())'
    data = {
        'message_id': request.form['msg_id'],
        'user_id': session['id'],
        'comment': request.form['comment']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')
app.run(debug=True)