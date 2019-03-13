from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/projects')
def projects():
    return render_template('1_portfolio_projects.html')

@app.route('/about')
def about():
    return render_template('2_portfolio_about.html')

app.run(debug = True)