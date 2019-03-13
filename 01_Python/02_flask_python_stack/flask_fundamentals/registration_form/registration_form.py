from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/information', methods=['POST'])
def form_info():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email_valid')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address', 'email_valid')
    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash('not a real name', 'name_valid')
    if len(request.form['password']) < 8:
        flash('password must be at least 8 characters', 'password_valid')
    elif request.form['password'] != request.form['confirm_password']:
        flash('password does not match', 'password_valid')
    return redirect('/')

app.run(debug=True)