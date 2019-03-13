from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def greatNumGame():
    session['winning_num'] = random.randrange(0, 101)
    return render_template('great_number.html')

@app.route('/guess_num', methods=['POST'])
def check_num():
    guess = int(request.form['number'])
    correct = False
    while not correct:
        if guess == session['winning_num']:
            session['result'] = 'winner'
            correct = True
        elif guess < session['winning_num']:
            session['result'] = 'too low'
            print session['winning_num']
            return render_template('great_number.html')
        elif guess > session['winning_num']:
            session['result'] = 'too high'
            print session['winning_num']
            return render_template('great_number.html')
        return render_template('greatNumReset.html')

@app.route('/reset', methods=['POST'])
def reset_game():
    session['result'] = ''
    return redirect('/')

app.run(debug=True)