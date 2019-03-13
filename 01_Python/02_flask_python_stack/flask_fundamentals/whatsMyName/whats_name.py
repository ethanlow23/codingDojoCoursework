from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def whats_name():
    return render_template('whats_name.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    print name
    return redirect('/')
app.run(debug=True)