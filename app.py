from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/contato')
def contact():
    return 'contato'
