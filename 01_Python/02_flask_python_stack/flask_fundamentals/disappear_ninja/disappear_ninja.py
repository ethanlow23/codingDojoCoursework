from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'thisIsSecret'

@app.route('/')
def disappear_ninja():
    return render_template('disappear_ninja.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja_turtles.html')

@app.route('/ninja/<color>')
def turtle_color(color):
    session['ninja_turtle'] = ''
    if color == 'red':
        session['ninja_turtle'] = 'raphael.jpg'
    elif color == 'blue':
        session['ninja_turtle'] = 'leonardo.jpg'
    elif color == 'orange':
        session['ninja_turtle'] = 'michelangelo.jpg'
    elif color == 'purple':
        session['ninja_turtle'] = 'donatello.jpg'
    else:
        session['ninja_turtle'] = 'notapril.jpg'
    return render_template('ninja_color.html')

app.run(debug=True)