from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def ninja_money():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('ninja_gold.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        session['gold'] += random.randrange(10, 21)
    elif request.form['building'] == 'cave':
        session['gold'] += random.randrange(5, 11)
    elif request.form['building'] == 'house':
        session['gold'] += random.randrange(2, 6)
    elif request.form['building'] == 'casino':
        session['gold'] += random.randrange(-50, 51)
    return redirect('/')

app.run(debug=True)