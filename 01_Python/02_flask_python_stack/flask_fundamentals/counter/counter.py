from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'thisIsSecret'

@app.route('/')
def session_counter():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('counter.html')

@app.route('/increment_two', methods=['POST'])
def counterPlusTwo():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_counter():
    session['counter'] = 0
    return redirect('/')
app.run(debug=True)