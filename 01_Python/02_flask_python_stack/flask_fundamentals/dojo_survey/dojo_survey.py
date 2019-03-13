from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def dojo_survey():
    return render_template('dojo_survey.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    description = request.form['description']
    return render_template('result.html', name = name, description = description, location = location, language = language)

app.run(debug=True)