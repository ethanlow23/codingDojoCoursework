from flask import Flask, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def dojo_survey():
    return render_template('dojoSurveyValid.html')

@app.route('/result', methods=['POST'])
def result():
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    if len(request.form['name']) < 1:
        flash('name cannot be blank')
        return render_template('dojoSurveyValid.html')
    else:
        session['name'] = request.form['name']
        if len(request.form['description']) < 1:
            flash('comments cannot be blank')
            return render_template('dojoSurveyValid.html')
        elif len(request.form['description']) > 120:
            flash('too many words')
            return render_template('dojoSurveyValid.html')
        else:
            session['description'] = request.form['description']
    return render_template('result.html')

app.run(debug=True)