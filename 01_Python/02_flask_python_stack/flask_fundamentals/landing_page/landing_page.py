from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/ninjas')
def ninjas():
    return render_template('landingPageNinja.html')

@app.route('/dojos/new', methods=['POST'])
def dojos():
    return render_template('landingPageDojos.html')
app.run(debug=True)