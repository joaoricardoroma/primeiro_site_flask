from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", messages=False)

@app.route('/contato')
def contact():
    return 'contato'
